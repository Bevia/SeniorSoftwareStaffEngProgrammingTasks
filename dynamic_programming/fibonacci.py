# the Fibonacci sequence is defined as:
# F(n) = F(n-1) + F(n-2)
# 1 1 2 3 5 8 13 21 34 55
#

# recursive approach
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Without memoization, each recursive call would recompute the same Fibonacci values many times,
# resulting in exponential time complexity O(2^n). Memoization improves this to
# linear time complexity O(n) by storing and reusing results.
# Using memoization (top-down approach):
def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    # memo[10] = fib_memoization(9) + fib_memoization(8)
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]


# using tabulation (bottom-up approach):
# Computes Fibonacci numbers iteratively, filling in values from the base cases up to the desired n.
# Uses a table to store each computed Fibonacci number, which allows it to access previously computed values instantly.
# Is efficient in terms of both time (O(n)) and memory (O(n)) compared to the naive recursive approach.
def fib_tabulation(n):
    if n <= 1:
        return n
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]


if __name__ == '__main__':
    n = 10
    print(f"Fibonacci Recursive({n}) = {fib_recursive(n)}")
    print(f"Fibonacci Memoization({n}) = {fib_memoization(n)}")
    print(f"Fibonacci Tabulation({n}) = {fib_tabulation(n)}")
