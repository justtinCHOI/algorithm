def bubble_swap(arr: list, a: int , b: int) -> list:
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def solution(arr: list) -> list:
    length = len(arr)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1) :
            if arr[j] > arr[j + 1]:
                bubble_swap(arr, j, j + 1)
                swapped = True
        if not swapped:
            break
    return arr

print(solution([7, 5, 3, 2, 1]))