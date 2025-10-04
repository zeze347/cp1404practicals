"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while numerator == 0 or denominator == 0:
        if numerator == 0:
            numerator = int(input("Enter the numerator: "))
        elif denominator == 0:
            denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
# When will a ValueError occur?
# When a non-integer value is entered

# When will a ZeroDivisionError occur?
# When the denominator or numerator is 0

# Could you change the code to avoid the possibility of a ZeroDivisionError?

# If the user enters the denominator or numerator of 0, add a loop structure
# before calculating the result to prompt the user to re-enter until it is not 0.