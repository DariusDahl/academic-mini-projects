import numpy as np
import random

LENGTH = 4096  # Length of the Bloom filter array
MASK = 0xfff  # Mask to limit indices to the Bloom filter array size (12 bits)


# Hash function to generate five hash values
def hasher(ix):
    return ((17377*ix**2) & MASK,
            (17377*(ix+31)**2) & MASK,
            (10607*(ix+39)) & MASK,
            (1297*ix**2>>4) & MASK,
            (10607*(ix+41)**2) & MASK)


# Alternative hash function with different parameters for five hash values
def hasher2(ix):
    return (
        (17377 * ix**2 >> 4) & MASK,
        ((17377 * (ix + 5)**2) >> 8) & MASK,
        ((10607 * (ix + 7)**2) >> 2) & MASK,
        ((1297 * (ix + 11)**2) >> 6) & MASK,
        ((311 * (ix + 13)**2) >> 3) & MASK,
    )


# Bloom filter class with insert and look-up functionality
class Bloom:
    def __init__(self, LENGTH, MASK, hasher):
        self.length = LENGTH  # Bloom filter array length
        self.mask = MASK  # Mask for limiting hash values
        self.array = np.zeros(LENGTH, dtype=bool)  # Initialize bit array with False (0)
        self.hasher = hasher  # Use the provided hashing function

    # Insert an element into the Bloom filter
    def insert(self, x):
        # Get hash indices and set corresponding bits to True
        for h in self.hasher(x):  # Compute hash indices
            self.array[h] = True  # Set corresponding bits to True

    # Check if an element might be in the Bloom filter
    def look_up(self, x):
        # Check if all bits at the hash indices are True
        return all(self.array[h] for h in self.hasher(x))  # Return True only if all bits are True


# Main function to test the Bloom filter
def main():
    # Create a Bloom filter instance with the updated parameters
    my_bloom = Bloom(LENGTH, MASK, hasher2)

    # Insert 200 random integers into the Bloom filter
    for i in random.sample(range(10000), 200):
        my_bloom.insert(i)

    # Generate 100,000 random integers and check for false positives
    false_positive_count = 0  # Track false positives
    for i in range(100000):
        x = random.randint(10000, 10000000)  # Random test integer
        if my_bloom.look_up(x):  # Check if the integer is falsely identified as present
            false_positive_count += 1  # Increment false positive count

    # Calculate the false positive rate
    false_positive_rate = false_positive_count / 100000

    # Output results
    print(f"Number of false positives out of 100,000: {false_positive_count}")
    print(f"False positive rate: {false_positive_count} / 100,000 = {false_positive_rate:.3%}")


if __name__ == "__main__":
    main()
