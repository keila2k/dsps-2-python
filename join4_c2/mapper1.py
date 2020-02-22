# coding=utf-8
# !/usr/bin/env python
import re
import sys


def cleanWord(aword):
    regex = r"[a-zA-Z0-9_]+"
    matches = bool(re.search(regex, aword, re.MULTILINE))
    if matches:
        return None
    return aword


def read_input(__file__, separator='\t'):
    for line in __file__:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_input(sys.stdin, separator=separator)
    for line in data:
        key, value = line
        splits = key.split(" ")
        if len(splits) == 2:
            print "%s %s ['%s',%s]" % (key, separator, ' ', value)
        else:
            print "%s %s %s ['%s',%s]" % (splits[0], splits[1], separator, key.rstrip(), value)


if __name__ == "__main__":
    main()
