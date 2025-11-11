import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql.freedb.tech",
        user="freedb_hardik04",
        password="pjpf63@&u3hA6w7",
        database="freedb_personal_portfolio"
    )
