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

    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
