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
        key, values = line
        regex = r"\['.*?'.*?\]"
        values = re.findall(regex, values)
        try:
            values = map(eval, values)
            w2w3_key_index = -1
            for idx, item in enumerate(values):
                if item[0] is ' ':
                    w2w3_key_index = idx
                    break
            w2w3_key, w2w3_value = values.pop(w2w3_key_index)
            for key, value1, value2, value3, value4 in values:
                print "%s%s%s,%s,%s,%s,%s" % (key, separator, value1, value2, value3, value4, w2w3_value)
        except Exception:
            pass


if __name__ == "__main__":
    main()
