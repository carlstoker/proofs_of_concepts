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
    sequence = [num_1]

    if (num_1 + num_2) < desired:
        # Recursively pass new numbers to fibonacci function if the
        # sum of num_1 and num_2 are less than the desired integer.
        sequence.extend(fibonacci(desired, num_2, num_1 + num_2))
    else:
        sequence.append(num_2)

    return sequence


def main():
    desired = int(input("Enter desired number: "))
    formatted_sequence = ', '.join(str(i) for i in fibonacci(desired))
    print('{}.'.format(formatted_sequence))

if __name__ == '__main__':
    main()
