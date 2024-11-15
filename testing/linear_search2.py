# arr = [1, 3, 5, 6, 7, 8, 9]
arr = [3, 9, 1, 5, 7, 8, 6]
target = 6
# find the index for 5
# both solutions are log (n)


def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


def linear_search_enumeration(arr, target):
    for i, n in enumerate(arr):
        if n == target:
            return i
    return -1


result = linear_search_enumeration(arr, target)
print(f"the index for {target} is {result}")