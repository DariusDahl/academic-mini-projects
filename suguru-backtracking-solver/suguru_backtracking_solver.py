# Puzzle dimensions, as given from PA3 instructions
di = 6
dj = 6

# The initial puzzle configuration from PA3 instructions
configuration = [
    {(0, 0), (1, 0), (0, 1), (2, 0)},
    {(2, 1), (3, 1), (3, 0), (4, 0), (5, 0)},
    {(0, 2), (1, 1), (1, 2), (1, 3), (2, 2)},
    {(4, 1), (4, 2)},
    {(5, 1), (5, 2), (5, 3), (4, 4), (5, 4)},
    {(3, 2), (2, 3), (3, 3), (4, 3), (3, 4)},
    {(0, 3), (0, 4), (0, 5), (1, 4), (2, 4)},
    {(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)}
]

# Starting matrix, again from PA3 instructions
matrix = [[0 for j in range(dj)] for i in range(di)]
matrix[0][0] = 4
matrix[4][0] = 5
matrix[2][2] = 4
matrix[3][3] = 2
matrix[4][3] = 3
matrix[4][4] = 5
matrix[2][5] = 1


# Function to find the first empty spot in the array
# Returns the coordinates of the first cell that still contains a zero.
def find_empty(matrix):
    for i in range(di):
        for j in range(dj):
            if matrix[i][j] == 0:
                return (i, j)
    return None


# Check if the current placement is valid
# Checks that:
# (a) no two non-zero repeating integers are next to each other, even diagonally
# (b) each area contains only numbers larger than 0 once and not larger than
# the number of cells in the area.
def valid_so_far(matrix, i, j, num):
    # Check the block
    for block in configuration:
        if (i, j) in block:
            # Check that the number doesn't already exist in the block (no repetition)
            if any(matrix[x][y] == num for (x, y) in block):
                return False
    # Define all possible neighboring positions:
    # Four adjacent (up, down, left, right) and four diagonal (top-left, top-right, bottom-left, bottom-right).
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1),
                 (i + 1, j + 1)]
    # Loop through all neighboring cells and check for valid indices.
    # If the neighbor exists within the matrix and contains the same number, return False.
    for (ni, nj) in neighbors:
        # Check for in bounds and if repeating number exists
        if 0 <= ni < di and 0 <= nj < dj and matrix[ni][nj] == num:
            return False
    # Return True if valid
    return True


# Check if the puzzle is solved
def done(matrix):
    # True if all indices in the matrix are not equal to zero
    return all(matrix[i][j] != 0 for i in range(di) for j in range(dj))


# Recursive backtracking function
def backtrack(matrix):
    # First check if puzzle is solved
    if done(matrix):
        return matrix
    empty = find_empty(matrix)
    if not empty:
        return None
    i, j = empty
    # Try all possible numbers for this block
    for block in configuration:
        if (i, j) in block:
            for num in range(1, len(block) + 1):
                if valid_so_far(matrix, i, j, num):
                    matrix[i][j] = num
                    result = backtrack(matrix)
                    if result:
                        return result
                    matrix[i][j] = 0  # Undo move (backtrack)
    return None


# Function to print the puzzle
def print_it(matrix):
    for row in matrix:
        print(row)


# Main function to run the puzzle solver
def main():
    solution = backtrack(matrix)
    if solution:
        print("Solved Puzzle:")
        print_it(solution)
    else:
        print("No solution found.")


# Run the main function
if __name__ == "__main__":
    main()