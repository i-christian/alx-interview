#!/usr/bin/python3
"""
Using DFS algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes: A list of lists

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Start with the first box
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                stack.append(key)
                visited[key] = True
    return all(visited)
