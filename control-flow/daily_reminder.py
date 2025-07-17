# Prompt for a single task
task = input("Enter a task description: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes or no): ")

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Adjust for time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Provide customized reminder
print(reminder)