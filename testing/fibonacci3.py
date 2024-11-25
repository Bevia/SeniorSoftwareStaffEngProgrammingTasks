# Find the fibonacci number for input n
# Recursive Naive which has a time complexity of O(2^n)
# Without memoization, the naive Fibonacci function would have
# a time complexity of  O(2^n)  due to the exponential
# growth of recursive calls.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


# Memoization which has a time complexity of O(n)
def memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memoization(n-1, memo)+memoization(n-2, memo)
    return memo[n]


# Tabulation
def tabulation(n):
    if n <= 1:
        return n
    fib_tab = [0] * (n + 1)
    fib_tab[1] = 1
    for i in range(2, n + 1):
        fib_tab[i] = fib_tab[i-1] + fib_tab[i-2]
    return fib_tab[n]  # After all iterations,  fib_table[5]  contains the 5th Fibonacci number, which is 5.


# Execution Flow Example for n = 5
#
# 	1.	Initialization: fib_table = [0, 1, 0, 0, 0, 0]
# 	2.	Loop Iterations:
# 	•	i = 2: Compute  fib_table[2] = fib_table[1] + fib_table[0] = 1 + 0 = 1  → fib_table = [0, 1, 1, 0, 0, 0]
# 	•	i = 3: Compute  fib_table[3] = fib_table[2] + fib_table[1] = 1 + 1 = 2  → fib_table = [0, 1, 1, 2, 0, 0]
# 	•	i = 4: Compute  fib_table[4] = fib_table[3] + fib_table[2] = 2 + 1 = 3  → fib_table = [0, 1, 1, 2, 3, 0]
# 	•	i = 5: Compute  fib_table[5] = fib_table[4] + fib_table[3] = 3 + 2 = 5  → fib_table = [0, 1, 1, 2, 3, 5]
# 	3.	Return:  fib_table[5] = 5

# Client goes here:

n = 8
result = tabulation(n)
print(f"the fibonacci series for {n} is {result}")

# 1,2,3,4,5,6, 7, 8, 9
# 1,1,2,3,5,8,13,21,34
