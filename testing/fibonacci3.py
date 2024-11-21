def memoization(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = memoization(n-1, memo) + memoization(n-2, memo)
    return memo[n]


def tabulation(n):
    if n <= 1:
        return n

    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = tabulation(i-1) + tabulation(i-2)
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


n = 9
result = tabulation(n)
print(f"the fibonacci sequence of {n} is {result}")

# 1,2,3,4,5,6, 7, 8, 9
# 1,1,2,3,5,8,13,21,34
