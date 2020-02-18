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
    regex = r"[a-zA-Z]+"
    matches = re.match(regex, aword, re.MULTILINE)
    if matches:
        return None
    return aword


def read_input():
    for line in fileinput.input():
        # split the line into words
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input()
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            aword = cleanWord(word)
            if aword is None:
                continue
            else:
                print '%s%s%d' % (aword, separator, 1)


if __name__ == "__main__":
    main()
