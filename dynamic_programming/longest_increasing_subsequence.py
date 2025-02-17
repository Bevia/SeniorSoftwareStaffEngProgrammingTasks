#  Question: Given an array of integers, write a function to find the length of
#  the longest increasing subsequence (LIS). An increasing subsequence is
#  a subsequence of elements in the array such that the elements are in
#  strictly increasing order. Your solution should aim to have an optimal time complexity.
# Example:
# Input: [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4
# Explanation: The longest increasing subsequence is [2, 3, 7, 101], so the length is 4.

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
