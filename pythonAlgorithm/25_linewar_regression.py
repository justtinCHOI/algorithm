import matplotlib.pyplot as plt
from Demos.SystemParametersInfo import x
from sklearn.linear_model import LinearRegression

# 머신러닝 학습
LR_model = LinearRegression()
LR_model.fit(x, y)

# 예측하기
prd = LR_model.predict([[7],[12]])
prd

plt.scatter(x, y, label='Train Data')
plt.scatter([7, 12], prd, marker='v', label='Predicted Data')
plt.legend()
plt.show()

line_x = np.array([1, 12])
line_y = line_x * LR_model.coef_[0] + LR_model.intercept_
plt.plot(line_x, line_y, label='Linear Regression')
plt.legend()
plt.show()

