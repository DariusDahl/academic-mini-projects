# Einstein Solid Multiplicity Calculator (Stat Mech Mini Project)

This mini-project is a Python-based tool for analyzing the multiplicity and probabilities in coupled Einstein solids, created as part of statistical mechanics coursework.

## Overview

The script computes:

- Multiplicity: The number of microstates corresponding to a given macrostate for two coupled Einstein solids.
- Probability Distribution: The likelihood of each macrostate given the total energy of the system.

### What the Script Does

With user-provided inputs:
- The number of atoms in solid A.
- The number of atoms in solid B.
- The total energy.

The program:
1. Enumerates all ways of distributing the total energy between the two solids.
2. Computes:
   - Multiplicity for solid A.
   - Multiplicity for solid B.
   - Combined multiplicity.
   - Probability of each macrostate.
3. Builds a table with:
   - Energy distribution for each solid.
   - Multiplicities for each solid and the combined system.
   - Probability of each macrostate.
4. Summarizes:
   - The total number of microstates for the combined system.
   - Confirms that probabilities sum to 1 within numerical precision.

#### Example Usage:
Example run with 5 atoms in solid A, 8 atoms in solid B, and 10 energy:
```text
Enter the number of atoms for Einstein solid A: 5
Enter the number of atoms for Einstein solid B: 8
Enter the total energy: 10

Ω of A*B:
----------------------------------------------------------------------------------------------------------
| Energy of A | Energy of B | Multiplicity of A | Multiplicity of B | Multiplicity of A*B | Probability  |
----------------------------------------------------------------------------------------------------------
|     0       |     10       |       1          |  92561040         |   92561040          |    0.0141    |
|     1       |      9       |       15         |  28048800         |   420732000         |    0.0643    |
|     2       |      8       |      120         |   7888725         |   946647000         |    0.1447    |
| ...                                                                                                  |
----------------------------------------------------------------------------------------------------------
Total amount of microstates between Einstein solids A and B: 65404715896
```

## Computational Limitations

The multiplicity grows extremely quickly due to factorial operations, leading to constraints:
- Inputs of up to around 100 atoms compute quickly.
- Larger inputs may trigger integer overflow or take significant time to process.

## How to Run

From the `statmech-physics` folder:

```bash
python statmech.py
```

Follow the prompts for:
1. Number of atoms in Einstein solid A.
2. Number of atoms in Einstein solid B.
3. Total energy.

Results will be printed in a formatted table.

## Programming Skills Demonstrated

- Translating physics concepts into efficient Python code.
- Handling large factorial calculations.
- Structuring tabular console output.
- Using normalization for numerical consistency.

## Future Improvements

The project can be optimized by:
- Refactoring to use libraries like `numpy` for efficient computation.
- Allowing dynamic precision control to handle larger ranges.
- Adding visualizations (e.g., histograms for probability distributions).

---

This project highlights the combination of physics and computation, bridging theoretical concepts with practical implementation.
