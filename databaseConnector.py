import sqlite3
import os

'''
Provide interface for database to store or retrieve items
'''

class MyDatabase():
    CONNECTIONS = []
    def __init__(self):
        # will store single connection!
        # sqlite atm
        self.connect()

    def connect(self):
        if len(self.CONNECTIONS) == 0 :
            conn = sqlite3.connect('items.db')
            self.cursor = conn.cursor()
            self.CONNECTIONS.append(self.cursor)
            return self.cursor
        else:
            self.cursor = self.CONNECTIONS[0]
            return self.cursor

    def get_dict_db(self):
        #  will return dict from database with products
        pass

    def create_storage(self, number:int):
        #  will create storage for user item and store it note
        pass

    def get_storage(self, number:int):
        #  will get user storage
        pass

if __name__ == '__main__':
    mydb = MyDatabase()
