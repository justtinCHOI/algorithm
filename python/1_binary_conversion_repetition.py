def solution(s):
    count_transform = 0
    total_count_zero = 0

    while s != "1":
        count_zero = s.count("0")
        total_count_zero += count_zero

        s = s.replace("0", "")
        length = len(s)

        s = bin(length)[2:]
        count_transform += 1

    return [count_transform, total_count_zero]