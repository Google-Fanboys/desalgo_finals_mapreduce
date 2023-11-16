import sys

def sort(input_file, output_file):

    file = open(input_file, 'r', encoding='utf-8')
    lines = file.readlines()

    key_value_pairs = [tuple(line.strip().split(' ', 1)) for line in lines]
    
    key_value_pairs = [(key, int(value)) for key, value in key_value_pairs]

    sorted_pairs = sorted(key_value_pairs, key=lambda x: x[1], reverse=True)

    # def value_of_pair(pair):
    #     return pair[1]
    # sorted_pairs = sorted(key_value_pairs, key=value_of_pair, reverse=True)

    file = open(output_file, 'w', encoding='utf-8')
    for pair in sorted_pairs:
        file.write(f"{pair[0]} {pair[1]}\n")


if __name__ == "__main__":

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    sort(input_file_path, output_file_path)