# !/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys


def read_input(__file__):
    for line in __file__:
        # split the line into words
        yield line.strip().split()


def main():
    count = 0
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for c0_reducer1.py
        #
        if line is None:
            continue
        count = count + 1
    print count


if __name__ == "__main__":
    main()
