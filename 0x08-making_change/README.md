# 0x08. Making Change


## Description
This project, "0. Change comes from within," addresses the classic coin change problem from the domain of dynamic programming and greedy algorithms. The primary objective is to determine the minimum number of coins required to reach a given total amount, given a list of coin denominations.

### Key Concepts
- **Greedy Algorithms:**
    - Understanding the mechanism of greedy algorithms and their suitability for the coin change problem.
    - Identifying scenarios where greedy algorithms may not offer the optimal solution.
- **Dynamic Programming:**
    - Basic principles of dynamic programming for optimization problems.
    - Overlapping subproblems and optimal substructure in the context of the coin change problem.
- **Algorithmic Complexity:**
    - Analysis of time and space complexity.
    - Aim for solutions with lower complexity to meet runtime constraints.
- **Problem-Solving Strategies:**
    - Decomposing the problem into smaller, manageable sub-problems.
    - Comparison of iterative vs. recursive approaches to dynamic programming.
- **Python Programming:**
    - List manipulation and comprehension.
    - Implementing functions with efficient looping and conditional statements.

### Resources
- **Python Official Documentation:**
    - More Control Flow Tools (for loops, if statements)
- **GeeksforGeeks Articles:**
    - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
    - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials:**
    - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jaNZ83Q3QGc) for a visual and step-by-step explanation of the dynamic programming approach.

## Additional Resources
- **Mock Technical Interview**

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should adhere to the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks
### 0. Change comes from within (mandatory)
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- **Prototype:** `def makeChange(coins, total)`
- **Return:** Fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

### Example
```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

## Repo
- **GitHub repository:** [alx-interview](https://github.com/i-christian/alx-interview)
- **Directory:** 0x08-making_change
- **File:** 0-making_change.py
