#!/usr/bin/python3

def roman_to_int(roman_string):
    # Define the mapping of Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the result
    result = 0

    # Check if the input is valid
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Iterate through the Roman string from left to right
    for i in range(len(roman_string)):
        current_value = roman_values.get(roman_string[i], 0)
        next_value = roman_values.get
        (roman_string[i + 1], 0) if i + 1 < len(roman_string) else 0

        # If the current value is less than the next value, subtract it
        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result
