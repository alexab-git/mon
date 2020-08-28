#!/usr/bin/env python3
from random import randint

def main():
    rand_bot = 0
    rand_top = 100
    mcount = 3

    for x in range(1, mcount + 1):
        print("otus_important_metrics[metric%d]=%d" % (x, randint(rand_bot,rand_top)))

if __name__ == '__main__':
    main()
