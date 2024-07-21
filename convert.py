#!/usr/bin/env python3
import argparse


def read_dictionary(dictionary_file):
    dictionary = {}
    with open(dictionary_file, "r") as file:
        for line in file:
            number, word = line.strip().split()
            dictionary[number] = word
    return dictionary


def read_numbers(numbers_file):
    with open(numbers_file, "r") as file:
        numbers = [line.strip() for line in file]
    return numbers


def write_wordlist(wordlist):
    with open("wordlist", "w") as file:
        for word in wordlist:
            file.write(word + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Convert numbers to words using a dictionary."
    )
    parser.add_argument(
        "numbers_file", type=str, help="File containing list of numbers."
    )
    parser.add_argument(
        "dictionary_file", type=str, help="File containing dictionary mappings."
    )
    args = parser.parse_args()

    dictionary = read_dictionary(args.dictionary_file)
    numbers = read_numbers(args.numbers_file)

    wordlist = [dictionary[number] for number in numbers if number in dictionary]

    write_wordlist(wordlist)


if __name__ == "__main__":
    main()
    print("Numbers converted. See 'words' file.")
