import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 'Malgun Gothic' 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 그래프에서 마이너스 기호가 깨지는 현상 해결
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv('./publicDatabase/서울특별시_시간별 (초)미세먼지_20221231/서울시 대기질 자료 제공_2022.csv', encoding='cp949')

# '일시' 컬럼을 날짜-시간 형식으로 변환
df['일시'] = pd.to_datetime(df['일시'])
df['hour'] = df['일시'].dt.hour
df['month'] = df['일시'].dt.month

# 1. 시간대별 미세먼지 및 초미세먼지 수준 변화 시각화
plt.figure(figsize=(12, 6))
hourly_avg = df.groupby('hour')[['미세먼지(PM10)', '초미세먼지(PM2.5)']].mean()
hourly_avg.plot(marker='o', linestyle='-', title='시간대별 평균 미세먼지 (PM10) 및 초미세먼지 (PM2.5) 수준', ax=plt.gca())
plt.xlabel('시간대')
plt.ylabel('농도 (µg/m³)')
plt.legend(title='오염물질 종류')
plt.grid()
plt.show()

# 2. 구별 미세먼지 및 초미세먼지 분포
plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='구분', y='미세먼지(PM10)')
plt.title('구별 미세먼지 (PM10) 수준 분포')
plt.xlabel('구분')
plt.ylabel('미세먼지 농도 (PM10)')
plt.xticks(rotation=45)
plt.show()

# 3. 월별 미세먼지 및 초미세먼지 수준 변화
monthly_avg = df.groupby('month')[['미세먼지(PM10)', '초미세먼지(PM2.5)']].mean()
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', ax=plt.gca(), color=['#3498db', '#e74c3c'])
plt.title('월별 평균 미세먼지 (PM10) 및 초미세먼지 (PM2.5) 수준')
plt.xlabel('월')
plt.ylabel('농도 (µg/m³)')
plt.legend(title='오염물질 종류')
plt.show()

# 4. 초미세먼지(PM2.5)와 미세먼지(PM10) 상관관계
plt.figure(figsize=(10, 6))
sns.regplot(x='미세먼지(PM10)', y='초미세먼지(PM2.5)', data=df, scatter_kws={'alpha':0.2}, line_kws={'color': 'red'})
plt.title('미세먼지(PM10)와 초미세먼지(PM2.5) 상관관계')
plt.xlabel('미세먼지(PM10)')
plt.ylabel('초미세먼지(PM2.5)')
plt.grid()
plt.show()
