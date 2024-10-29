# we could've sorted out the array, but the extra sorting step
# makes it slightly less efficient than directly applying
# the two-pointer technique to a sorted array.

def find_pair_with_sum_unsorted(arr, target):
    seen_numbers = set()

    for num in arr:
        complement = target - num
        if complement in seen_numbers:
            return (complement, num)
        seen_numbers.add(num)

    return None


# Example usage
arr = [4, 2, 7, 1, 5, 6, 3]
target = 9
result = find_pair_with_sum_unsorted(arr, target)
if result:
    print(f"Pair found: {result}")
else:
    print("No pair with the given sum found.")
