# Rotate 2D Matrix

This repository contains the solution for the "0. Rotate 2D Matrix" project, which is part of the ALX Software Engineering curriculum.

## Project Description

In this project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python.

### Key Concepts

- **Matrix Representation in Python:** Understanding how 2D matrices are represented using lists of lists in Python, and accessing/modifying elements in a 2D matrix.
- **In-place Operations:** Performing operations on data without creating a copy of the data structure, and minimizing space complexity by modifying the matrix in place.
- **Matrix Transposition:** Understanding the concept of transposing a matrix (swapping rows and columns), and implementing matrix transposition as a step in the rotation process.
- **Reversing Rows in a Matrix:** Manipulating rows of a matrix by reversing their order as part of the rotation process.
- **Nested Loops:** Using nested loops to iterate through 2D data structures like matrices, and modifying elements within nested loops to achieve the desired rotation.

### Resources

- **Python Official Documentation:**
- [data structures](https://docs.python.org/3/tutorial/datastructures.html)
- **GeeksforGeeks Articles:**
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- **TutorialsPoint:**
- [Python Lists](https://intranet.alxswe.com/projects/1220)

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving your problem-solving and algorithmic thinking skills in Python.

## Additional Resources

- **Mock Technical Interview** [link](https://www.youtube.com/watch?v=yM9Xbi-MigE)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle style (version 2.8.0)
- Not allowed to import any module
- All modules and functions must be documented
- All files must be executable

### Tasks

#### 0. Rotate 2D Matrix

- Given an n x n 2D matrix, rotate it 90 degrees clockwise.
- Prototype: `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- Assume the matrix will have 2 dimensions and will not be empty.

## Usage

```bash
./main_0.py

## Example Output

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```
## Repository Information

- **GitHub repository:** [alx-interview](https://github.com/i-christian/alx-interview)
- **Directory:** 0x07-rotate_2d_matrix
- **File:** 0-rotate_2d_matrix.py
