def solution(n):
    return bin(n).count('1')

def solution2(n):
    battery_usage = 0
    while n > 0:
        if n % 2 == 1:
            battery_usage += 1
            n //= 2
        else:
            n //= 2
    return battery_usage