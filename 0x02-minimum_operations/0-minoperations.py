#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    Calculates the min num of operations needed to achieve exactly n H chars.

    Args:
    - n: An integer representing the desired number of characters

    Returns:
    - int: The minimum number of operations needed
    """
    if n < 2:
        return 0

    operations_needed = 0  # Total operations needed
    factor = 2  # Start with the smallest prime factor

    while factor <= n:
        if n % factor == 0:  # Check if 'factor' is a prime factor of 'n'
            operations_needed += factor  # Add 'factor' to the total operations
            n //= factor  # Reduce 'n' by dividing it by 'factor'
            factor -= 1  # Decrement 'factor' to check for further occurrences
        factor += 1  # Move to the next potential prime factor

    return operations_needed
