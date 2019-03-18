import psycopg2
from pymongo  import MongoClient
HOST = "localhost"
PORT = "5432"
PASSWORD = "password"
USER = "myprojectuser"
DB = "spillwater"



class DBManager:
    def connect(self):
        self.conn = MongoClient("mongodb://myproject:units123@ds163254.mlab.com:63254/units")
        self.cusor = self.conn.units
        return self.cusor
    def save(self, data, tablename=None):
        try:
            unit_id = self.cusor.waterspill.insert_one(data).inserted_id
            print(unit_id)
            return unit_id
        except (Exception, psycopg2.Error) as error:
            return error
        finally:
            if(self.conn):
                self.conn.close()
    def find_all(self):
        data = []
        try:
            for unit in self.cusor.waterspill.find({}):
                data.append(unit)
            return data
        except (Exception, psycopg2.Error) as error:
            return error
        finally:
            if(self.conn):
                self.conn.close()
        return
    def close(self):
        if(self.conn):
            self.conn.close()
    


    