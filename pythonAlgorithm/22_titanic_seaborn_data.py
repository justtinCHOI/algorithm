import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 타이타닉 데이터셋 불러오기
titanic = sns.load_dataset('titanic')

# 데이터의 기본 정보 확인
print("데이터의 기본 정보:\n", titanic.info())
print("\n데이터의 첫 5행:\n", titanic.head())
print("\n기술 통계:\n", titanic.describe())

# 결측치 확인
print("\n결측치 정보:\n", titanic.isnull().sum())

# # 성별 생존율 시각화
# plt.figure(figsize=(8, 6))
# sns.countplot(data=titanic, x='sex', hue='survived')
# plt.title("성별에 따른 생존자 수")
# plt.xlabel("성별")
# plt.ylabel("인원 수")
# plt.legend(['사망', '생존'])
# plt.show()
#
# # 나이 분포 시각화
# plt.figure(figsize=(8, 6))
# sns.histplot(titanic['age'], bins=30, kde=True)
# plt.title("나이 분포")
# plt.xlabel("나이")
# plt.ylabel("빈도수")
# plt.show()
#
# # 클래스별 생존율 시각화
# plt.figure(figsize=(8, 6))
# sns.barplot(data=titanic, x='pclass', y='survived')
# plt.title("클래스별 생존율")
# plt.xlabel("티켓 클래스")
# plt.ylabel("생존율")
# plt.show()

# 타이타닉 데이터셋 불러오기
titanic = sns.load_dataset('titanic')

# 나이를 10대 단위로 나누어 생존자 분포 확인
titanic['age_group'] = pd.cut(titanic['age'], bins=range(0, 81, 10), right=False, labels=["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79"])

# 나이 그룹별 생존자와 사망자 수 계산
rt= titanic.groupby('age_group')['survived'].value_counts().unstack().fillna(0)

# 생존율 계산
rt['survival_rate'] = rt[1] / (rt[1] + rt[0]) * 100

# 데이터 리셋 및 시각화
rt = rt.reset_index()

# 나이대별 생존율 시각화
plt.figure(figsize=(10, 6))
sns.barplot(data=rt, x='age_group', y='survival_rate')
plt.title("나이대별 생존율")
plt.xlabel("나이대")
plt.ylabel("생존율 (%)")
plt.show()
