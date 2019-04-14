import sqlite3 as sql
def connect(): #connect to database#
    """Connect to the database"""
    conn = sql.connect("books.db",timeout=10)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY,Title TEXT,Author TEXT, Year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn): #add entry#
    """Add items to the database"""
    conn = sql.connect("books.db",timeout=10)
    cur = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view_all(): #view all#
    """Views the current entries"""
    conn = sql.connect("books.db",timeout=10)
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows #returns list#

def update_selected():
    """To pick an entry from the frontend"""
    conn = sql.connect("books.db",timeout=10)
    cur = conn.cursor()
    cur.execute("UPDATE bookstore SET ")
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    """Searches for an entry in the database"""
    conn = sql.connect("books.db",timeout=10)
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE Title = ? or Author = ? or Year = ? or ISBN = ?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete_entry(id):
    """Deletes entry from the database"""
    conn = sql.connect("books.db",timeout=10)
    cur=conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id = ? ",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    """Updates an entry from the database"""
    conn = sql.connect("books.db",timeout=10)
    cur=conn.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect() # to create a database if there is none
