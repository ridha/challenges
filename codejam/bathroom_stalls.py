#!/usr/bin/env python3

"""
Problem C. Bathroom Stalls
"""

import argparse
from heapq import heappush, heappop


def main(n, k):
    if n == k:
        return [0, 0]

    heap = [-n]
    for _ in range(k):
        max_item = -heappop(heap)
        max_item = max_item - 1
        i = max_item // 2
        j = max_item - i
        heappush(heap, -i)
        heappush(heap, -j)
    return sorted([i, j], reverse=True)


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
        n, k = map(int, line.split())
        r = main(n, k)
        print("Case #{}: {} {}".format(i, *r))
