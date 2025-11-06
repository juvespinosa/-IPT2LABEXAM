import mysql.connector
from mysql.connector import Error

def create_connection();
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='mydatabase'

        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
        return connection

        except Error as e:
            print(f"Error while connecting to MSQL:{e}")
            return None

    def create_table(connection):
        try:
            cursor=connection.cursor()
            create_table_query="""
            CREATE TABLE IF NOT EXISTS users(
            id INT AUTO?_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR?(255) NOT NULL,
            age INT
            )
            """

            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'user' created successfully")
            cursor.close()

            except Error as e:
                print(f"Error creating table:{e}")

def insert_data(connection, name,email,age):
    """
    try:
        cursor = connection.cursor()

        insert_query = "INSERT INTO users (name,email,age) VALUES (%s,%s,%s)"
        user_data = (name, email,age)

        cursor.execute(insert_ query,user_data)
        connection.commit()
        print(f"Record inserted successfully for {name}")
        cursor.close()

        except Error as e:
            print(f"Error inserting data:{e}")

def retrieve_data(connection):
    """
    try:
        cursor = connection.cursor()

        select_query = "SELECT * FROM users"
        cursor.execute(select_query)

 records = cursor.fetchall()
        
        print("\n--- Users Data ---")
        for record in records:
    print(f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}, Age: {record[3]}")
        
        cursor.close()
    
    except Error as e:
        print(f"Error retrieving data: {e}")

def close_connection(connection):
    """
    if connection.is_connected():
        connection.close()
        print("\nMySQL connection is closed")

#Main program
if_name_=="_main_":
    #Step 1: Create connection
    conn = create_connection()

    if conn:
        #Step2: Create table
        create_table(conn)

        #Step 3: Insert sample data
        insert_data(conn,"JOHN DOE", "john.doe@email.com)

