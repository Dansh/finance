import sqlite3


class DataBase:
    def __init__(self, file_name):
        self.filename = file_name
        self.con = sqlite3.connect(self.filename)
        self.cursor = self.con.cursor()
        
    def create_table(self, table_name, *columns):
        # Create table
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} {str(columns)}")
        except sqlite3.OperationalError:
            print("ERROR - Table Already Exists!")
    
    def insert_row(self, table_name, *values):
        # Insert a row of data
        self.cursor.execute(f"INSERT INTO {table_name} VALUES {values}")
        # Save (commit) the changes
        self.con.commit()

    def __del__(self):
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.con.close()



if __name__ == "__main__":
    users_db = DataBase("users.db")
    users_db.create_table("users", "username", "password")
    users_db.insert_row("users", "dan", "123")
    del users_db
