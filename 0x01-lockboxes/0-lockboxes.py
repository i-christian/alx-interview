#!/usr/bin/python3
from collections import deque
"""
Using BFS algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes: A list of lists.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    visited = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        visited.add(current_box)
        for key in boxes[current_box]:
            if key not in visited:
                queue.append(key)

    return len(visited) == len(boxes)
