import mysql.connector
from mysql.connector import Error
def connect_database():


    db_name="gym_membership_sql_db"
    user="root"
    password ="#Comco92505"
    host ="127.0.0.1"
    try:
        conn=mysql.connector.connect(
        database=db_name,
        user=user,
        password= password,
        host=host
    )
        
        print("Connected to MYSQL database succesful")  
        return conn         
    except Error as e:
        print(f"Error: {e}")
        return None


