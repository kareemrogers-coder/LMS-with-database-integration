from db_connection import connect_lib, Error

def delete_authors():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()

            author_id = input("Please enter the author id: ")

            author_info = "SELECT * FROM authors WHERE id = %s"

            cursor.execute(author_info,(author_id,))

            id, name, biography = cursor.fetchone()
            print(f" Author {name} under id number {id} has been successfully deleted")

            query = "DELETE FROM books WHERE author_id = %s"
            
            cursor.execute(query, (author_id,))
            conn.commit()

            query1 = "DELETE FROM authors WHERE id = %s"
            cursor.execute(query1, (author_id,))
            conn.commit()


        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close") 

if __name__ == "__main__":
    delete_authors()

