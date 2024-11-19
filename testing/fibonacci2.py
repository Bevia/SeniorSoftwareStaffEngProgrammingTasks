# find the fibonacci sequence for up to n = 8
# test for edge cases, for instance n = 1

# the naive recursive Fibonacci function does not use memoization
# or dynamic programming and hence exhibits exponential complexity.
#
# The total number of calls for  \text{find_fibonacci(n)}  grows exponentially because the function recomputes the same values multiple times.
#
# For example:
# 	•	 n = 3 : 5 calls.
# 	•	 n = 4 : 9 calls.
# 	•	 n = 5 : 15 calls.
# 	•	 n = 6 : 29 calls.

# 1,1,2,3,5,8,13 ....

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


n = 7
result = fibonacci(n)
print(f"the sequence result for {n} is {result}")
