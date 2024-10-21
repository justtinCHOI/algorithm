import pandas as pd
import random
import os
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows에서는 'Malgun Gothic' 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 경로 설정
output_dir = 'generated_files'
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
    return [random.randint(50, 100) if random.random() > 0.1 else None for _ in range(len(df_students))]

# 파일이 존재하는지 확인하고, 없으면 생성하는 함수
def create_file_if_not_exists(file_key, df):
    if not os.path.exists(files[file_key]):
        df.to_csv(files[file_key], index=False)
        print(f"{files[file_key]} 파일이 생성되었습니다.")
    else:
        print(f"{files[file_key]} 파일이 이미 존재합니다.")

# 1. students.csv 생성
create_file_if_not_exists('students', df_students)

# 2. midterm.csv 생성
df_midterm = pd.DataFrame({'학번': df_students['학번'], '중간고사': generate_scores()})
create_file_if_not_exists('midterm', df_midterm)

# 3. final.csv 생성
df_final = pd.DataFrame({'학번': df_students['학번'], '기말고사': generate_scores()})
create_file_if_not_exists('final', df_final)

# 4. assignment1.csv ~ assignment4.csv 생성
for i in range(1, 5):
    df_assignment = pd.DataFrame({'학번': df_students['학번'], f'과제{i}': generate_scores()})
    create_file_if_not_exists(f'assignment{i}', df_assignment)

# 5. attendance.csv 생성
df_attendance = pd.DataFrame({'학번': df_students['학번'], '출석': [random.randint(50, 100) for _ in range(len(df_students))]})
create_file_if_not_exists('attendance', df_attendance)

print("모든 파일 확인 및 생성 작업이 완료되었습니다.")

# 생성된 파일들을 읽어서 데이터프레임으로 로드 (학번을 문자열로 명시적으로 지정)
df_midterm = pd.read_csv(files['midterm'], dtype={'학번': str})
df_final = pd.read_csv(files['final'], dtype={'학번': str})
df_attendance = pd.read_csv(files['attendance'], dtype={'학번': str})
assignments = [pd.read_csv(files[f'assignment{i}'], dtype={'학번': str}) for i in range(1, 5)]

# 성적 데이터 병합 (학번 기준)
df_grades = df_students.merge(df_midterm, on='학번', how='left')\
                       .merge(df_final, on='학번', how='left')\
                       .merge(df_attendance, on='학번', how='left')

# 과제 성적 병합
for i, assignment in enumerate(assignments, 1):
    df_grades = df_grades.merge(assignment, on='학번', how='left')

# 결측값(미입력 성적)은 0으로 채움
df_grades.fillna(0, inplace=True)

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
