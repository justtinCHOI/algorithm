import pandas as pd
import random
import os
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows에서는 'Malgun Gothic' 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# Random seed 설정 (데이터 재현성 확보)
random.seed(42)

# 경로 설정
output_dir = 'gradeManagement_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 파일 경로 설정
files = {
    'students': f'{output_dir}/students.csv',
    'midterm': f'{output_dir}/midterm.csv',
    'final': f'{output_dir}/final.csv',
    'assignment1': f'{output_dir}/assignment1.csv',
    'assignment2': f'{output_dir}/assignment2.csv',
    'assignment3': f'{output_dir}/assignment3.csv',
    'assignment4': f'{output_dir}/assignment4.csv',
    'attendance': f'{output_dir}/attendance.csv'
}

# 학생 데이터 생성 (학번과 이름)
names = ['최정의', '송인식', '이정권'] + [f'학생{i}' for i in range(4, 38)]
students = [{'학번': f'{random.choice([2021, 2022, 2023, 2024])}E{str(i).zfill(4)}', '이름': name}
            for i, name in enumerate(names, 1)]
df_students = pd.DataFrame(students)

# 성적 생성 함수
def generate_scores():
    return [random.randint(70, 100) if random.random() > 0.05 else None for _ in range(len(df_students))]

# 파일을 읽어오거나, 없을 경우 파일을 생성하는 함수
def load_or_create_file(file_key, df):
    if os.path.exists(files[file_key]):
        print(f"{files[file_key]} 파일이 이미 존재합니다. 데이터를 불러옵니다.")
        return pd.read_csv(files[file_key], dtype={'학번': str})
    else:
        df.to_csv(files[file_key], index=False)
        print(f"{files[file_key]} 파일이 생성되었습니다.")
        return df

# 1. 학생 파일 생성 또는 로드 : students.csv
df_students = load_or_create_file('students', df_students)

# 2. 중간고사 파일 생성 또는 로드 : midterm.csv
df_midterm = pd.DataFrame({'학번': df_students['학번'], '중간고사': generate_scores()})
df_midterm = load_or_create_file('midterm', df_midterm)

# 3. 기말고사 파일 생성 또는 로드 : final.csv
df_final = pd.DataFrame({'학번': df_students['학번'], '기말고사': generate_scores()})
df_final = load_or_create_file('final', df_final)

# 4. 과제 파일 생성 또는 로드 : assignment1.csv ~ assignment4.csv
assignments = []
for i in range(1, 5):
    df_assignment = pd.DataFrame({'학번': df_students['학번'], f'과제{i}': generate_scores()})
    assignments.append(load_or_create_file(f'assignment{i}', df_assignment))

# 5. 출석 파일 생성 또는 로드 : attendance.csv
df_attendance = pd.DataFrame({'학번': df_students['학번'], '출석': [random.randint(70, 100) for _ in range(len(df_students))]})
df_attendance = load_or_create_file('attendance', df_attendance)

print("모든 파일 확인 및 로드 또는 생성 작업이 완료되었습니다.")

# 성적 데이터 병합 (학번 기준)
df_grades = df_students.merge(df_midterm, on='학번', how='left')\
                       .merge(df_final, on='학번', how='left')\
                       .merge(df_attendance, on='학번', how='left')

# 과제 성적 병합
for i, assignment in enumerate(assignments, 1):
    df_grades = df_grades.merge(assignment, on='학번', how='left')

# 결측값(미입력 성적)은 None으로 유지
df_grades.fillna({'중간고사': 0, '기말고사': 0, '출석': 0, '과제1': 0, '과제2': 0, '과제3': 0, '과제4': 0}, inplace=True)

# 최종 성적 계산
df_grades['최종성적'] = (df_grades['중간고사'] * 0.3 +
                        df_grades['기말고사'] * 0.3 +
                        (df_grades[f'과제1'] + df_grades[f'과제2'] + df_grades[f'과제3'] + df_grades[f'과제4']) * 0.05 +
                        df_grades['출석'] * 0.2)

# 평점 부여 (출석 성적이 60점 미만이면 F)
def calculate_grade(row):
    if row['출석'] < 60:
        return 'F'
    elif row['최종성적'] >= 90:
        return 'A'
    elif row['최종성적'] >= 80:
        return 'B'
    elif row['최종성적'] >= 70:
        return 'C'
    elif row['최종성적'] >= 60:
        return 'D'
    else:
        return 'F'

df_grades['평점'] = df_grades.apply(calculate_grade, axis=1)

# 이름 순으로 정렬
df_grades.sort_values(by='이름', inplace=True)

# 결과 출력
print(df_grades[['학번', '이름', '최종성적', '평점']])

# 평점별 분포 그래프 그리기
grade_distribution = df_grades['평점'].value_counts()
grade_distribution.plot(kind='bar', color='skyblue')
plt.title('평점 분포')
plt.xlabel('평점')
plt.ylabel('학생 수')
plt.show()
