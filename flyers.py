#!/usr/bin/env python3
"""
Return URL of the most recent sales flyer of a chain, for use elsewhere.
"""
import datetime
import sys


def main(chain, store_number):
    chains = {
        'shaws': shaws
    }

    func = chains.get(chain, lambda n: 'Invalid chain selected.')
    print(func(int(store_number)))


def shaws(store_number):
    """
    Return flyer URL for the Shaws grocery chain.

    Keyword arguments:
        store_number -- Your local store number.  Example: 00624
    """
    base_url = 'https://circulars-prod.cpnscdn.com/pdf-cache/Shaws/19_{}_SHW_WC_S/stores/{:05d}.pdf'

    # Calculate week number for the flyer.
    week = int(datetime.date.today().strftime("%U")) % 52 + 51
    return base_url.format(week, store_number)


if __name__ == '__main__':
    main(*sys.argv[1:3])
