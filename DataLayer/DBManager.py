import mysql.connector
from mysql.connector import cursor
from mysql.connector.cursor import MySQLCursorPrepared

from DataLayer.config import Config

class DBManager:
    def __init__(self):
        try:
            self.__db = mysql.connector.connect(user=Config.DATABASE_CONFIG['user'],password=Config.DATABASE_CONFIG['password'],host=Config.DATABASE_CONFIG['host'],db=Config.DATABASE_CONFIG['dbName'])
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            self.__db = False
            

    def executeStatement(self, query, params):
        try:
            cursor = self.__db.cursor(prepared=True)

            cursor.execute(query,params)
            cursor.close()
            self.__db.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def executeSelectStatement(self, query, params):
        try:
            cursor = self.__db.cursor(prepared=True)

            cursor.execute(query,params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return None

    