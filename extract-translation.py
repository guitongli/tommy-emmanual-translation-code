#!/usr/bin/env python3
import sys


def remove_duplicates(line_list):
    prev_line = None
    unique_lines = []
    for i, line in enumerate(line_list):
        if line != prev_line:
            unique_lines.append(line)
        prev_line = line
    return unique_lines


def extract_translations(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file if line.strip() != '']
    text = '，'.join(remove_duplicates(lines[3::4]))
    print(text)


if __name__ == '__main__':
    extract_translations(sys.argv[1])
