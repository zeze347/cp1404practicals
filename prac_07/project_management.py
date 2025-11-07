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

def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    incomplete = sorted(incomplete, key=lambda project: project.priority)
    complete = sorted(complete, key=lambda project: project.priority)
    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project.format_for_display()}")

    print("Completed projects: ")
    for project in complete:
        print(f"  {project.format_for_display()}")

def add_new_project(project):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    project.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project.format_for_display())
    choice = int(input("Project choice: "))
    print(projects[choice].format_for_display())

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        projects[choice].completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":
        projects[choice].priority = int(new_priority)

def filter_projects_by_date(projects):
    try:
        user_date = input("Show projects that start after date (dd/mm/yy): ")
        user_date = parse_date(user_date)
        projects_after_user_date = []
        for project in projects:
            project_start_date = parse_date(project.start_date)
            if project_start_date >= user_date:
                projects_after_user_date.append(project)
        projects_after_user_date.sort(key=lambda single_project: parse_date(single_project.start_date))
        for project in projects_after_user_date:
            print(project.format_for_display())
    except ValueError:
        print("Dates must be in dd/mm/yy format")
def parse_date(date_string):
    parsed_date = datetime.datetime.strptime(date_string.strip(), "%d/%m/%Y").date()
    return parsed_date

main()

