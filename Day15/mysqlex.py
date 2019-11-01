import mysql.connector
#pip install mysql-connector-python

class Database:

	def __init__(self,db):
		self.conn = mysql.connector.connect(host="localhost",user="root",passwd="",database=db)
		
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS tblbook (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER,isbn INTEGER)")
		self.conn.commit()

	def insert_data(self,id,title,author,year,isbn):
		self.cur.execute("INSERT INTO tblbook(id,title,author,year,isbn) VALUES(%s,%s,%s,%s,%s)",(id,title,author,year,isbn,))		
		self.conn.commit()
        
	def show_data(self):

		self.cur.execute("SELECT * FROM tblbook")
		rows = self.cur.fetchall()
		return rows

	def search_data(self,title="",author="",year="",isbn=""):

		self.cur.execute("SELECT * FROM tblbook WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title,author,year,isbn))
		rows = self.cur.fetchall()
		return rows

	def delete_data(self,id):
		self.cur.execute("DELETE FROM tblbook WHERE id=%s",(id,))
		self.conn.commit()
        
	def update_data(self,id,title,author,year,isbn):
		self.cur.execute("UPDATE tblbook SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title,author,year,isbn,id))
		self.conn.commit()
        
	def __del__(self):
		self.conn.close()
		
#db = Database("mypydb") #Creating Class Object
#db.insert_data(1,"The Sun","Nazmul",1999,1001)
#db.insert_data(2,"The Best","Saiful",2000,1002)
#db.insert_data(3,"Test","Munaz",2001,1003)
#db.update_data(2,"The Sun moon","Nazmul",1999,1001)
#print(db.show_data())
#print(db.search_data(author="Munaz"))	






