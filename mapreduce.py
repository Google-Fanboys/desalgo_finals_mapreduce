"""Script that implements the MapReduce algorithm."""
import sys # for sys.argv, the command-line arguments
import string # for string.punctuation

def clean_word(word: str) -> str:
    """Returns a cleaned-up version of the word."""
    return word.strip(string.punctuation).lower()

def mapper(line: str) -> list[tuple[str, int]]:
    """Returns a list of (key, value) pairs for each word in the line."""
    words = line.split()
    return [(clean_word(word), 1) for word in words]

def reducer(key: str, counts: list[int]) -> tuple[str, int]:
    """Returns a (key, value) pair where the value is the sum of the counts."""
    return key, sum(counts)

def sort(result: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Sorts the result by key in descending order."""
    return sorted(result, key=lambda x: x[0])

def main() -> None:
    """Main program."""

    # Check command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python mapreduce.py <input_file> <output_file>")
        sys.exit(1)

    # Get input and output file names
    input_file = sys.argv[1:-1]
    output_file = sys.argv[-1]

    # Read input files and map each word to a list of (key, value) pairs
    mapped_words = []
    for filename in input_file:
        with open(filename, 'r', encoding="utf-8") as file:
            words = file.read().splitlines()
            for word in words:
                mapped_words.extend(mapper(word))

    # Sort the (key, value) pairs by key
    sorted_words = sort(mapped_words)

    # Group the (key, value) pairs by key
    reduced_words = {}
    for key, value in sorted_words:
        reduced_words.setdefault(key, []).append(value)

    # Reduce the (key, value) pairs
    result = [reducer(key, values) for key, values in reduced_words.items()]

    # Write the result to the output file
    with open(output_file, 'w', encoding="utf-8") as file:
        for key, value in result:
            file.write(f"{key}, {value}\n")

# Call main() if the program is run from the command line
if __name__ == "__main__":
    main()
