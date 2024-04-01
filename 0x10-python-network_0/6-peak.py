#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    left, right = 0, len(list_of_integers) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
