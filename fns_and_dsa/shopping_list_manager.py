def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("\nEnter the item to add: ").lower()
            shopping_list.append(item)
            print(f"Your item {item} has been added to the List\n")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("\nEnter the name of the item you want to remove: ").lower()
            if (item in shopping_list):
                shopping_list.remove(item)
                print(f"The item {item} has been removed\n")
            else:
                print(f"The Item {item} is not in the Shopping List\n")
                
        elif choice == '3':
            for i in shopping_list:
                print(i)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
