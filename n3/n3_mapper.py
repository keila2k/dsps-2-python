# coding=utf-8
# !/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import re
import sys


def win32_unicode_argv():
    """Uses shell32.GetCommandLineArgvW to get sys.argv as a list of Unicode
    strings.

    Versions 2.x of Python don't support Unicode in sys.argv on
    Windows, with the underlying Windows API instead replacing multi-byte
    characters with '?'.
    """

    from ctypes import POINTER, byref, cdll, c_int, windll
    from ctypes.wintypes import LPCWSTR, LPWSTR

    GetCommandLineW = cdll.kernel32.GetCommandLineW
    GetCommandLineW.argtypes = []
    GetCommandLineW.restype = LPCWSTR

    CommandLineToArgvW = windll.shell32.CommandLineToArgvW
    CommandLineToArgvW.argtypes = [LPCWSTR, POINTER(c_int)]
    CommandLineToArgvW.restype = POINTER(LPWSTR)

    cmd = GetCommandLineW()
    argc = c_int(0)
    argv = CommandLineToArgvW(cmd, byref(argc))
    if argc.value > 0:
        # Remove Python executable and commands if present
        start = argc.value - len(sys.argv)
        return [argv[i] for i in
                xrange(start, argc.value)]


# sys.argv = win32_unicode_argv()


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
    selectedWord1 = sys.argv[1]
    selectedWord2 = sys.argv[2]
    selectedWord3 = sys.argv[3]
    data = read_input(sys.stdin)
    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for c0_reducer1.py
        #
        word1 = cleanWord(line[1])
        word2 = cleanWord(line[2])
        word3 = cleanWord(line[3])
        if (word1 and word1 == selectedWord1) and (word2 and word2 == selectedWord2) and (
                word3 and word3 == selectedWord3):
            occurrences = int(line[5])
            print '%s %s %s %s %d' % (word1, word2, word3, separator, occurrences)
        else:
            continue


if __name__ == "__main__":
    main()