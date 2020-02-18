# !/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import re
import fileinput


def cleanWord(aword):
    """
    Function input: A string which is meant to be
       interpreted as a single word.
    Output: a clean, lower-case version of the word
    """
    regex = r"[a-zA-Z0-9_]+"
    matches = bool(re.search(regex, aword, re.MULTILINE))
    if matches:
        return None
    return aword


def read_input():
    for line in fileinput.input():
        # split the line into words
        yield line.strip().split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input()
    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for c0_reducer1.py
        #
        word = cleanWord(line[0])
        if word is None:
            continue
        occurrences = int(line[2])

        print '%s%s%d' % (word, separator, occurrences)


if __name__ == "__main__":
    main()