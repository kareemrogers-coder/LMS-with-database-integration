from db_connection import connect_lib, Error

def fetch_all_authors():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM authors"

            cursor.execute(query)

            for id, name, biography in cursor.fetchall():
                print(f"{id}: {name}, {biography}")

        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    fetch_all_authors()

def author_search():
    conn = connect_lib()

    if conn is not None:
        try:
            author_id = input("Please enter the author id: ")
            cursor = conn.cursor()

            query = "SELECT * FROM authors WHERE id = %s"

            cursor.execute(query, (author_id,))

            id, name, bio = cursor.fetchone()
            print(f"{id}: {name}, {bio}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

        
if __name__ == "__main__":   
    author_search()