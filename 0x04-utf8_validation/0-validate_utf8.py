#!/usr/bin/python3
"""
Validates UTF-8 encoding.
"""


def valid_UTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the bytes of the data.

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
        otherwise False.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask_byte = 1 << 7

        if num_bytes == 0:
            while mask_byte & byte:
                num_bytes += 1
                mask_byte >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
