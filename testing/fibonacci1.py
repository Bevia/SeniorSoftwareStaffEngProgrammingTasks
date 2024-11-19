# resulting in exponential time complexity O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoization(n, memo={}):
    # Check if the result for n is already cached
    if n in memo:
        return memo[n]

    # Base case: trivial Fibonacci values
    if n <= 1:
        return n

    # Recursive calculation with memoization
    memo[n] = memoization(n - 1, memo) + memoization(n - 2, memo)
    return memo[n]


def tabulation(n):
    if n <= 1:
        return n
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]


def main():
    result1 = fibonacci(7)
    result2 = memoization(7)
    result3 = tabulation(7)

    print(f"fiboancci result {result1}")
    print(f"fiboancci memoization result {result2}")
    print(f"fiboancci tabulation result {result3}")


if __name__ == "__main__":
    main()
