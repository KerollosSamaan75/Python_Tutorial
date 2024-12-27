import os
from datetime import datetime

def create_diary_entry(file_name):
    try:
        with open(file_name, 'a') as file:
            entry = input("Enter your diary entry: ")
            add_timestamp = input("Do you want to add a timestamp? (yes/no): ")
            if add_timestamp.lower() == 'yes':
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{timestamp} - {entry}\n")
            else:
                file.write(f"{entry}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_diary_entries(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                entries = file.readlines()
                if entries:
                    for entry in entries:
                        print(entry.strip())
                else:
                    print("No entries found.")
        else:
            print("Diary file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = "diary.txt"
    while True:
        print("\n1. Create new diary entry")
        print("2. View diary entries")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_diary_entry(file_name)
        elif choice == '2':
            view_diary_entries(file_name)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

main()
