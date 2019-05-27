import sqlite3


def main():

    conn = sqlite3.connect("db_coffee_for_me.db")

    conn.execute("""CREATE TABLE IF NOT EXISTS sellers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS managers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS summary (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    seller_name_id INTEGER,
                    number_of_sales INTEGER,
                    total INTEGER,
                    FOREIGN KEY (seller_name_id) REFERENCES sellers(id)
                    )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS coffee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER,
                currency_id INTEGER,
                FOREIGN KEY (currency_id) REFERENCES currency(id)
                )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS currency (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )""")

    conn.execute("""INSERT INTO sellers(name) VALUES ('Alex'), ('Bob'), ('Liza')""")
    conn.execute("""INSERT INTO managers(name) VALUES ('Jeff'), ('Scott'), ('Garry')""")
    conn.execute("""INSERT INTO summary(seller_name_id) VALUES (1), (2), (3)""")
    conn.execute("""INSERT INTO coffee(name, price, currency_id) VALUES ("Espresso", 3, 1), ("Latte", 4, 1), ("Cappuccino", 6, 1), ("Americano", 5, 1)""")
    conn.execute("""INSERT INTO ingredients(name) VALUES ("sugar"), ("cream"), ("cinnamon")""")
    conn.execute("""INSERT INTO currency(name) VALUES ("USD")""")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
