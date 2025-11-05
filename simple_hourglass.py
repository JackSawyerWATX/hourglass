def hourglass_sum(arr):
    """Find the maximum hourglass sum in a 6x6 array"""
    max_sum = float('-inf')
    
    # Check all possible hourglass positions
    for i in range(4):
        for j in range(4):
            # Calculate hourglass sum at position (i,j)
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +      # Top row
                arr[i+1][j+1] +                               # Middle
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
            )
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test with sample data
sample = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

# Print the sample array
print("Sample 6x6 array:")
for row in sample:
    print(row)

# Find and show the maximum hourglass
max_sum = float('-inf')
best_i, best_j = 0, 0

for i in range(4):
    for j in range(4):
        current_sum = (
            sample[i][j] + sample[i][j+1] + sample[i][j+2] +
            sample[i+1][j+1] +
            sample[i+2][j] + sample[i+2][j+1] + sample[i+2][j+2]
        )
        if current_sum > max_sum:
            max_sum = current_sum
            best_i, best_j = i, j

print(f"\nMaximum hourglass sum: {max_sum}")
print(f"Found at position ({best_i}, {best_j})")

# Show what the hourglass looks like
print("\nHourglass pattern:")
print("X X X")
print("  X  ")
print("X X X")

print(f"\nThe winning hourglass at position ({best_i}, {best_j}):")
print(f"{sample[best_i][best_j]} {sample[best_i][best_j+1]} {sample[best_i][best_j+2]}")
print(f"  {sample[best_i+1][best_j+1]}  ")
print(f"{sample[best_i+2][best_j]} {sample[best_i+2][best_j+1]} {sample[best_i+2][best_j+2]}")

print(f"\nCalculation: {sample[best_i][best_j]} + {sample[best_i][best_j+1]} + {sample[best_i][best_j+2]} + {sample[best_i+1][best_j+1]} + {sample[best_i+2][best_j]} + {sample[best_i+2][best_j+1]} + {sample[best_i+2][best_j+2]} = {max_sum}")