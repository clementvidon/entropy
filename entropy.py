#!/usr/bin/env python3
import math

def calculate_entropy(length, symbols):
    entropy = length * math.log2(symbols)
    return entropy

def main():
    print("Password Entropy Calculator")
    print("===========================")
    length = int(input("Enter the length of the password: "))
    symbols = int(input("Enter the number of possible symbols: "))

    entropy = calculate_entropy(length, symbols)

    print(f"\nThe entropy of the password is: {entropy:.2f} bits")

if __name__ == "__main__":
    main()
