from db_connection import connect_lib, Error

def add_users():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("Please enter the users name:  ").title()
            library_id = input("Please enter your library id: ")

            new_users = (name, library_id)

            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"

            cursor.execute(query, new_users)
            conn.commit()
            print(f"New Author {name} added successfully!")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    add_users()