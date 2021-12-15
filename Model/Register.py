from typing import Tuple
import os
import hashlib, binascii
from DataLayer.DBConnection import databaseConnection as DC

class Register:

    def checkEmail(self, email):
        query = "SELECT * FROM users WHERE Email = %s"
        parameters = [email]
        result = DC.executeSelectStatement(query, parameters)
        if(len(result) == 0):
            return True
        return False

    def checkUserName(self, username):
        query = "SELECT * FROM users WHERE Username = %s"
        parameters = [username]
        result = DC.executeSelectStatement(query, parameters)
        if(len(result) == 0):
            return True
        else:
             return False

    def hashPassword(self,password: str):

        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('utf-8')
        hashPass = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        hashPass = binascii.hexlify(hashPass)

        return (salt + hashPass).decode('utf-8')

    def Registration(self, email, username, password):
        if(self.checkEmail(email)):
            #no existing entries of that email
            if(self.checkUserName(username)):
                #no existing entries of that username
                registeredPassword = self.hashPassword(password)
                query = "INSERT INTO users(Email, Username, Password) VALUES (%s,%s,%s)"
                params = [email,username,registeredPassword]
                DC.executeStatement(query, params)
                return True
            else:
                return False
        else:
            return False