# The function efficiently finds the pair in O(n) time complexity, taking advantage of the sorted property of the array.
def find_pair_with_sum(arr, target):
    # Step 1: Sort the array
    # arr.sort()    sorting step makes it slightly less efficient than directly applying the two-pointer technique to a sorted array

    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    # Traverse the array with the two pointers
    # The function efficiently finds the pair in O(n) time complexity, taking advantage of the sorted property of the array.
    while left < right:
        current_sum = arr[left] + arr[right]

        # Check if the current sum matches the target
        if current_sum == target:
            return (arr[left], arr[right])  # Found the pair

        # Move the left pointer to increase sum
        elif current_sum < target:
            left += 1

        # Move the right pointer to decrease sum
        else:
            right -= 1

    # If no pair found
    return None


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
target = 9
result = find_pair_with_sum(arr, target)
if result:
    print(f"Pair found: {result}")
else:
    print("No pair with the given sum found.")
