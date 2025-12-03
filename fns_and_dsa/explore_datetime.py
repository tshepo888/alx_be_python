from datetime import datetime, timedelta

# Part 1: Function to display current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Function to calculate the future date after adding a specified number of days
def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in the desired format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function to drive the script
def main():
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Prompt the user to input the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Call the function to calculate and display the future date
    calculate_future_date(days_to_add)

if __name__ == "__main__":
    main()
