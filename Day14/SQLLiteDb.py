import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tblbook (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER,isbn INTEGER)")
        self.conn.commit()

    def insert_data(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO tblbook VALUES(null,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        
    def show_data(self):

        self.cur.execute("SELECT * FROM tblbook")
        rows = self.cur.fetchall()
        return rows

    def search_data(self,title="",author="",year="",isbn=""):

        self.cur.execute("SELECT * FROM tblbook WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()

        return rows

    def delete_data(self,id):
        self.cur.execute("DELETE FROM tblbook WHERE id=?",(id,))
        self.conn.commit()
        
    def update_data(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE tblbook SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
		
db = Database("dbBook1.db") #Creating Class Object
	
db.insert_data("The Sun","Nazmul",1999,1001)
db.insert_data("The Best","Saiful",2000,1002)
db.insert_data("Test","Munaz",2001,1003)

db.update_data(2,"The Sun moon","Nazmul",1999,1001)

print(db.show_data())

print(db.search_data(author="Munaz"))	






