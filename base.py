import sqlite3

with sqlite3.connect("travels.sqlite3") as connection:
    cursor = connection.cursor()
