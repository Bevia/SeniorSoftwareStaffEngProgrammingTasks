arr = [1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
pair_sum = 8


def find_pair(arr, pair_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == pair_sum:
            return arr[left], arr[right]
        elif current_sum < pair_sum:
            left += 1
        else:
            right -= 1
    return None


def find_pairs(arr, pair_sum):
    left, right = 0, len(arr) - 1
    pairs = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == pair_sum:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < pair_sum:
            left += 1
        else:
            right -= 1
    return pairs


def find_unique_pairs(arr, pair_sum):
    left, right = 0, len(arr)-1
    pairs = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == pair_sum:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
            while current_sum == pair_sum and arr[left] == arr[left - 1]:
                left += 1
            while current_sum == pair_sum and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < pair_sum:
            left += 1
        else:
            right -= 1
    return pairs


result = find_unique_pairs(arr, pair_sum)
if not result:
    print(f"no pairs found")
else:
    print(f"the pair the sum of {pair_sum} are {result}")
