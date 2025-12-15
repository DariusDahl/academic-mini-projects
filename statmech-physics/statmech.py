import math


def multiplicity(num_atoms, U):
    """
    Calculates the multiplicity of a macrostate given the number of atoms and the total energy.

    Args:
        num_atoms (int): The number of atoms in the system.
        U (int): The total energy of the system.

    Returns:
        int: The multiplicity of the macrostate.
    """
    N = num_atoms
    q = U
    if q == 0 or N == 0:
        return 1
    multiplicity = (math.factorial(q + 3 * N - 1) // (math.factorial(q) * math.factorial(3 * N - 1)))
    return multiplicity

while True:
    try:
        num_atoms_A = int(input("\nEnter the number of atoms for Einstein solid A: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        num_atoms_B = int(input("Enter the number of atoms for Einstein solid B: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        U = int(input("Enter the total energy: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print()


# Create a list to store the results of the calculation
results = []

# Calculate the multiplicities for each energy level
for i_A in range(U + 1):
    for i_B in range(U, -1, -1):
        # Calculate the multiplicity of A
        multiplicity_A = multiplicity(num_atoms_A, i_A)

        # Calculate the multiplicity of B
        multiplicity_B = multiplicity(num_atoms_B, i_B)

        # Calculate the multiplicity of A*B
        multiplicity_AB = multiplicity_A * multiplicity_B

        # Add the results to the list
        results.append([i_A, i_B, multiplicity_A, multiplicity_B, multiplicity_AB])

# Filter the results to only include energy distributions that add up to the total input energy
filtered_results = []
for result in results:
    if result[0] + result[1] == U:
        filtered_results.append(result)

# Initialize the total variable
total = 0

# Calculate the total amount of microstates
for result in filtered_results:
    total += result[4]

# Print the table
print("\u03A9 of A*B:")
print("-" * 106)
print("| Energy of A | Energy of B | Multiplicity of A | Multiplicity of B | Multiplicity of A*B | Probability  |")
print("-" * 106)
for result in filtered_results:
    probability = result[4] / total

    # Use the `str.format()` method to format the multiplicities in scientific notation if they are larger than 10 digits
    multiplicity_A_string = "{:.4E}".format(result[2]) if result[2] > 10**10 else str(result[2])
    multiplicity_B_string = "{:.4E}".format(result[3]) if result[3] > 10**10 else str(result[3])
    multiplicity_AB_string = "{:.4E}".format(result[4]) if result[4] > 10**10 else str(result[4])

    print(f"| {result[0]:7}     | {result[1]:7}     | {multiplicity_A_string:12}      | {multiplicity_B_string:12}      | {multiplicity_AB_string:12}        | {probability:12.10f} |")
print("-" * 106)

# Print the total amount of microstates
total_string = "{:.4E}".format(total) if total > 10**10 else str(total)

if len(total_string) == 1:
    space = "          "
elif len(total_string) == 2:
    space = "          "
elif len(total_string) == 3:
    space = "          "
elif len(total_string) == 4:
    space = "          "
elif len(total_string) == 5:
    space = "      "
elif len(total_string) == 6:
    space = "      "
elif len(total_string) == 7:
    space = "      "
elif len(total_string) == 8:
    space = "      "
elif len(total_string) == 9:
    space = "  "
elif len(total_string) == 10:
    space = "  "
elif len(total_string) == 11:
    space = "  "
else:
    space = "  "

print(f"\t\t\t\t\t\t\t\t\t\t\t     Total: \t\t     ", total_string, "\t\t", space,"1.0000000000\n")
print(f"Total amount of microstates between Einstein solids A and B: {total}")