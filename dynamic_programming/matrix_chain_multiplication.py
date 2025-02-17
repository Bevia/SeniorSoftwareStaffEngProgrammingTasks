# Interview Question
# Given a sequence of matrices, write a function to find the minimum
# number of scalar multiplications needed to multiply the chain of matrices.
# The dimensions of the matrices are provided in an array, where the (i)-th matrix has dimensions ((p[i-1] times p[i])).
# Your solution should aim to have an optimal time complexity.

# Example:
# Input: [1, 2, 3, 4]
# Output: 18
# Explanation: The matrices dimensions are (1x2), (2x3), (3x4).
# The most efficient way to multiply these matrices is (A1(A2A3))
# which requires 18 multiplications.

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[0][n - 1]
