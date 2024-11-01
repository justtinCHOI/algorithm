def solution(number):
    primes = [True] * (number + 1)

    for i in range(2, number):
        if primes[i]:
            for j in range(i * i, number + 1, i):
                primes[j] = False

    return [i for i in range(2, number + 1) if primes[i]]

print(solution(10))
