import mysql.connector
from mysql.connector import errorcode

import yaml

with open('/home/olin/Robotics/ros_pos_ws/src/price_lookup.yaml', "r") as file:
    default_entries = yaml.safe_load(file)



class Database:
    def __init__(self):
        
        conn = mysql.connector.connect(
            host='localhost',   # MySQL server address
            user='olin',        # MySQL username
            password='start'  # MySQL password
        )

        cursor = conn.cursor()
        self.db_name = "my_business_database"
        try:
            # Create a new database
            cursor.execute("CREATE DATABASE "+self.db_name+";")
            print("Database "+self.db_name+" created successfully.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print("Database already exists.")
            else:
                print(f"Error: {err}")

        # Close cursor and connection
        cursor.close()
        conn.close()
    
    def lookup_price(self, item_name):
        conn = mysql.connector.connect(
            host='localhost',        # server address
            user='olin',    # MySQL username
            password='start',  # MySQL password
            database=self.db_name   # Database name
        )
        cursor = conn.cursor()
        
        lookup_query = "SELECT price FROM example_table WHERE item_name = '"+item_name+"';"
        cursor.execute(lookup_query)
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0
    
    def create_price_lookup_table(self):
        conn = mysql.connector.connect(
            host='localhost',        # server address
            user='olin',    # MySQL username
            password='start',  # MySQL password
            database=self.db_name   # Database name
        )
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            item_name VARCHAR(255),
            price DOUBLE
        );
        """
        cursor.execute(create_table_query)
        print("Table created successfully (if not already exists).")
        cursor.close()
        conn.close()
    
    def drop_table(self):
        conn = mysql.connector.connect(
            host='localhost',        # MySQL server address
            user='olin',    # Your MySQL username
            password='start',  # Your MySQL password
            database=self.db_name   # Database name
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        drop_table_query = """
        DROP TABLE IF EXISTS example_table;
        """
        cursor.execute(drop_table_query)
        print("Table dropped successfully.")
        cursor.close()
        conn.close()
    
        

    def insert_data(self, dic=default_entries):
        # Connect to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',        # MySQL server address
            user='olin',    # Your MySQL username
            password='start',  # Your MySQL password
            database=self.db_name   # Database name
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = """
        INSERT INTO example_table (item_name, price)
        VALUES (%s, %s)
        """

        # Data to insert
        for key, value in dic.items():
            data = (key, value)
            cursor.execute(insert_query, data)

        # Commit the transaction to save changes
        conn.commit()

        print(f"{cursor.rowcount} record(s) inserted.")

        # Close the cursor and connection
        cursor.close()
        conn.close()
