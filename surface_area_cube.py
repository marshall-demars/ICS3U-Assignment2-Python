#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program calculates surface area of a cube
#    with user input

import math


def main():
    # this function calculates surface area of a cube

    # input
    length_of_square = float(input("Enter length of the square (cm): "))
    width_of_square = float(input("Enter width of the square (cm): "))

    # process
    area_of_square = length_of_square * width_of_square
    surface_area_of_cube = 6 * area_of_square

    # output
    print("\nSurface area is {0} cm².".format(surface_area_of_cube))

    print("\nDone.")


if __name__ == "__main__":
    main()
