def solution(s):
    numbers = list(map(int, s.split()))

    max_number = max(numbers)

    min_number = min(numbers)

    answer = f"{min_number} {max_number}"

    return answer
