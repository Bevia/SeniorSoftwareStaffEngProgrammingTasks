# Function to find the length of the longest common subsequence
def lcs(X, Y):
    # Lengths of the input sequences
    m = len(X)
    n = len(Y)

    # Create a 2D table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # If characters match, add 1 to the previous diagonal value
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # If they don't match, take the maximum of the previous row or column
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of LCS is in the bottom-right cell
    return dp[m][n]


# Example usage
X = "ABCBDAB"
Y = "BDCAB"

lcs_length = lcs(X, Y)
print("Length of LCS:", lcs_length)