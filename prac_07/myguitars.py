from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Main function to run the guitar management program"""
    guitars = load_guitars(FILENAME)

    display_guitars(guitars)

    guitars.sort()

    sort_guitars(guitars)

    add_guitar(guitars)

    save_guitars(guitars)


def display_guitars(guitars):
    """Display all guitars currently stored in the list."""
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)


def sort_guitars(guitars):
    """Display guitars sorted by year"""
    print("Sorted by year :")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def add_guitar(guitars):
    """Prompt the user to input a new guitar's details and add it to the list."""
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost:$ "))
    guitars.append(Guitar(name, year, cost))


def save_guitars(guitars):
    """Write guitars back to the file."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            line = f"{guitar.name},{guitar.year},{guitar.cost}\n"
            out_file.write(line)


main()
