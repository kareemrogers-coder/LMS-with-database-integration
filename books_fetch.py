from db_connection import connect_lib, Error

def fetch_all_books():
    conn = connect_lib()

    if conn is not None:
        try: 
            cursor = conn.cursor()

            query = "SELECT * FROM books;"

            cursor.execute(query)

            for id, title, author_id, isbn, publication_date, availablity in cursor.fetchall():
                print(f"{id}: {title}, {author_id},{isbn}, {publication_date},{availablity}")

        except Error as e:
            print(f"Error: {e}")
        

        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    fetch_all_books()   


def book_search():
    conn = connect_lib()

    if conn is not None:
        try:
            book_id = input("Please enter the book id: ")
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE id = %s"

            cursor.execute(query, (book_id,))

            id, title, author_id, isbn, publication_date, avail = cursor.fetchone()
            print(f"{id}: {title}, {author_id}, {isbn}, {publication_date}, {avail}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

        
if __name__ == "__main__":   
    book_search()