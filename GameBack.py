#backend
import sqlite3

def GameData():
    con=sqlite3.connect("Game1.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Game_ID text,Game_Name text,Release_Year text,Developer text,Genre text,Platform text,Mode text,Rating text)")
    con.commit()
    con.close()
    
def AddGameRec(Game_ID,Game_Name,Release_Year,Developer,Genre,Platform,Mode,Rating):
    con=sqlite3.connect("Game1.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", (Game_ID,Game_Name,Release_Year,Developer,Genre,Platform,Mode,Rating))
    con.commit()
    con.close()

def ViewGameData():
    con=sqlite3.connect("Game1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteGameRec(id):    
    con=sqlite3.connect("Game1.db")    
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  

def SearchGameData(Game_ID="",Game_Name="",Release_Year="",Developer="",Genre="",Platform="",Mode="",Rating=""):  
    con=sqlite3.connect("Game1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE Game_ID=? OR Game_Name=? OR Release_Year=? OR Developer=? OR Genre=? OR Platform=? OR Mode=? OR Rating=?",(Game_ID,Game_Name,Release_Year,Developer,Genre,Platform,Mode,Rating))
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateGameData(id,Game_ID="",Game_Name="",Release_Year="",Developer="",Genre="",Platform="",Mode="",Rating=""):
    con=sqlite3.connect("Game1.db")    
    cur=con.cursor()
    cur.execute("UPDATE book " "SET Game_ID=?","Game_Name=?","Release_Year=?","Developer=?","Genre=?","Platform=?","Mode=?","Rating=?"," WHERE id=?",(Game_ID,Game_Name,Release_Year,Developer,Genre,Platform,Mode,Rating))
    con.commit()
    con.close()

GameData()
