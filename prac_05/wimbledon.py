"""
Program: wimbledon.py
Estimate: 30 minutes
Actual: 45 minutes
"""
import csv

filename = "wimbledon.csv"

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = list(reader)[1:]
        return data

def get_champion(data):
    champion_to_count = {}
    for line in data:
        champion = line[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count


def get_countries(data):
    countries = {line[1] for line in data}
    return sorted(countries)

def main():
    data = read_file(filename)
    champion_to_count = get_champion(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
