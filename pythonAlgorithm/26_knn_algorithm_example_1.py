import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 데이터 로드
df = pd.read_csv('Student_Marks.csv')

# 데이터 정보
df.info()

# 상관도 확인
print("Correlation Matrix:\n", df.corr())

# 그래프
sns.regplot(x='number_courses', y='Marks', data=df)
plt.title("Number of Courses vs Marks")
plt.show()

sns.regplot(x='time_study', y='Marks', data=df)
plt.title("Time Spent Studying vs Marks")
plt.show()

# 학습 데이터와 테스트 데이터 분리
x = df[['number_courses', 'time_study']]  # 독립 변수
y = df['Marks']  # 종속 변수
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# 모델 학습
model = LinearRegression()
model.fit(x_train, y_train)

# 예측
y_pred = model.predict(x_test)

# 결과 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# 실제 값 vs 예측 값 비교
comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nActual vs Predicted Values:")
print(comparison_df)

# 시각화: 실제 값 vs 예측 값
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_pred)), y_pred, label='Predicted', alpha=0.7, color='red')
plt.title("Actual vs Predicted Marks")
plt.xlabel("Test Sample Index")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.show()
