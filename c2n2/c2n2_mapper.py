# coding=utf-8
# !/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import re
import sys


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


def read_input(__file__):
    for line in __file__:
        # split the line into words
        yield line.strip().split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for line in data:
        if len(line) < 5:
            continue
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for c0_reducer1.py
        #
        word1 = cleanWord(line[1])
        word2 = cleanWord(line[2])
        if word1 is None or word2 is None:
            continue
        occurrences = int(line[4])
        print '%s %s %s %d' % (word1, word2, separator, occurrences)


if __name__ == "__main__":
    main()
