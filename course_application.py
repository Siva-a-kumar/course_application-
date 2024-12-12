import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


# Function to connect to the database and fetch data
def fetch_data():
    
    try:
        # Establish a secure connection to the database
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
	if connection.is_connected():
            print("Connection to MySQL database successful")
        else:
            print("Failed to connect to MySQL database")
        if connection.is_connected():
            print("Successfully connected to the database.")

            # Define the SQL query to join the tables and fetch the required fields
             # SELECT 
                #     p.program_name AS Program,
                #     u.email AS Email,
                #     c.course_name AS CourseName,
                #     a.applying_level AS ApplyingLevel,
                #     a.current_level AS CurrentLevel,
                #     a.fee_details AS FeeDetails,
                #     a.application_status AS ApplicationStatus
                # FROM applications a
                # INNER JOIN users u ON a.user_id = u.user_id
                # INNER JOIN programs p ON a.program_id = p.program_id
                # INNER JOIN courses c ON p.course_id = c.course_id;
                 #use course_registration_2;

            query = """
                
                SELECT 
                a.program, 
                a.email, 
                 c.course_name, 
               t.applying_level, 
               t.current_level, 
              c.fee_details, 
              ap.application_status 
             FROM 
              Account a 
              INNER JOIN Term_course_registration_application t ON a.id = t.account_id 
             INNER JOIN Application ap ON t.application_id = ap.id 
             INNER JOIN Course c ON t.course_id = c.id;
            """

            # Execute the query and fetch the data into a pandas DataFrame
            data_frame = pd.read_sql(query, connection)
            return data_frame

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Fetch the data and display the DataFrame
print("test")

data = fetch_data()
print("hi")
if data is not None:
    print(data.head())

