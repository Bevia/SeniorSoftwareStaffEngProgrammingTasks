
# the naive recursive Fibonacci function does not use memoization
# or dynamic programming and hence exhibits exponential complexity.
#
# The total number of calls for  \text{find_fibonacci(n)}
# grows exponentially because the function recomputes
# the same values multiple times.

# Fibonacci formula: F(n) = F(n-1) + F(n-2)
#
# For example:
# 	•	 n = 3 : 5 calls.
# 	•	 n = 4 : 9 calls.
# 	•	 n = 5 : 15 calls.
# 	•	 n = 6 : 29 calls.

# 1,1,2,3,5,8,13,21,34 ....


# O(2^n)
def fibonacci(n):
    # base case
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# To reduce the time complexity, you can use memoization
# or dynamic programming, which reduces the time complexity
# to  O(n)  by storing intermediate results and avoiding redundant calculations.


def fibonacci_memoization(n, memo={}):
    #base case
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]


# This initial return memo[n] avoids even considering
# the base case if the result is already cached.
# This improves clarity and might slightly improve runtime
# for edge cases (though this difference is negligible).
def better_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = better_fibonacci(n-1, memo) + better_fibonacci(n-2, memo)
    return memo[n]


n = 9
result = fibonacci_memoization(n)
print(f"the fibonacci series result for {n} is {result}")
