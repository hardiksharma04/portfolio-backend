import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="54321",          # your MySQL password
        database="portfolio"  # your database name
    )
