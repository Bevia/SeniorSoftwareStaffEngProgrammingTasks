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
        fib_table[i] = tabulation(n-1) + tabulation(n-2)
    return fib_table[n]


n = 9
result = tabulation(n)
print(f"the fibonacci sequence of {n} is {result}")

# 1,2,3,4,5,6, 7, 8, 9
# 1,1,2,3,5,8,13,21,34
