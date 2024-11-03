#Here’s a classic two-pointer algorithm example in Python: finding pairs in a sorted array that sum up to a given target. This approach is efficient with a time complexity of O(n), making it ideal for scenarios where you need to find pairs without using nested loops.

#Problem Statement

#Given a sorted array of integers and a target sum, find all unique pairs in the array that add up to the target sum.

def find_pairs_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            result.append((arr[left], arr[right]))
            left += 1
            right -= 1
            # Skip duplicate pairs
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return result

arr = [1, 2, 3, 4, 5, 6, 7]
target = 3
print(find_pairs_with_sum(arr, target))