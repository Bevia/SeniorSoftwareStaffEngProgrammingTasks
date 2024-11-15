# find the fibonacci sequence for up to n = 8
# test for edge cases, for instance n = 1


def find_fibonacci(n):
    # base case
    if n <= 1:
        return n
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)


n = 6
result = find_fibonacci(n)
print(f"fibonacci sequence for {n} is {result}")
