#!/usr/bin/env python3

"""
Round 1B 2017: Problem A. Steed 2: Cruise Control
"""

import argparse


def main(distance, n, horses):
    max_time = 0.0
    for i in range(n):
        d = distance - horses[i][0]
        time = d / horses[i][1]
        max_time = max(max_time, time)
    return '{0:.6f}'.format(distance / max_time)


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to input file", required=True)
    args = parser.parse_args()
    with open(args.file) as fd:
        t = int(fd.readline())
        for i in range(1, t + 1):
            line = fd.readline().strip()
            # D and N: the destination position of all of the horses (in kilometers) and the number of other horses on the road.
            d, n = map(int, line.split())
            horses = []
            for j in range(n):
                line = fd.readline().strip()
                horses.append(tuple(map(int, line.split())))
            yield i, d, n, horses


if __name__ == '__main__':
    for i, d, n, horses in parse_input():
        r = main(d, n, horses)
        print("Case #{}: {}".format(i, r))
