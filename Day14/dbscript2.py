import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert_data(item,qty,price):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,qty,price))
    conn.commit()
    conn.close()

def show_data():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()

    conn.close()
    return rows

def delete_data(item):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update_data(item,pr):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price=%s WHERE item=%s",(pr,item))
    conn.commit()
    conn.close()

create_table()
insert_data("Coke",100,25.0)
insert_data("Pepsi",10,20.0)
insert_data("Fanta",80,22.0)

delete_data("Pepsi")
update_data("Fanta",111.0)
print(show_data())
