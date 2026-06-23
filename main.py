import sqlite3

def connect_db():
    return sqlite3.connect('library.db')

def main_menu():
    print("\n--- Library Management System ---")
    print("1. List Books")
    print("2. Add Book")
    print("3. Exit")
    return input("Your choice: ")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == '1':
            print("Listing books...")
        elif choice == '2':
            print("Add book screen...")
        elif choice == '3':
            break
