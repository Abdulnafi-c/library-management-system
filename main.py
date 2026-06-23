import database

def main_menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. List Books")
        print("2. Add Book")
        print("3. Delete Book")
        print("4. Exit")
        
        try:
            choice = input("Select an option: ")
            
            if choice == '1':
                books = database.get_all_books()
                if not books:
                    print("No books found.")
                for book in books:
                    print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]}")
                    
            elif choice == '2':
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                database.add_book(title, author)
                print("Book added successfully!")
                
            elif choice == '3':
                book_id = input("Enter book ID to delete: ")
                database.delete_book(book_id)
                print("Book deleted successfully!")
                
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    database.init_db()
    main_menu()
