from db_connection import connect_lib, Error

def fetch_all_users():
    conn = connect_lib()

    if conn is not None:
        try: 
            cursor = conn.cursor()

            query = "SELECT * FROM users;"

            cursor.execute(query)

            for id, name, library_id in cursor.fetchall():
                print(f"{id}: {name}, {library_id}")

        except Error as e:
            print(f"Error: {e}")
        

        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    fetch_all_users()  


def user_search():
    conn = connect_lib()

    if conn is not None:
        try:
            user_id = input("Please enter the user id: ")
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE id = %s"

            cursor.execute(query, (user_id,))

            id, name, library_id = cursor.fetchone()
            print(f"{id}: {name}, {library_id}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

        
if __name__ == "__main__":   
    user_search()