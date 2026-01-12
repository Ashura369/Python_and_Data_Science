import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='0_new_database')
            self.mycursor = self.conn.cursor()
        except:
            print('EROOR : NOT CONNECTED TO THE DATABASE')
        else:
            print('SUCCESSFULLY CONNECTED TO THE DATABSE') 