#!/usr/bin/python3
"""
Using DFS algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list of lists where each inner list represents a box containing keys to other boxes.

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
