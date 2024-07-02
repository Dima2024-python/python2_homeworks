import sqlite3

with sqlite3.connect("new_db.sqlite3") as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            login TEXT NOT NULL CHECK (length(login) > 3) UNIQUE,
            password TEXT NOT NULL
        )
    """

    ather_table = """
    CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL
        )
    """

    #    cursor.execute(query)

    query = """
            CREATE TABLE IF NOT EXISTS device(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title TEXT NOT NULL UNIQUE,
                whole_price FLOAT CHECK (whole_price > 0),
                price FLOAT CHECK (price >= whole_price),
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES category(id)
            )
    """

    # cursor.execute(query)

    # insert_query = """
    #     INSERT INTO category (name)
    #     VALUES (?)
    # """

    # cursor.execute(insert_query, ['new_category'])

    insert_query_device = """
            INSERT INTO device (title, whole_price, price, category_id)
            VALUES (?, ?, ?, ?)
        """
    devices = [
        ("Samsung S23", 45000, 50000, 1),
        ("Serfing", 3000, 4000, 5),
    ]
    cursor.executemany(insert_query_device, devices)

    # query = """
    #     SELECT title, price, whole_price
    #     FROM device
    #     WHERE price > 5000
    #     LIMIT 2
    #     OFFSET 1
    # """
    # query = """
    #         SELECT title, price, whole_price
    #         FROM device
    #         WHERE (price > 5000 OR title = 'Serfing') and (title NOT LIKE '%Iphone 25%')
    #     """
    #
    # result = cursor.execute(query)
    # # pprint(result.fetchall(), indent=4)
    # pprint(result.fetchmany(size=200), indent=4)
