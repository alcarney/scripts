#!/usr/bin/env python3
"""generate.py - A script for generating data."""
import argparse
import collections
import csv
import random


def generate(value, n, mu, stdev):
    samples = [int(value * random.normalvariate(mu, stdev)) for _ in range(n)]
    return collections.Counter(samples)


cli = argparse.ArgumentParser()
cli.add_argument("-v", "--value", type=int, default=100, help="the max value of the sampled groups")
cli.add_argument("-n", "--num-samples", type=int, default=10_000, help="how many samples to generate")
cli.add_argument("-m", "--mean", type=float, default=0.5, help="the mean value of the distribution")
cli.add_argument("--stdev", type=float, default=0.1, help="the standard deviation of the distribution")

cli.add_argument("-o", "--output", type=argparse.FileType('w'), default=None, help="the output file.")

if __name__ == '__main__':
    args = cli.parse_args()

    dist = generate(args.value, args.num_samples, args.mean, args.stdev)

    if args.output:
        writer = csv.writer(args.output)
        writer.writerow(["Group", "Count"])

        def write(i, v):
            writer.writerow([i, v])

    else:

        def write(i , v):
            print(i, v, sep="\t")

    for i in range(1, args.value + 1):
        v = dist.get(i, 0)
        write(i, v)
