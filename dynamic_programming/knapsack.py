# Function to solve the knapsack problem
def knapsack(weights, values, capacity):
    # Number of items
    n = len(values)

    # Create a 2D DP table where dp[i][w] will store the maximum value
    # for a capacity w using the first i items
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Populate the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If item i-1 can fit in the current capacity w
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # Otherwise, skip item i-1

    # The maximum value will be at dp[n][capacity]
    return dp[n][capacity]


# Example usage
weights = [2, 3, 4, 5]  # Weights of the items
values = [3, 4, 5, 6]  # Values of the items
capacity = 5  # Capacity of the knapsack

# Find the maximum value we can fit in the knapsack
max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)