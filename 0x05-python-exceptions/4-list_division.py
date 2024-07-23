#!/usr/bin/python3

def list_division(ls_1, ls_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Check if the index is out of range for the lists
            if i >= len(ls_1) or i >= len(ls_2):
                raise IndexError  # This will be caught by the IndexError block

            # Check if the element in ls_1 is a number
            if not isinstance(ls_1[i], (int, float)):
                print("wrong type")
                new_list.append(0)
                continue  # Skip the rest of the loop for this iteration

            # Check if the element in ls_2 is a number
            if not isinstance(ls_2[i], (int, float)):
                print("wrong type")
                new_list.append(0)
                continue  # Skip the rest of the loop for this iteration

            # Perform the division
            new_list.append(ls_1[i] / ls_2[i])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
