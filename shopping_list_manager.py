def display_menu():
    # Display the options for the user
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list
    
    while True:
        # Display the menu and get the user's choice
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Add item to the list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':
            # Remove item from the list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        
        elif choice == '3':
            # View the shopping list
            if shopping_list:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
