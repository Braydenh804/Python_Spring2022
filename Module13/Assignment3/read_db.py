import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows # return the rows


def select_all_students(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return: the row from the db
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows # return the rows
