#!/usr/bin/python3
""" UTF-8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """This method determines if a given data set
    represents a valid UTF-8 encoding.
    
    Args:
        data list(int): list of integers
    Return:
        bool

    Examples:
        >>> data = [65]
        >>> print(validUTF8(data))
        >>> True
        >>>
        >>> [80, 121, 116, 104, 111,
        ...  110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
        >>> print(validUTF8(data))
        >>> True
        >>>
        >>> data = [229, 65, 127, 256]
        >>> print(validUTF8(data))
        >>> False
    """
    bytes_left = 0

    for byte in data:
        if bytes_left == 0:
            if (byte & 0b10000000) == 0:
                bytes_left = 0
            elif (byte & 0b11100000) == 0b11000000:
                bytes_left = 1
            elif (byte & 0b11110000) == 0b11100000:
                bytes_left = 2
            elif (byte & 0b11111000) == 0b11110000:
                bytes_left = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            bytes_left -= 1

    return bytes_left == 0
