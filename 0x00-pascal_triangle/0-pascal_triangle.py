#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        current_row = [1]  # Start the current row with 1
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)  # End the current row with 1
        triangle.append(current_row)

    return triangle
