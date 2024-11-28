#!/usr/bin/python3
"""
Module to solve the making change problem
"""

def makeChange(coins, total):
    # If total is 0 or negative, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize a DP array with a value higher than any possible number of coins
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 total requires 0 coins
    dp[0] = 0
    
    # Iterate over all coin denominations
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, it's not possible to form the total
    return dp[total] if dp[total] != float('inf') else -1
