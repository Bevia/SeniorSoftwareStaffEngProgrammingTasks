# the Fibonacci sequence is defined as:
# F(n) = F(n-1) + F(n-2)
# 1 1 2 3 5 8 13 21 34 55
#

# recursive approach
def fib_recursive(n):
    if n <= 1:  # base cases are 0 and 1
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Without memoization, each recursive call would recompute the same Fibonacci values many times,
# resulting in exponential time complexity O(2^n). Memoization improves this to
# linear time complexity O(n) by storing and reusing results.
# Using memoization (top-down approach):
# memo={} is an empty dictionary
def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    # memo[10] = fib_memoization(9) + fib_memoization(8)
    # this is actually the formula: F(n) = F(n-1) + F(n-2)
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]


# using tabulation (bottom-up approach):
# Computes Fibonacci numbers iteratively, filling in values from the base cases up to the desired n.
# Uses a table to store each computed Fibonacci number, which allows it to access previously computed values instantly.
# Is efficient in terms of both time (O(n)) and memory (O(n)) compared to the naive recursive approach.
def fib_tabulation(n):
    # base case:
    if n <= 1:
        return n
    # fib_table repeats the list [0] a total of  n+1  times, effectively creating a list of  n+1  zeros.
    fib_table = [0] * (n + 1)  # for example for n = 5 we have this: fib_table = [0, 0, 0, 0, 0, 0]
    fib_table[1] = 1  # sets the value of fib_table[1] to 1 because this is one of the base cases of the Fibonacci sequence
    for i in range(2, n + 1):   # starts a loop that iteratively fills in the fib_table list from index 2 up to n
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]

# Execution Flow Example for n = 5
#
# 	1.	Initialization: fib_table = [0, 1, 0, 0, 0, 0]
# 	2.	Loop Iterations:
# 	•	i = 2: Compute  fib_table[2] = fib_table[1] + fib_table[0] = 1 + 0 = 1  → fib_table = [0, 1, 1, 0, 0, 0]
# 	•	i = 3: Compute  fib_table[3] = fib_table[2] + fib_table[1] = 1 + 1 = 2  → fib_table = [0, 1, 1, 2, 0, 0]
# 	•	i = 4: Compute  fib_table[4] = fib_table[3] + fib_table[2] = 2 + 1 = 3  → fib_table = [0, 1, 1, 2, 3, 0]
# 	•	i = 5: Compute  fib_table[5] = fib_table[4] + fib_table[3] = 3 + 2 = 5  → fib_table = [0, 1, 1, 2, 3, 5]
# 	3.	Return:  fib_table[5] = 5


# alternatively:
# if you want to reduce the space complexity to  O(1) ,
# you can avoid storing the entire table and only
# keep the last two Fibonacci numbers:
def fib_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    n = 3
    print(f"Fibonacci Recursive({n}) = {fib_recursive(n)}")
    print(f"Fibonacci Memoization({n}) = {fib_memoization(n)}")
    print(f"Fibonacci Tabulation({n}) = {fib_tabulation(n)}")
    print(f"Fibonacci Optimize({n}) = {fib_optimized(n)}")
