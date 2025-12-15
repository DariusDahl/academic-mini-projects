# Bloom Filter False Positive Rate Analysis

This mini-project is a Python implementation of a Bloom filter, a probabilistic data structure used to test membership in a set, with a focus on analyzing its false positive rate.

## Overview

The script demonstrates how a Bloom filter works by:

- Inserting elements into the filter using multiple hash functions.
- Testing the filter's false positive rate by querying random elements that were not inserted.
- Exploring the effects of hash function design and Bloom filter size on the error rate.

## What the Script Does

1. Initializes a Bloom filter with:
   - A bit array of specified length.
   - A masking mechanism to limit hash indices.
   - A hashing function that generates multiple hash values for each element.

2. Inserts 200 random integers into the filter.

3. Tests the filter with 100,000 random integers to measure the false positive rate:
   - Tracks how often the filter incorrectly indicates membership for elements not inserted.

4. Calculates and outputs:
   - The count of false positives.
   - The false positive rate as a percentage.

### Example Output

```text
Number of false positives out of 100,000: 265
False positive rate: 6345 / 100,000 = 0.265%
```

## Key Concepts Demonstrated

- **Bloom Filters**: Probabilistic data structures for efficient membership checks, allowing false positives but no false negatives.
- **Hash Functions**: Custom hash functions that generate multiple indices for Bloom filter operations.
- **False Positives**: Measuring the rate at which the filter incorrectly identifies non-members as members.
- **Combinatorics**: Understanding how hash function design and element density impact false positive rates.

## How to Run

Ensure Python and NumPy are installed, then run the script:

```bash
python bloom_filter_false_positive_rate.py
```

The script:
1. Generates random integers for insertion and testing.
2. Outputs the false positive count and rate.

### Parameters
- **LENGTH**: The size of the Bloom filter array (default: 4096 bits).
- **MASK**: Limits hash indices to fit the Bloom filter size (default: 12 bits).
- **Hash Functions**: Two variants for generating multiple hash indices.

## Insights from the Project

Bloom filters balance performance and accuracy by trading off false positives for efficient storage and membership checks. This mini-project highlights:
- The impact of filter size and hash functions on error rates.
- Practical considerations for data structures in applications like databases and network caches.

---

This project showcases an introduction to probabilistic data structures and their real-world implications in computer science.
