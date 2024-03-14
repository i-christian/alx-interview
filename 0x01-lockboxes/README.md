# Lockboxes

This project aims to develop a method to determine if all the lockboxes in a given set can be opened. Each lockbox may contain keys to other boxes, and the goal is to ascertain whether it's possible to open all the boxes.

## Overview

- **Project Name**: 0x01. Lockboxes
- **Language**: Python
- **Author**: Carrie Ybay, Software Engineer at Holberton School
- **Weight**: 1
- **Start Date**: Mar 11, 2024 5:00 AM
- **End Date**: Mar 15, 2024 5:00 AM
- **Checker Release Date**: Mar 12, 2024 5:00 AM
- **Auto Review**: Will be launched at the deadline

## Must Know

To successfully tackle this project, a solid understanding of various concepts is essential. Below are the key concepts and resources that will aid in developing an efficient solution:

### Concepts Needed

1. **Lists and List Manipulation**:
   - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
   - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

2. **Graph Theory Basics**:
   - Knowledge of graph theory, especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search, can be helpful.
   - [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/introduction-to-breadth-first-search-and-shortest-path)

3. **Algorithmic Complexity**:
   - Understanding the time and space complexity of the solution is crucial.
   - [Big O Notation](https://www.geeksforgeeks.org/analysis-of-algorithms-set-4-analysis-of-loops/)

4. **Recursion**:
   - Some solutions might require a recursive approach to traverse through the boxes and keys.
   - [Recursion in Python](https://realpython.com/python-thinking-recursively/)

5. **Queue and Stack**:
   - Knowing how to use queues and stacks is crucial for implementing BFS or DFS algorithms.
   - [Python Queue and Stack](https://www.geeksforgeeks.org/queue-in-python/)

6. **Set Operations**:
   - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
   - [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

### Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=V8DGdPkBBxg)

## Requirements

### General

- **Allowed Editors**: vi, vim, emacs
- **Interpretation/Compilation Environment**: Ubuntu 20.04 LTS using Python3 (version 3.4.3)
- **File Endings**: All files should end with a new line
- **First Line of Files**: Should be exactly `#!/usr/bin/python3`
- **Mandatory Files**: README.md file at the root of the folder
- **Documentation**: Code should be documented
- **PEP 8 Style**: Code should use the PEP 8 style (version 1.7.x)
- **Executable Files**: All files must be executable

## Tasks

### Lockboxes

**Task Description**:
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and may contain keys to other boxes. Write a method that determines if all the boxes can be opened.

**Prototype**: `def canUnlockAll(boxes)`

- `boxes` is a list of lists
- A key with the same number as a box opens that box
- All keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

### Example Usage

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
