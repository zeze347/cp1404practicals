"""
Program: project.py
Estimate: 30 minutes
Actual: 45 minutes
"""


class Project:
    """Represent a project with a name, start date, priority, cost and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a compact one-line representation for debugging."""
        return (f"{self.name}, {self.start_date}, "
                f"{self.priority}, {self.cost_estimate}, {self.completion_percentage}")

    def is_complete(self):
        """Return True if the project is completed."""
        return self.completion_percentage >= 100

    def format_for_display(self):
        """Return the formatted project string for display"""
        return (f"{self.name}, start: {self.start_date}, "
                f"priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")
