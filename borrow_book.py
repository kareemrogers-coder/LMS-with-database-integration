from db_connection import connect_lib, Error

def borrow_books():
    conn = connect_lib()

    if conn is not None:
        try:
            book_id = input(f"Please enter the book id: ")
            cursor = conn.cursor()

            query = "UPDATE books SET availability = False WHERE id = %s" 

            cursor.execute(query,(book_id,))
            conn.commit()

            select_query = "SELECT * FROM books WHERE id = %s "
            cursor.execute(select_query, (book_id,))
           

            id, title, author_id, isbn, publication_date, availability = cursor.fetchone()
            print(f"{id}: {title}, {author_id}, {isbn}, {publication_date}, {availability}")
            print(f"Book under the {title} was borrowed successfully")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    borrow_books()

