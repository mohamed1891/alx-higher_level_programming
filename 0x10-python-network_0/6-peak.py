#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    # Check if the list is empty
    if list_of_integers is None or list_of_integers == []:
        return None
    
    # Define search boundaries
    lo = 0
    hi = len(list_of_integers)

    # Calculate the middle index
    mid = (hi - lo) // 2 + lo
    mid = int(mid)

    # Handle base cases for lists of size 1 or 2
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)

    # Check if the middle element is a peak
    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    
    # Recursively search in the right half of the list
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    
    # Recursively search in the left half of the list
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

