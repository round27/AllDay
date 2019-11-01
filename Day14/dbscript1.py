import sqlite3

def create_table():
    conn = sqlite3.connect("myDb1.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert_data(item,qty,price):
    conn = sqlite3.connect("myDb1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()

def show_data():
    conn = sqlite3.connect("myDb1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()

    conn.close()
    return rows

def delete_data(item):
    conn = sqlite3.connect("myDb1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update_data(item,pr):
    conn = sqlite3.connect("myDb1.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price=? WHERE item=?",(pr,item))
    conn.commit()
    conn.close()

create_table()
#insert_data("Coke",100,25.0)
#insert_data("Pepsi",10,20.0)
#insert_data("Fanta",80,22.0)

delete_data("Pepsi")
update_data("Fanta",111.0)
print(show_data())
