#!/usr/bin/env python3

"""
Problem A. Oversized Pancake Flipper
"""

import argparse


def main(pattern, k):
    """
    Returns number of flips
    """
    count = 0
    pancake_seq = list(pattern)
    while pancake_seq and len(pancake_seq) >= k:
        pancake_seq = remove_first_up_cakes(pancake_seq)
        if len(pancake_seq) >= k:
            count += 1
            _flip(pancake_seq, k)

    return count if not pancake_seq else "IMPOSSIBLE"


def remove_first_up_cakes(pancake_seq):
    i = 0
    while i < len(pancake_seq) and pancake_seq[i] == '+':
        i += 1
    return pancake_seq[i:]


def _flip(pancake_seq, k):
    for i in range(k):
        pancake_seq[i] = "+" if pancake_seq[i] == '-' else '-'


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to input file", required=True)
    args = parser.parse_args()
    with open(args.file) as fd:
        t = int(fd.readline())
        for i in range(1, t + 1):
            yield i, fd.readline().strip()


if __name__ == '__main__':
    for i, line in parse_input():
        pattern, m = line.split()
        m = int(m)
        if '-' not in pattern:
            print("Case #{}: {}".format(i, 0))
        else:
            r = main(pattern, m)
            print("Case #{}: {}".format(i, r))
