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

    # Initialize a list to store the minimum operations for each number
    min_ops = [0] * (n + 1)

    # Iterate from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Initialize the minimum operations for the current number
        min_ops[i] = i

        # Check for all factors of i
        for j in range(2, i // 2 + 1):
            # If j is a factor of i
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + min_ops[i // j])

    return min_ops[n]
