import sqlite3

# define connection and cursor

connection = sqlite3.connect('transaction_store.db')

# cursor is used to interact with the database

cursor = connection.cursor()

# create stores table

store = """CREATE TABLE IF NOT EXISTS
store(storeID INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(store)

# create purchases table

purchases = """CREATE TABLE IF NOT EXISTS
purchases(purchaseID INTEGER PRIMARY KEY, storeID INTEGER, totalCost FLOAT,
FOREIGN KEY(storeID) REFERENCES store(storeID))"""

cursor.execute(purchases)

# add to stores

cursor.execute("INSERT INTO store VALUES (21, 'Manila, Philippines')")
cursor.execute("INSERT INTO store VALUES (22, 'Pangasinan, Philippines')")

# add to purchases

cursor.execute("INSERT INTO purchases VALUES (1, 21, 600.76)")
cursor.execute("INSERT INTO purchases VALUES (34, 22, 700.87)")

# get results

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()

print(results)