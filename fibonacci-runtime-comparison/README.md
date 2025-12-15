# Fibonacci Algorithm Runtime Comparison

This mini-project provides a Python-based timing experiment to compare the execution time of two algorithms for computing Fibonacci numbers: recursive and iterative implementations.

## Overview

The experiment evaluates:
- **Recursive Fibonacci Algorithm**: A computationally expensive method using repeated function calls.
- **Iterative Fibonacci Algorithm**: An optimized method using pre-computed values.

The project highlights the stark differences in computational efficiency between the two approaches.

## What the Script Does

1. Computes Fibonacci numbers for values of \( n \) up to 30 using:
   - Recursive implementation.
   - Iterative (non-recursive) implementation.
   
2. Measures the runtime for each algorithm over 30 runs per value of \( n \).

3. Calculates:
   - Average runtime for each algorithm at each \( n \).
   - Confidence intervals for the average runtimes.

4. Outputs:
   - Runtime results table comparing both algorithms.
   - A graph showing the growth in runtime as \( n \) increases.

### Example Output
#### Text Results:
```
Recursive Fibonacci(30) = 832040, Average Time of 30 Runs: 0.0793192784 seconds
Non-recursive Fibonacci(30) = 832040, Average Time of 30 Runs: 0.0000000000 seconds

  Value | Recursive Fibonacci (sec) | Good Fibonacci (sec)
------- | ------------------------- | --------------------
      0 |    0.000000 ± 0.000000    | 0.000000 ± 0.000000
      1 |    0.000000 ± 0.000000    | 0.000000 ± 0.000000
      2 |    0.000000 ± 0.000000    | 0.000000 ± 0.000000
      ...
     28 |    0.029906 ± 0.000190    | 0.000000 ± 0.000000
     29 |    0.048424 ± 0.000291    | 0.000000 ± 0.000000
     30 |    0.079319 ± 0.000975    | 0.000000 ± 0.000000
```

#### Graph Results:
![image5](fibonacci-runtime-comparison/Sample_Output_Graph.png)

## Programming Skills Demonstrated

- **Performance Analysis**: Measuring runtimes and identifying computational bottlenecks.
- **Probability and Statistics**: Using confidence intervals to analyze runtime consistency.
- **Visualization**: Plotting runtime growth to highlight differences in algorithm efficiency.

## How to Run

Ensure Python and the required libraries (`scipy`, `matplotlib`) are installed, then:
```bash
python fibonacci_timing_experiment.py
```

The script:
1. Runs the recursive and iterative Fibonacci algorithms for values of \( n \) from 0 to 30.
2. Outputs statistics and a graph comparing their runtimes.

## Insights from the Project

This experiment demonstrates:
- The exponential computational cost of the recursive approach due to redundant calculations.
- The efficiency of iterative solutions in avoiding repetitive work.

---

This project serves as an introduction to algorithm analysis and highlights the importance of choosing appropriate data structures and approaches for computational efficiency.
