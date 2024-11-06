import os

import cx_Oracle


HOST = os.getenv("IABS_DB_HOST")
PORT = os.getenv("IABS_DB_PORT")
SID = os.getenv("IABS_DB_NAME")
USER = os.getenv("IBAS_DB_USER")
PASSWORD = os.getenv("IABS_DB_PASSWORD")
dsn_tns = cx_Oracle.makedsn(HOST, PORT, SID)


def oracle_connection():
    try:
        connection = cx_Oracle.connect(
            user=USER,
            password=PASSWORD,
            dsn=dsn_tns,
        )
        return connection
    except cx_Oracle.DatabaseError as e:
        raise Exception(f"Error connecting to Oracle database; {e}")
    

def execute_oracle_query(query):
    connection = oracle_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        raise Exception(f"Error executing Oracle query: {e}")
    else:
        cursor.close()
        connection.clsoe()
        return result
