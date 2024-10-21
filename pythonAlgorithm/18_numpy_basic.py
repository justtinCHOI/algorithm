import numpy as np


def print_random_values():
    # 0과 1 사이의 균일 난수 두 개 생성
    uniform_random = np.random.rand(2)
    print("Uniform random values between 0 and 1:", uniform_random)

    # 평균 1, 표준편차 1인 정규분포 난수 두 개 생성
    normal_random = np.random.randn(2)
    print("Normal random values with mean 0 and standard deviation 1:", normal_random)

    # 1에서 10 사이의 정수 난수 세 개 생성
    integer_random = np.random.randint(1, 10, size=30)
    print("Integer random values between 1 and 10:", integer_random)

    # 0에서 9 사이의 정수 난수를 2x2 배열로 생성
    integer_random_array = np.random.randint(10, size=[2, 2])
    print("2x2 array of integer random values between 0 and 9:\n", integer_random_array)


# 함수 실행
print_random_values()
