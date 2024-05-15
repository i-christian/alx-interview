#!/usr/bin/python3
"""Prime Game Module."""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums: List of integers representing the range of nums for each round.

    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben").
        None: If the input is invalid or the winner cannot be determined.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Remove multiples of a given prime number from the list.

    Args:
        ls (list): The list of integers where multiples are to be removed.
        x (int): The prime number whose multiples are to be removed.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
