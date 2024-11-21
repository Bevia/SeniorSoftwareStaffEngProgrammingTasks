def memoization(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = memoization(n-1, memo) + memoization(n-2, memo)
    return memo[n]


n = 9
result = memoization(n)
print(f"the fibonacci sequence of {n} is {result}")

# 1,1,2,3,5,8,13,21,34
