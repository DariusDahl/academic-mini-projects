# Suguru Backtracking Solver

This mini-project provides a Python implementation of a **Suguru puzzle solver** that uses recursive backtracking to solve puzzles with predefined configurations and constraints.

## Overview

Suguru is a logic-based number placement puzzle. The solver:
- Accepts a predefined puzzle configuration.
- Uses backtracking to assign numbers while adhering to the constraints.
- Ensures the solution satisfies all rules of Suguru puzzles.

## What the Script Does

1. Defines:
   - The puzzle dimensions (6x6 grid).
   - Block configurations that specify groupings of cells.
   - An initial puzzle matrix with some cells pre-filled.

2. Iteratively solves the puzzle using recursive backtracking:
   - Identifies the next empty cell.
   - Attempts to place numbers in the cell while validating constraints.
   - Reverts numbers if constraints are violated and continues searching.

3. Outputs:
   - The solved puzzle if a solution is found.
   - A "No solution found" message if the puzzle cannot be solved.

## Key Constraints and Validations

### Puzzle Rules
- Each block (group of cells) must contain unique integers from 1 to the size of the block.
- No two identical numbers may touch, even diagonally.

### Validations
- Verifies the rules for each block.
- Ensures that neighboring cells do not have repeating values.

### Example Input
#### Puzzle Configuration:
A 6x6 grid divided into blocks:
```
configuration = [
    {(0, 0), (1, 0), (0, 1), (2, 0)},
    ...
]
```

#### Initial Matrix:
Partially filled cells:
```
matrix = [
    [4, 0, 0, 0, 0, 0],
    ...
]
```

### Example Output
Running the solver yields:
```text
Solved Puzzle:
[4, 2, 1, 5, 1, 2]
[3, 5, 3, 2, 4, 5]
[1, 2, 4, 1, 3, 1]
[4, 3, 5, 2, 4, 2]
[5, 2, 1, 3, 5, 3]
[1, 3, 4, 2, 1, 4]
```

## Programming Skills Demonstrated

- **Recursive Backtracking**: Incrementally building solutions and backtracking when constraints are violated.
- **Logic & Validations**: Implementing validations to ensure puzzle rules are followed.
- **Matrix Manipulation**: Working with multi-dimensional arrays and positional indexing.

## How to Run

From the `suguru-backtracking-solver` folder:

```bash
python suguru_backtracking_solver.py
```

The script:
- Uses the predefined puzzle configuration (from PA3 instructions).
- Prints the solved puzzle or indicates no solution was found.

## Applications

Suguru puzzles are popular in recreational math and logic games. This solver demonstrates:
- Advanced problem-solving techniques.
- Efficient validation and constraint handling.

---

This project showcases recursive algorithms and logical constraints, bridging mathematical challenges with computational frameworks.
