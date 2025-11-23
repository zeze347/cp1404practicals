from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Controls the simulation flow."""
    print("Let's drive!")

    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    bill_to_date = 0.0
    current_taxi = None
    print(MENU)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            cost = drive_taxi(current_taxi)
            if cost > 0:
                print(f"Your {current_taxi.name} trip cost you ${cost}")
                bill_to_date += cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Print the list of taxis with their index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Let user choose a taxi and return it."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return None


def drive_taxi(current_taxi):
    """Perform a trip using the selected taxi and return the cost."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0

    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    current_taxi.start_fare()
    current_taxi.drive(distance)
    return current_taxi.get_fare()


if __name__ == "__main__":
    main()
