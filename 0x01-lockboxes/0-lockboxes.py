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
    visited = set()
    stack = [0]  # Start with the first box
    while stack:
        current_box = stack.pop()
        visited.add(current_box)
        for key in boxes[current_box]:
            if key < num_boxes and key not in visited:
                stack.append(key)
    return len(visited) == num_boxes
