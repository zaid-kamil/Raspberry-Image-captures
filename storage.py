from sqlite3 import connect
from datetime import datetime

class Database:

    path = "imageDB.sqlite3"
    table = "captures"
    
    def __init__(self):
        self.con = connect(self.path)
        print('connected')

    def run(self,query,params=()):
        try:
            self.con.execute(query,params)
            print("create table captures")
            return True
        except Exception as e:
            print("error",e)
            return False



    def create_table(self):
        query = """CREATE TABLE captures (id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT, created_at TIMESTAMP)"""
        self.run(query)
    
    def add(self,path):
        now = datetime.now()
        query ="INSERT INTO captures(null,?,?)"
        params = (path,now)
        self.run(query,params)
        
    def view(self):
        query = "SELECT * FROM captures"
        try:
            result = self.con.execute(query)
            if result:
                return result.fetchall()
            else:
                return None
        except Exception as e:
            print(e)
            return None
        
        