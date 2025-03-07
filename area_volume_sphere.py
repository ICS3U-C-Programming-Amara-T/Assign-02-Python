#!/usr/bin/env python3

# Created By: Amara Tie

# Date: Month March 4, 2025

# Calculating the surface area and volume of a sphere.
import math
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def main():
    # Get Radius
    radius = float(input("Enter the radius of the sphere : "))
    units = input("Enter Units: ")

    # Calculate the surface area and volume
    surface_area = 4 * math.pi * radius**2
    volume = 4 / 3 * math.pi * radius**3

    # Color your text Source:https://www.youtube.com/watch?v=u51Zjlnui4Y
    print("\nChoose a color")
    print("1. magenta")
    print("2. blue")
    print("3. yellow")
    print("4. red")
    color_choice = input("Enter the # (1-5)")

    # Color choices to Fore Colors
    if color_choice == "1":
        color = Fore.MAGENTA
    if color_choice == "2":
        color = Fore.BLUE
    if color_choice == "3":
        color = Fore.YELLOW
    if color_choice == "4":
        color = Fore.RED

    # Display the volume, surface area and color
    print("")
    print(f"Color: {color}")
    print(f"Volume: {color} {volume:.2f}^3".format(volume, units))
    print(f"Surface Area: {color}{surface_area:.2f}^2".format(surface_area, units))


if __name__ == "__main__":
    main()
