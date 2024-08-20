from db_connection import connect_lib, Error

def add_books():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input(" Please enter the title of the book: ")
            isbn = input(" Please enter the isbn number: ")
            publication_date = input("Please enter the publication using (yyyy-mm-dd) format: ")
            author_id = int(input("Please in the author id (Numbers only): "))

            new_book = (title, isbn, publication_date, author_id)

            query = "INSERT INTO books (title, isbn, publication_date, author_id) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit()
            print(f"New Book {title} has been added successfully")
 
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")   

if __name__ == "__main__":
    add_books()