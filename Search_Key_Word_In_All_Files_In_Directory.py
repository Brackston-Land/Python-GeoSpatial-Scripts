'''
The purpose of this script is to recursively iterate through all
files in a given path whose titles match a regex. Each line in the
file is matched against another regex.

Search strings are prompted through stdin and all matches are printed
to stdout.

Authors: Brackston Land, Blake Herrera
Created: 2023
'''

import os
import re


def __main__():
    
    # Prompt the user for search strings
    # An empty search path defaults to current working directory
    search_path = input("Enter directory path to search: ")
    file_pattern = re.compile(input("Enter file name regex: "))
    search_pattern = re.compile(input("Enter search regex: "))
    
    # Search for matching files and lines
    # Recursively walk through the file system
    for root, dirs, files in os.walk(search_path):
    
        # Iterate through only matching files
        for file in map(open, filter(file_pattern.match, files)):
    
            # Iterate through lines with number
            for line_num, line in enumerate(file):
    
                # Iterate through all matching instances and print them
                for m in search_pattern.finditer(line):
                    print(f'{os.path.join(root, file.name)}, line {line_num}, {m}')


# This prevents the code from running on import.
if __name__ == '__main__':
    __main__()
