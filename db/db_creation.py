# import sqlite3
#
# conn = sqlite3.connect('test_db_coffee.db')
# # cursor = conn.cursor()
#
# conn.execute("""CREATE TABLE IF NOT EXISTS sellers (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS managers (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS summary (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 seller_name_id INTEGER,
#                 number_of_sales INTEGER,
#                 total INTEGER,
#                 FOREIGN KEY (seller_name_id) REFERENCES sellers(id)
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS coffee (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 price INTEGER,
#                 currency_id INTEGER,
#                 FOREIGN KEY (currency_id) REFERENCES currency(id)
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS ingredients (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT
#                 )""")
#
# conn.execute("""CREATE TABLE IF NOT EXISTS currency (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT
#                 )""")
#
# conn.execute("""INSERT INTO sellers(name) VALUES ('Alex'), ('Bob'), ('Liza')""")
# conn.execute("""INSERT INTO managers(name) VALUES ('Jeff'), ('Scott'), ('Garry')""")
# conn.execute("""INSERT INTO summary(seller_name_id) VALUES (1), (2), (3)""")
# conn.execute("""INSERT INTO coffee(name, price, currency_id) VALUES ("Espresso", 3, 1), ("Latte", 4, 1), ("Cappuccino", 6, 1), ("Americano", 5, 1)""")
# conn.execute("""INSERT INTO ingredients(name) VALUES ("sugar"), ("cream"), ("cinnamon")""")
# conn.execute("""INSERT INTO currency(name) VALUES ("USD")""")
# # #  --------------------------------------------
# # # values = (1)
# #
# # # "INSERT INTO summary (number_of_sales) \
# # # SELECT number_of_sales\
# # #   FROM summary\
# # #  WHERE id=1"
# #
# # # cursor.execute('UPDATE details SET name = "latte" where id = 1')
# # # conn.commit()
# #
# #
# # # cursor.execute('drop table if exists summary')
# # # conn.execute("""CREATE TABLE details (
# # #                 id INTEGER PRIMARY KEY,
# # #                 seller_name TEXT,
# # #                 number_of_sales INTEGER,
# # #                 total_value INTEGER
# # #                 )""")
# #
# #
# # # conn.execute("""ALTER TABLE additional_beverage ADD COLUMN currency INT;""")
# #
# #
# # # conn.execute("""INSERT INTO additional_beverage VALUES (?)""", values)
# # # conn.execute("""INSERT INTO currency VALUES (?, ?)""", values)
# #
# # # r = conn.execute("""SELECT * FROM beverage_type""")
# # # r = conn.execute("""SHOW TABLES""")
# # # res = r.fetchall()
# # # print(res)
# #
# conn.commit()
# conn.close()
#
# ## console report
# # from tabulate import tabulate
# #
# # table = [["Sunfdgfdg dfg dfdfgdf",696000,1989100000],["Earth",6371,5973.6],
# #          ["Moon",1737,73.5],["Mars",3390,641.85]]
# # print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"], tablefmt="presto", numalign="left"))