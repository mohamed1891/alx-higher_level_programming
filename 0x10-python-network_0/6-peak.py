#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        A peak element from the list, if it exists, otherwise None.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize search boundaries
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search
    while low < high:
        mid = (low + high) // 2  # Calculate mid index

        # Compare middle element with its right neighbor
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1  # Update search range to the right
        else:
            high = mid  # Update search range to the left

    # Return peak element
    return list_of_integers[low]

