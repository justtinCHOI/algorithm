def solution(n):
    answer = 0
    k = 1

    # k(k+1)/2 <= n 인 k의 최대값까지만 검사
    while k * (k - 1) // 2 < n:
        kx = n - k * (k - 1) // 2
        if kx > 0 and kx % k == 0:
            answer += 1
        k += 1

    return answer