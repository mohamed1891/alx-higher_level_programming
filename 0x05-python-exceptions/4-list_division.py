#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if the index is out of range
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
            else:
                # Check if the elements are numbers
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    print("wrong type")
                    result.append(0)
                else:
                    # Perform division and check for division by zero
                    try:
                        division_result = my_list_1[i] / my_list_2[i]
                        result.append(division_result)
                    except ZeroDivisionError:
                        print("division by 0")
                        result.append(0)
        except Exception as e:
            # Catch any unexpected exceptions
            print(f"An unexpected error occurred: {e}")
            resul
