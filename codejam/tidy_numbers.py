#!/usr/bin/env python3

"""
Problem B. Tidy Numbers

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest,
her pencils are sorted from shortest to longest and her computers from oldest
to newest. One day, when practicing her counting skills, she noticed that some
integers, when written in base 10 with no leading zeroes, have their digits
sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488.
She decided to call these numbers tidy. Numbers that do not have this property,
like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N.
What was the last tidy number she counted?
"""

import argparse


def issorted(n):
    next_digit = n % 10
    n = n // 10
    while n:
        digit = n % 10
        if digit > next_digit:
            return False
        next_digit = digit
        n = n // 10
    return True


def main(i, m):
    if ''.join(sorted(m)) == m:
        print("Case #{}: {}".format(i, m))
    else:
        num = int(m)
        tmp = num
        p = 1
        while num:
            last_digit = (tmp % 10 + 1) * p
            num -= last_digit
            p *= 10
            tmp = num // p

            if issorted(num):
                print("Case #{}: {}".format(i, num))
                break


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
        main(i, line)
