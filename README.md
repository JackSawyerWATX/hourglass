# Hourglass Array Sum Problem

1. **Clear Problem Explanation**
   - What an hourglass is visually
   - Why it's called an hourglass

2. **Real-World Context**
   - Image processing applications
   - Game development uses
   - Data analysis scenarios
   - Programming skills developed

3. **Complete Running Instructions**
   - Prerequisites needed
   - Step-by-step terminal commands
   - How to run both versions
   - How to enter custom data

4. **Technical Details**
   - Time and space complexity
   - Algorithm explanation
   - Example walkthrough
    
5. **Learning Aids**
   - Memory techniques
   - Visual analogies
   - Key insights

## Quick Reference - How to Run:
Simple version (runs immediately):

```
python simple_hourglass.py
```

Full version (with input options):

```
python hourglass.py
```

## What is This?

This program solves the "Hourglass Sum" problem - finding the maximum sum among all possible hourglass 
patterns in a 6×6 array.

## What Does an Hourglass Look Like?

An hourglass is a specific pattern that looks like this:
```
X X X
  X  
X X X
```

It's called an "hourglass" because it resembles the shape of an hourglass ⏳ - wide at the top, 
narrow in the middle, wide at the bottom.

## Why Does This Problem Matter?

### Real-World Applications

**Image Processing & Computer Vision:**
- Detecting specific patterns in photos (crosswalks, text, objects)
- Finding shapes and features in medical imaging
- Pattern recognition in security systems

**Game Development:**
- Checking for winning patterns in board games
- Detecting tile arrangements in puzzle games
- Finding optimal moves in strategy games

**Data Analysis:**
- Looking for trends and peaks in spreadsheet data
- Identifying clusters in survey data
- Detecting anomalies in sensor readings

### Programming Skills Developed
- **Pattern Recognition**: Identifying geometric shapes in data
- **2D Array Navigation**: Systematic traversal of matrices
- **Boundary Checking**: Ensuring you don't exceed array limits
- **Optimization**: Finding the best solution among many options
- **Nested Loop Logic**: Understanding complex iteration patterns

## How It Works

1. **Scan all positions**: Check every possible 3×3 location in the 6×6 grid
2. **Calculate hourglass sum**: For each position, add up the 7 elements that form the hourglass
3. **Track maximum**: Keep the highest sum found
4. **Return result**: The maximum hourglass sum in the entire array

### Example
In this array:
```
[1, 1, 1, 0, 0, 0]
[0, 1, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0]
[0, 0, 2, 4, 4, 0]
[0, 0, 0, 2, 0, 0]
[0, 0, 1, 2, 4, 0]
```

The winning hourglass is:
```
2 4 4
  2
1 2 4
```
Sum: 2 + 4 + 4 + 2 + 1 + 2 + 4 = **19**

## Files in This Project

- `hourglass.py` - Full version with user input and testing options
- `simple_hourglass.py` - Minimal version that runs immediately with sample data
- `README.md` - This documentation file

## How to Run

### Prerequisites
- Python 3.x installed on your system
- Command line access (PowerShell, Command Prompt, or Terminal)

### Running the Simple Version
1. Open your terminal/command prompt
2. Navigate to the project directory:
   ```bash
   cd "C:\Users\compname\OneDrive\Desktop\hourglass"
   ```
3. Run the simple version:
   ```bash
   python simple_hourglass.py
   ```

This will immediately show:
- The sample 6×6 array
- The maximum hourglass sum
- Which hourglass pattern produced the maximum
- The actual calculation breakdown

### Running the Full Version
1. Navigate to the project directory (same as above)
2. Run the full version:
   ```bash
   python hourglass.py
   ```
3. Choose your option:
   - Type `y` for sample data (quick test)
   - Type `n` to enter your own 6×6 array

### Entering Your Own Data
If you choose to enter custom data, provide:
- 6 rows of input
- Each row contains 6 integers separated by spaces
- Example input:
  ```
  1 1 1 0 0 0
  0 1 0 0 0 0
  1 1 1 0 0 0
  0 0 2 4 4 0
  0 0 0 2 0 0
  0 0 1 2 4 0
  ```

## Understanding the Algorithm

### Time Complexity: O(1)
- Always checks exactly 16 hourglasses (4×4 possible positions)
- Constant time regardless of input values

### Space Complexity: O(1)
- Uses only a few variables to track the maximum
- No additional data structures needed

### Key Insight
You're not just manipulating arrays - you're learning to systematically search for optimal patterns in 
structured data. This skill applies to analyzing business data, processing images, building games, and 
many other real-world programming tasks.

## Memory Techniques

**Visual Memory:**
- Think of scanning a photo with a special lens that only sees hourglass shapes
- Imagine you're a detective looking for a specific clue pattern

**Pattern Memory:**
- Remember the shape: ⏳
- Top shelf: 3 items, Narrow middle: 1 item, Bottom shelf: 3 items

**Practical Memory:**
- "I'm finding the richest treasure location among all possible spots"
- "I'm checking every 3×3 area for the best score"

### I love you all and Happy Coding!!