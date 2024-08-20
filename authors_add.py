from db_connection import connect_lib, Error

def add_authors():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("Please enter the authors name:  ").title()
            biography = input("Please enter a breif Bio: ")

            new_authors = (name, biography)

            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"

            cursor.execute(query, new_authors)
            conn.commit()
            print(f"New Author {name} added successfully!")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    add_authors()
