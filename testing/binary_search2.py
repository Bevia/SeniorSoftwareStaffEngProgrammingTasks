# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [3, 1, 8, 4, 9, 5, 2, 6, 7]  # in this case you either sort the array or use linear search
target = 3

# if we sort the array the time complexity would be O(n log n), which is worse than linear


# binary search is O(log n)
def binary_search(arr, target):
    arr.sort()  # don't do this...
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


result = binary_search(arr, target)
print(f"the index of target {target} is {result}")
