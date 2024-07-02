import sqlite3
from pprint import pprint

with sqlite3.connect("book_store.sqlite3") as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS authors(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            birthday_year INTEGER CHECK (birthday_year > 1457)
        )
    """

    cursor.execute(query)

    insert_query = """
        INSERT INTO authors (name, birthday_year)
        VALUES (?, ?)
    """

    new_authors = [
        ("Еріх Марія Ремарк", 1898),
        ("Фредерік Бегбеде", 1965),
        ("Чарльз Діккенс", 1812),
        ("Француаза Саган", 1935),
    ]

    cursor.executemany(insert_query, new_authors)

    cursor.execute(insert_query, ["Шарлотта Бронте", 1816])

    query_where = """
         SELECT title
         FROM new_books
         WHERE title LIKE '%Рецепт%'
    """

    query_where2 = """
        SELECT title, price, information, author_id
        FROM new_books
        LIMIT 2
        OFFSET 1
    """

    result2 = cursor.execute(query_where)
    print("#6 \n")
    pprint(result2.fetchall())
    print("\n#9\n")

    result = cursor.execute(query_where2)
    pprint(result.fetchall(), indent=1)
