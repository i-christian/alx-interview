"""
Pascal triangle implementation using dynamic programming
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row using dynamic programming
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            left_val = triangle[i - 1][j - 1]
            right_val = triangle[i - 1][j]
            row.append(left_val + right_val)
        row.append(1)  # Adding the last element for each row
        triangle.append(row)

    return triangle
