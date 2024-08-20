from db_connection import connect_lib, Error

def delete_books():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()
            books_id = input("Please enter the book id: ")

            query1 = "SELECT * FROM books WHERE id = %s"
            
            cursor.execute(query1, (books_id,))

            id, title, author_id, isbn, publication_date, availablity = cursor.fetchone()
            print(f" Book Title {title} under id number {id} has been successfully deleted")

            
            query = "DELETE FROM books WHERE id = %s"
            
            cursor.execute(query, (books_id,))
            conn.commit()

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close") 

if __name__ == "__main__":
    delete_books()