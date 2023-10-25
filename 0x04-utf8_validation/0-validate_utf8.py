#!/usr/bin/env python3
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
    pass
