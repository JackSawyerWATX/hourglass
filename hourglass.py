#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Initialize with the first possible hourglass sum
    max_sum = float('-inf')  # Start with negative infinity to handle negative numbers
    
    # We can only form hourglasses starting from position (0,0) to (3,3)
    # because we need 3x3 space and the array is 6x6
    for i in range(4):  # rows 0 to 3 (4 possible starting rows)
        for j in range(4):  # cols 0 to 3 (4 possible starting columns)
            # Calculate the hourglass sum at position (i,j)
            # Top row: arr[i][j] + arr[i][j+1] + arr[i][j+2]
            # Middle: arr[i+1][j+1]
            # Bottom row: arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
                arr[i+1][j+1] +                           # Middle element
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
            )
            
            # Keep track of the maximum sum found so far
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def test_with_sample():
    # Sample test case
    sample_arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    
    print("Sample array:")
    for row in sample_arr:
        print(" ".join(f"{x:2}" for x in row))
    
    result = hourglassSum(sample_arr)
    print(f"\nMaximum hourglass sum: {result}")
    print("(Expected: 19)")

if __name__ == '__main__':
    choice = input("Test with sample data? (y/n): ").lower()
    
    if choice == 'y':
        test_with_sample()
    else:
        print("Enter 6 rows of 6 integers each:")
        arr = []

        for i in range(6):
            print(f"Row {i+1}: ", end="")
            arr.append(list(map(int, input().rstrip().split())))

        result = hourglassSum(arr)

        print(f"\nMaximum hourglass sum: {result}")
        
        # Optional: Save to file if you want
        # with open("output.txt", "w") as f:
        #     f.write(str(result) + "\n")
