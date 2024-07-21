#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Function to read numbers from file
def read_numbers_from_file(filename):
    with open(filename, "r") as file:
        numbers = [int(num) for num in file.read().split()]
    return np.array(numbers)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Measure the richness of the dataset.")
    parser.add_argument("filename", type=str, help="The input file containing numbers")
    args = parser.parse_args()

    # Read numbers from file
    numbers_array = read_numbers_from_file(args.filename)

    # Compute statistical measures
    mean = np.mean(numbers_array)
    std_dev = np.std(numbers_array)
    hist, bins = np.histogram(numbers_array, bins=10, density=True)

    # Print statistical measures
    print("Mean:", mean)
    print("Standard Deviation:", std_dev)
    print("See: histogram.png")

    # Plot histogram
    plt.hist(numbers_array, bins=10, alpha=0.7, color="b", edgecolor="black")
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.title("Histogram of Generated Numbers")
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig("histogram.png")

if __name__ == "__main__":
    main()
