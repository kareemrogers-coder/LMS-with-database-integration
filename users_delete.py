from db_connection import connect_lib, Error

def delete_users():
    conn = connect_lib()

    if conn is not None:
        try:
            cursor = conn.cursor()

            library_id = input("Please enter user library id: ")

            deleted_user = (library_id)

            query = "DELETE FROM users WHERE library_id = %s"
            
            cursor.execute(query, (library_id,))
            conn.commit()
            print(f" User under Library Id {library_id} has been deleted.")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close") 

if __name__ == "__main__":
    delete_users()