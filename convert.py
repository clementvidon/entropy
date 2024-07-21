#!/usr/bin/env python3
import argparse
import sys

def read_dictionary(dictionary_file):
    dictionary = {}
    with open(dictionary_file, "r") as file:
        for line in file:
            number, word = line.strip().split()
            dictionary[number] = word
    return dictionary

def read_numbers():
    numbers = [line.strip() for line in sys.stdin]
    return numbers

def main():
    parser = argparse.ArgumentParser(
        description="Convert numbers to words using a dictionary."
    )
    parser.add_argument(
        "dictionary_file", type=str, help="File containing dictionary mappings."
    )
    args = parser.parse_args()

    dictionary = read_dictionary(args.dictionary_file)
    numbers = read_numbers()

    wordlist = [dictionary[number] for number in numbers if number in dictionary]
    for word in wordlist:
        print(word)

if __name__ == "__main__":
    main()
