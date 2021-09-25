#!/usr/bin/env python3
import sys

def remove_duplicates(line_list):
    prev_line = None
    text = ''
    for i, line in enumerate(line_list):
        if line != prev_line:
             text += line + ','
             prev_line = line
    return text

def extract_translations(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file if line.strip() != '']
        line = lines[3::4]
        text = ''.join(remove_duplicates(line))

        prev_line = ''
        # for i, line in enumerate(lines):
        #     text += line


        # line_list = lines[::4]
        # text = remove_duplicates(line_list)
    print(text)

if __name__ == '__main__':
    extract_translations(sys.argv[1])
