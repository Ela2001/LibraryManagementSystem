import sqlite3


def get_connection():
    return sqlite3.connect("library.db")


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    with open("sql/create_tables.sql", "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    connection.commit()
    connection.close()