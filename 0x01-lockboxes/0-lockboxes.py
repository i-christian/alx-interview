#!/usr/bin/python3
"""
Using BFS algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list of lists where each inner list represents a box containing keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    def dfs(current_box, visited):
        visited.add(current_box)
        for key in boxes[current_box]:
            if key not in visited:
                dfs(key, visited)

    visited = set()
    dfs(0, visited)

    return len(visited) == len(boxes)
