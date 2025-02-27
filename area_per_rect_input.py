#!/usr/bin/env python3

# Created By: Joanna Keza
# Date: February 19, 2025
# This program calculates the area and perimeter with the user input.

def main():
    #input
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    #calculations
    area= length * width 
    perimeter= 2 * (length + width)
    #output
    print("area= {}cm^2" .format(area))
    print("perimeter= {}" .format(perimeter))

if __name__ == "__main__":
    main()