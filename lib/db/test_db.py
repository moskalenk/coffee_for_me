import sqlite3

conn = sqlite3.connect('db_coffee_for_me.db')
# cursor = conn.cursor()

# conn.execute("""CREATE TABLE IF NOT EXISTS currency (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS salesman (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT
#                 )""")
# #
# conn.execute("""CREATE TABLE IF NOT EXISTS summary (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 seller_name_id INTEGER,
#                 number_of_sales INTEGER,
#                 total INTEGER,
#                 FOREIGN KEY (seller_name_id) REFERENCES salesman(id)
#                 )""")

# conn.execute("""CREATE TABLE IF NOT EXISTS coffee (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 price INTEGER,
#                 currency_id INTEGER,
#                 FOREIGN KEY (currency_id) REFERENCES currency(id)
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS ingredients (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 price INTEGER,
#                 currency_id INTEGER,
#                 FOREIGN KEY (currency_id) REFERENCES currency(id)
#                 )""")

# conn.execute("""INSERT INTO currency(id, name) VALUES (1, 'USD'), (2, 'BYN')""")
# conn.execute("""INSERT INTO salesman(id, name) VALUES (1, 'Alex'), (2, 'Bob'), (3, 'Liza')""")
# conn.execute("""INSERT INTO summary(seller_name_id) VALUES (1), (2), (3)""")
# noooo conn.execute("""INSERT INTO salesman(id, seller_name_id, number_of_sales, total) VALUES (1, 'Alex'), (2, 'Bob'), (3, 'Liza')""")
# conn.execute("""INSERT INTO coffee(id, name, price, currency_id) VALUES (1, "Espresso", 3, 1), (2, "Latte", 4, 1), (3, "Cappuccino", 6, 1), (4, "Americano", 5, 1)""")
# conn.execute("""INSERT INTO ingredients(id, name, price, currency_id) VALUES (1, "sugar", 1, 1), (2, "cream", 2, 1), (3, "cinnamon", 1, 1)""")
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
