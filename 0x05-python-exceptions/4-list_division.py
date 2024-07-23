#!/usr/bin/python3

fl = float
t = int
isn = isinstance


def list_division(ls_1, ls_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if the index is out of range for the lists
            if i >= len(ls_1) or i >= len(ls_2):
                print("out of range")
                result.append(0)
            else:
                # Check if the elements are numbers
                if not isn(ls_1[i], (t, fl)) or not isn(ls_2[i], (t, fl)):
                    print("wrong type")
                    result.append(0)
                else:
                    # Perform division and handle division by zero
                    try:
                        result.append(ls_1[i] / ls_2[i])
                    except ZeroDivisionError:
                        print("division by 0")
                        result.append(0)
        except Exception as e:
            # Catch any unexpected exceptions
            print(f"An unexpected error occurred: {e}")
            result.append(0)

    return result
