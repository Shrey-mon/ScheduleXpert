import mysql.connector
class connection:
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost", user="root", password="swadesh@1408",database="scheduler")
    def getConnection(self):
        return self.conn