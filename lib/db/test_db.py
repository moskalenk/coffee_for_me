import sqlite3

conn = sqlite3.connect('test_db_cofee.db')
# cursor = conn.cursor()

conn.execute("""CREATE TABLE IF NOT EXISTS salesman (
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
                FOREIGN KEY (seller_name_id) REFERENCES salesman(id)
                )""")

conn.execute("""CREATE TABLE IF NOT EXISTS coffee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price_in_USD INTEGER
                )""")

conn.execute("""CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
                )""")

# conn.execute("""INSERT INTO salesman(name) VALUES ('Alex'), ('Bob'), ('Liza')""")
# conn.execute("""INSERT INTO managers(name) VALUES ('Jeff'), ('Scott'), ('Garry')""")
# conn.execute("""INSERT INTO summary(seller_name_id) VALUES (1), (2), (3)""")
conn.execute("""INSERT INTO coffee(name, price_in_USD) VALUES ("Espresso", 3), ("Latte", 4), ("Cappuccino", 6), ("Americano", 5)""")
conn.execute("""INSERT INTO ingredients(name) VALUES ("sugar"), ("cream"), ("cinnamon")""")
#  --------------------------------------------
# values = (1)

# "INSERT INTO summary (number_of_sales) \
# SELECT number_of_sales\
#   FROM summary\
#  WHERE id=1"

# cursor.execute('UPDATE details SET name = "latte" where id = 1')
# conn.commit()


# cursor.execute('drop table if exists summary')
# conn.execute("""CREATE TABLE details (
#                 id INTEGER PRIMARY KEY,
#                 seller_name TEXT,
#                 number_of_sales INTEGER,
#                 total_value INTEGER
#                 )""")


# conn.execute("""ALTER TABLE additional_beverage ADD COLUMN currency INT;""")


# conn.execute("""INSERT INTO additional_beverage VALUES (?)""", values)
# conn.execute("""INSERT INTO currency VALUES (?, ?)""", values)

# r = conn.execute("""SELECT * FROM beverage_type""")
# r = conn.execute("""SHOW TABLES""")
# res = r.fetchall()
# print(res)

conn.commit()
conn.close()
