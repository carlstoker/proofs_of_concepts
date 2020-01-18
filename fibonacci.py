#!/usr/bin/env python3
"""Fibonacci sequence generator"""


def fibonacci(desired, num_1=0, num_2=1):
    """
    Print a sequence of fibonacci numbers.

    Keyword arguments:
        desired -- Integer at which the sequence will be terminated.
        num_1 -- First component integer.
        num_2 -- Second component integer.
    """
    print(num_1, end=' ')

    if (num_1 + num_2) < desired:
        # Recursively pass new numbers to fibonacci function if the
        # sum of num_1 and num_2 are less than the desired integer.
        fibonacci(desired, num_2, num_1 + num_2)
    else:
        print(num_2)


def main():
    desired = int(input("Enter desired number: "))
    fibonacci(desired)


if __name__ == '__main__':
    main()
