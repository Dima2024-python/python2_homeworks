import sqlite3

with sqlite3.connect('travel_agency.sqlite3') as connection:
    cursor = connection.cursor()