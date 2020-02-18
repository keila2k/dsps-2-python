#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""
import fileinput
from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(separator='\t'):
    for line in fileinput.input():
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            # total_count = sum(int(count) for current_word, count in group)
            print "%s%s%d" % (current_word, separator, 1)
        except ValueError:
            # count was not a number, so silently discard this item
            pass


if __name__ == "__main__":
    main()
