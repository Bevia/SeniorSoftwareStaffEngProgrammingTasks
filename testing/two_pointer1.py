arr = [1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
target = 8

# find values in the array that will add up 11 could be one or many, don't allow duplicates


def two_pointer(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


def two_pointer_values(arr, target):
    left, right = 0, len(arr)-1
    pairs = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs


result = two_pointer_values(arr, target)
print(f"the two values that add up to {target} are {result}")



