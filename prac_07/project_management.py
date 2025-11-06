"""
Program: project_management.py
Estimate: 30 minutes
Actual: 45 minutes
"""
from project import Project

FILENAME = 'projects.txt'
def main():
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(load_projects(FILENAME))} projects from {FILENAME}")
    display_menu()
    choice = input(">>> ".upper())
    while choice != "Q":
        if choice == "L":


def load_projects(filename):
    projects = []
    with open(filename, 'r') as infile:
        infile.readline()
        for line in infile:
            line = line.strip()
            parts = line.split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        return projects



def display_menu():
    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print(menu)

main()

