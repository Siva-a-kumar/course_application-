import mysql.connector
from mysql.connector import Error

# Function to connect to MySQL
def connect_to_mysql():
    try:
        # Replace with your actual database credentials
        conn = mysql.connector.connect(
            host='localhost',  # or an IP address or domain name
            user='root',
            password='root',
            database='course_registration_2'
        )

        if conn.is_connected():
            print("Connection to MySQL database successful")
        else:
            print("Failed to connect to MySQL database")
        
        # Close the connection
        conn.close()
    
    except Error as e:
        print("Failed to connect to MySQL database:", e)

# Call the function
connect_to_mysql()
