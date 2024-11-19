# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [3, 1, 8, 4, 9, 5, 2, 6, 7]
target = 3


# O(n)
def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


# using enumeration
def linear_search_enumeration(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


result = linear_search(arr, target)
print(f"the index for target: {target} is {result}")
