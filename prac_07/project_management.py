"""
Program: project_management.py
Estimate: 5 hours
Actual:  7 hours
"""
import datetime
from project import Project

FILENAME = 'projects.txt'


def main():
    """Print the welcome message and the menu. Users can then choose which function to execute."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILENAME)
        elif choice == "S":
            filename_input = input("Filename: ")
            if filename_input == "":
                filename_input = FILENAME
            save_projects(filename_input, projects)
            print(f"Projects have been saved to {filename_input}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").upper()
    user_answer = input(f"Would you like to save to {FILENAME}? ").upper()
    if user_answer.startswith("Y"):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load the project data file and store it in the memory.  """
    projects = []
    with open(filename, 'r', encoding='utf-8') as infile:
        infile.readline()
        for line in infile:
            line = line.strip()
            parts = line.split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(float(parts[4]))
            projects.append(
                Project(
                    name,
                    start_date,
                    priority,
                    cost_estimate,
                    completion_percentage
                )
            )
        return projects


def display_menu():
    """Display the program menu"""
    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print(menu)


def display_projects(projects):
    """Display completed and incomplete projects"""
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


def add_new_project(projects):
    """Add a new project to the list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update the percentage and priority of the project"""
    for i, project in enumerate(projects):
        print(i, project.format_for_display())

    try:
        choice = int(input("Project choice: "))
        print(projects[choice].format_for_display())
        new_percentage = input("New Percentage: ")
        if new_percentage != "":
            projects[choice].completion_percentage = int(new_percentage)
        new_priority = input("New Priority: ")
        if new_priority != "":
            projects[choice].priority = int(new_priority)

    except (IndexError, ValueError):
        print("Please enter a valid number")


def filter_projects_by_date(projects):
    """Filter the projects by date"""
    try:
        date = input("Show projects that start after date (dd/mm/yy): ")
        date = parse_date(date)
        projects_after_date = []
        for project in projects:
            project_start_date = parse_date(project.start_date)
            if project_start_date >= date:
                projects_after_date.append(project)
        projects_after_date.sort(key=lambda single_project: parse_date(single_project.start_date))
        for project in projects_after_date:
            print(project.format_for_display())
    except ValueError:
        print("Dates must be in dd/mm/yy format")


def parse_date(date_string):
    """Parse a date string into a datetime object."""
    parsed_date = datetime.datetime.strptime(date_string.strip(), "%d/%m/%Y").date()
    return parsed_date


def save_projects(filename, projects):
    """Save the projects data to file"""
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            outfile.write(
                f"{project.name}\t"
                f"{project.start_date}\t"
                f"{project.priority}\t"
                f"{project.cost_estimate}\t"
                f"{int(project.completion_percentage)}\n"
            )


main()
