#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows the power up to a number

import math


def main():

    number = 0

    # process
    for number in range(1000, 2000 + 1):
        # output
        print("{0}".format(number), end=" ")
        if number % 5 == 0:
            print("")


if __name__ == "__main__":
    main()
