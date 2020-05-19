import sqlite3


def create_table() :
    conn=sqlite3.connect("giom_data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price) :
    conn=sqlite3.connect("giom_data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store values (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def update_data(item, quantity, price) :
    conn=sqlite3.connect("giom_data.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

def view_data() :
    conn=sqlite3.connect("giom_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    data = cur.fetchall()
    conn.close()
    return data

def delete_data(item) :
    conn=sqlite3.connect("giom_data.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,) )
    conn.commit()
    conn.close()

create_table
insert_data("red wine", 100, 10.0)
insert_data("white wine", 200, 8.0)
insert_data("cola", 250, 3.0)

for store_data in view_data() : 
    print(store_data)

print("Now deleting the Red Wines")
delete_data("red wine")
for store_data in view_data() : 
    print(store_data)

print("Now adding some White Wines")
update_data("white wine", 500, 8.0)
for store_data in view_data() : 
    print(store_data)


delete 
