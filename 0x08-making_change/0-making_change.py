#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins: A list of the values of the coins in your possession.
        total (int): The total amount to be met using the given coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, returns 0.
             If total cannot be met by any number of coins, returns -1.

    """

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Iterate through each coin denomination
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
