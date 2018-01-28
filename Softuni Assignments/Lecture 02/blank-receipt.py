#!/usr/bin/env python
"""Prints a blank cash receipt"""

__author__ = "Petar Stoyanov"

HEADER = "CASH RECEIPT"
DELIMITER = "------------------------------"
CHARGED = "Charged to____________________"
RECEIVED = "Received by___________________"
FOOTER = "\u00A9 SoftUni" # copyright


def combine_parts():
    """Prints the separate parts of the receipt.

    Returns:
        None.
    """
    print_receipt_header()
    print_receipt_body()
    print_receipt_footer()


def print_receipt_header():
    """Prints receipt header

    Returns:
        None.
    """
    for i in [HEADER, DELIMITER]:
        print(i)


def print_receipt_body():
    """Prints receipt body

    Returns:
        None.
    """
    for i in [CHARGED, RECEIVED,
              DELIMITER]:
        print(i)


def print_receipt_footer():
    """Prints receipt footer part

    Returns:
        None.
    """
    print(FOOTER)


if __name__ == '__main__':
    combine_parts()
