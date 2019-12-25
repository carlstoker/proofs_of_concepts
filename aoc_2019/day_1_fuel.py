#!/usr/bin/env python3
def calculate_fuel_basic(mass):
    return max((mass // 3) - 2, 0)


def calculate_fuel_with_extra(mass):
    needed = calculate_fuel_basic(mass)
    if needed == 0:
        return 0
    return needed + calculate_fuel_with_extra(needed)


with open("aoc_day_1.txt", "r") as file:
    masses = [int(line) for line in file.read().split()]

print("Part one:", sum([calculate_fuel_basic(m) for m in masses]))
print("Part two:", sum([calculate_fuel_with_extra(m) for m in masses]))

