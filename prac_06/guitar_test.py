from guitar import Guitar

def main():
    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("other guitar", 2013, 10000)


    print(f"{Gibson.name} get_age() - Expected 103. Got {Gibson.get_age()}")
    print(f"{other_guitar.name} get_age() - Expected 12. Got {other_guitar.get_age()}")
    print()
    print(f"{Gibson.name} is_vintage() - Expected True. Got {Gibson.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - Expected False. Got {other_guitar.is_vintage()}")
main()