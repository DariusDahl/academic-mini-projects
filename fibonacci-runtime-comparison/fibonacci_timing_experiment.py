import time
import statistics
from scipy.stats import t
import matplotlib.pyplot as plt


def recursive_fibonacci(n):
    if n < 2:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def non_recursive_fibonacci(n):
    if n < 2:
        return n
    cur, pre = 1, 0
    for _ in range(2, n + 1):
        cur, pre = cur + pre, cur
    return cur


def calculate_confidence_interval(data, confidence=0.95):
    if not data:
        return 0, 0
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    n = len(data)
    t_critical = t.ppf((1 + confidence) / 2, n - 1)
    margin_of_error = t_critical * (std_dev / (n ** 0.5))
    return mean, margin_of_error


n_max = 30
num_runs = 30

results = []
for i in range(n_max + 1):
    recursive_data = []
    non_recursive_data = []

    for _ in range(num_runs):
        start_time_fib = time.time()
        result_recursive = recursive_fibonacci(i)
        end_time_fib = time.time()
        recursive_data.append(end_time_fib - start_time_fib)

        start_time_non_fib = time.time()
        result_non_recursive = non_recursive_fibonacci(i)
        end_time_non_fib = time.time()
        non_recursive_data.append(end_time_non_fib - start_time_non_fib)

    mean_recursive, moe_recursive = calculate_confidence_interval(
        recursive_data)
    mean_non_recursive, moe_non_recursive = calculate_confidence_interval(
        non_recursive_data)

    results.append((i, mean_recursive, moe_recursive,
                   mean_non_recursive, moe_non_recursive))

average_recursive_time = sum(recursive_data) / num_runs
average_non_recursive_time = sum(non_recursive_data) / num_runs

print(
    f"Recursive Fibonacci({n_max}) = {result_recursive}, "
    f"Average Time of 30 Runs: {average_recursive_time:.10f} seconds"
)
print(
    f"Non-recursive Fibonacci({n_max}) = {result_non_recursive}, "
    f"Average Time of 30 Runs: {average_non_recursive_time:.10f} seconds"
)
print("  Value | Recursive Fibonacci (sec) | Good Fibonacci (sec)")
print("------- | ------------------------- | --------------------")
for value, mean_rec, moe_rec, mean_non_rec, moe_non_rec in results:
    print(f"{value:7} |    {mean_rec:.6f} ± {moe_rec:.6f}    | {mean_non_rec:.6f} ± {moe_non_rec:.6f}")

# Extract data from results
value, mean_rec, moe_rec, mean_non_rec, moe_non_rec = zip(*results)

# Plotting
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.errorbar(value, mean_rec, yerr=moe_rec,
             fmt='-o', label='Recursive Fibonacci')
plt.errorbar(value, mean_non_rec, yerr=moe_non_rec,
             fmt='-o', label='Non-recursive Fibonacci')

# Add labels, title, and legend
plt.xlabel('Value (n)')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Recursive and Non-Recursive Fibonacci Computation Times')
plt.legend()

# Display the plot
plt.show()
