# Prompt the user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Use a Match Case statement to react based on the task's priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task."
    case "medium":
        reminder_message = f"'{task}' is a medium priority task."
    case "low":
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = "Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " It requires immediate attention today!"
else:
    reminder_message += " Consider completing it when you have free time."

# Print the final reminder message
print(f"Reminder: {reminder_message}")
