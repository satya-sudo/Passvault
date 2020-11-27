import sqlite3
from PasswordHashing import checkPassword,hashPassword


# innitializing sqlite3 for python
conn=sqlite3.connect("data.db")
conn.execute("PRAGMA foreign_keys = 1")
cur=conn.cursor()


# create a database
def createdb():
    with conn:

        cur.execute('''CREATE TABLE IF NOT EXISTS User
        (CID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL)''')      

        cur.execute('''CREATE TABLE IF NOT EXISTS Password
        (ID INTEGER PRIMARY KEY,
        Sitename TEXT NOT NULL,
        Url TEXT NOT NULL,
        Password TEXT NOT NULL,
        CID             INT,
        FOREIGN KEY (CID) REFERENCES User (CID))''')

# calling it 
createdb()    

# user inputs functions


def checkAvaliableUsername(username):
    cur.execute('SELECT * FROM User WHERE username=:username',{'username':username})
    return False if cur.fetchone() else True
    

    

def createUser(username,password):

    hashpassword = hashPassword(password)
    with conn:
        cur.execute("INSERT INTO  User VALUES (null,?,?)",
        (username,hashpassword))
    cur.execute('SELECT * FROM User WHERE username=:username',{'username':username})
    return cur.fetchone()[0:2]
    

def createPassword(sitename,url,password,cid):
    with conn:
        cur.execute("INSERT INTO  Password VALUES (null,?,?,?,?)",
        (sitename,url,password,cid[0]))

def signInUser(username,password):
    cur.execute('SELECT * FROM User WHERE username=:username',{'username':username})
    gotUser = cur.fetchone()
    if gotUser == None:
        return None
    if checkPassword(password,gotUser[2]):
        print(gotUser)
        return gotUser[0:2]
    else:
        return  None    

def passwordFinder(sitename,cid):
    cur.execute('SELECT * FROM Password WHERE sitename=:sitename AND CID=:CID',{'sitename':sitename,'CID':cid[0]})
    passwords = [row[1:4] for row in cur.fetchall()]
    return passwords


def  fitchAllPassword(cid):
    cur.execute('SELECT * FROM Password WHERE CID=:CID',{'CID':cid[0]}) 
    allPassword = [ row[1:4] for row in cur.fetchall()]
    return allPassword
