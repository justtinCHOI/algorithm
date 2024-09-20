import math

def solution(brown, yellow):

    sub = (brown // 2) + 2
    mul = brown + yellow

    disc = math.sqrt(sub**2 - 4 * mul)

    width = (sub + disc) / 2
    height = (sub - disc) / 2
    return [int(width), int(height)]