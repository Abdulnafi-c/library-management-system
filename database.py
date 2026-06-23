import sqlite3

def connect_db():
    return sqlite3.connect('library.db')

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    # Virgül hatasını düzelttim ve tabloyu oluşturduk
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      author TEXT NOT NULL,
                      is_available INTEGER DEFAULT 1)''')
    conn.commit()
    conn.close()

# --- CRUD Operations ---

def add_book(title, author):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

def get_all_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
