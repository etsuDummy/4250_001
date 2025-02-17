# Recursive Number Problem Alex Cox Laynie Jaramillo used ChatGPT o3 to apply design to code.
def recursive_digit_sum(number):
    """
    Recursively reduces a number by removing its last digit (from its string representation)
    and adding it to the remaining part until only one digit remains (ignoring the decimal point).

    For example, with 5.876:
      "5.876"   -> remaining part "5.87" and last digit "6"  -> 5.87 + 6   = 11.87
      "11.87"   -> remaining part "11.8" and last digit "7"  -> 11.8 + 7   = 18.8
      "18.8"    -> remaining part "18"   and last digit "8"  -> 18 + 8     = 26
      "26"      -> remaining part "2"    and last digit "6"  -> 2 + 6      = 8
    Negative numbers are handled by storing the negative sign and reapplying it to both parts.
    """
    # Convert the number to a string.
    number_string = str(number)

    # If the number is negative, record the negative sign and remove it from the string.
    # This is used to reapply the sign to both the remaining part and the last digit.
    number_sign = 1
    if number_string.startswith('-'):
        number_sign = -1
        number_string = number_string[1:]  # Remove the '-' for processing

    # Helper function: Count only digit characters (ignore any decimal points).
    # This is used to determine when the number has been reduced to a single digit.
    def count_numeric_characters(string):
        return len([character for character in string if character.isdigit()])

    # Base case: When there's only one digit (ignoring the decimal point), return the number.
    # Convert to float if there is a decimal point, otherwise as an integer. Reapply the original sign.
    if count_numeric_characters(number_string) == 1:
        # Convert to float if there is a decimal point, otherwise as an integer.
        final_result = float(number_string) if '.' in number_string else int(number_string)
        return number_sign * final_result

    # Remove the last character from the string (this should be a digit).
    last_character = number_string[-1]
    truncated_number = number_string[:-1]

    # If the remaining string ends with a decimal point, remove it. This can happen if the last digit was a decimal.
    if truncated_number.endswith('.'):
        truncated_number = truncated_number[:-1]

    # Convert the remaining part of the string to a number. Convert to float if there is a decimal point.
    remaining_value = float(truncated_number) if '.' in truncated_number else int(truncated_number)
    # Convert the removed last character to an integer.
    last_digit_value = int(last_character)

    # Reapply the original sign to both the remaining part and the last digit. This is needed for negative numbers.
    remaining_value *= number_sign
    last_digit_value *= number_sign

    # Sum the two parts. Print the sum for each step.
    new_number = remaining_value + last_digit_value
    print(f"Current sum: {remaining_value} + {last_digit_value} = {new_number}")

    # Recursively process the new sum.
    return recursive_digit_sum(new_number)


def main():
    """
    A simple console application that:
      - Prompts the user to enter two numbers (either integers or floats),
      - Adds them together,
      - Applies the recursive digit-sum reduction until only one digit remains.
    """
    while True:
        first_input = input("Enter the first number (or 'q' to quit): ")
        if first_input.lower() == 'q':
            break
        second_input = input("Enter the second number (or 'q' to quit): ")
        if second_input.lower() == 'q':
            break

        try:
            first_number = float(first_input)
            second_number = float(second_input)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        total_sum = first_number + second_number
        print(f"Initial sum: {first_number} + {second_number} = {total_sum}")

        final_result = recursive_digit_sum(total_sum)
        print(f"Final single-digit result: {final_result}\n")


if __name__ == '__main__':
    main()
