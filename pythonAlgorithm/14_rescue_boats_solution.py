def solution(people, limit):

    people.sort()

    boats = 0
    left, right = 0, len(people) - 1

    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    if left == right:
        boats += 1

    return boats