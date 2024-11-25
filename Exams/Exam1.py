# 1) find the fibonacci for n = 8 for time complexity O(2^n), and O(n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memoization(n - 1, memo) + memoization(n - 2, memo)
    return memo[n]


def tabulation(n):
    if n <= 1:
        return n
    fib_tab = [0] * (n + 1)
    fib_tab[1] = 1
    for i in range(2, n + 1):
        fib_tab[i] = fib_tab[i - 1] + fib_tab[i - 2]
    return fib_tab[n]


# n = 8
# result = tabulation(n)
# print(f"the fibonacci result for n {n} is {result}")

# ************************ end ***************************

# 2) find the pairs of number/numbers that add up to 11 from this array
# arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9]
# notice that there might be more than one pair, don't allow duplicates
# arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9]
# target = 17

def find_pair(arr, target):
    left, right = 0, len(arr) - 1
    current_pair = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            current_pair.append((arr[left], arr[right]))
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
            # return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return current_pair


# result = find_pair(arr, target)
# print(f"the pair that add up to {target} are {result}")

# ************************ end ***************************

# 3) use linear search to find index of number 6 in this array: arr = [2, 7, 1, 6, 8, 9]
def linear_search(arr, target):
    # n = len(arr)
    # for i in range(n):
    #     if arr[i] == target:
    #         return i
    # return -1
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# arr = [2, 7, 1, 6, 8, 9]
# target = 6
# result = linear_search(arr, target)
# print(f"the index for target {target} is {result}")


# 4) use binary search to find value 7 in the array
# arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5


def binary_search(arr, target):
    """Returns the index of 'target' in 'arr', or -1 if not found."""
    left, right = 0, len(arr) - 1
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
print(f"the index for value {target} is {result}")

# DONE: VB
# test result 9 our of 10, this was wrong:
#             while left < right and arr[left] == arr[left + 1]:
#                 left += 1
#             while left < right and arr[right] == arr[right - 1]:
#                 right -= 1
# has been corrected in code!
