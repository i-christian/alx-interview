#!/usr/bin/python3
"""
.0-minoperations.py
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve n characters.

    Args:
    - n: An integer representing the desired number of characters

    Returns:
    - int: The minimum number of operations needed
    """
    if n <= 1:
        return 0

    memo = {}  # Memoization dictionary

    def min_operations_recursive(n):
        if n in memo:
            return memo[n]

        min_ops = n  # Initialize min_ops with worst-case scenario

        for i in range(2, n // 2 + 1):
            if n % i == 0:
                min_ops = min(min_ops, min_operations_recursive(i) + min_operations_recursive(n // i))

        memo[n] = min_ops
        return min_ops

    return min_operations_recursive(n)
