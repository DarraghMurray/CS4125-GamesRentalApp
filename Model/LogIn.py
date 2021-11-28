from DataLayer.DBConnection import databaseConnection as DC
import hashlib, binascii

class LogIn:
    
    def GetData(self,email):
        query = "SELECT * FROM users WHERE Email = %s"
        parameters = [email]
        return DC.executeSelectStatement(query, parameters)

    def VerifyPassword(self, actualPass, enteredPass):
        salt = actualPass[:64]
        actualPass = actualPass[64:]
        hashPassword = hashlib.pbkdf2_hmac('sha512', 
                                    enteredPass.encode('utf-8'), 
                                    salt.encode('utf-8'), 
                                    100000)
        hashPassword = binascii.hexlify(hashPassword).decode('utf-8')
        return hashPassword == actualPass

    def SignIn(self,email, password) -> bool:
        UserInfo = self.GetData(email)
        if(len(UserInfo) > 0):
            UserID = UserInfo[0][0]
            UserEmail = UserInfo[0][1]
            UserPassword = UserInfo[0][2]
            UserName = UserInfo[0][3]
            UserType = UserInfo[0][4]
            UserBanStatus = UserInfo[0][5]

            if(UserBanStatus == 0):
                if(self.VerifyPassword(UserPassword, password)):
                    print("signed in")
                    return True
                else:
                    print ("failpass")
                    return False
            else:
                print ("failban")
                return False
        else:
            print ("failnoACC")
            return False