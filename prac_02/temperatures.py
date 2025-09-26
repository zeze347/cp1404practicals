"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
def covert_celsius_to_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def covert_fahrenheit_to_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

def main():
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            covert_celsius_to_fahrenheit()
        elif choice == "F":
            covert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()