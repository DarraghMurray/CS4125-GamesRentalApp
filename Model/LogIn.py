from DataLayer.DBConnection import databaseConnection as DC
import hashlib, binascii

class LogIn:
    
    def get_data(self,email):
        query = "SELECT * FROM users WHERE Email = %s"
        parameters = [email]
        return DC.executeSelectStatement(query, parameters)

    def verify_password(self, actualPass, enteredPass):
        salt = actualPass[:64]
        actualPass = actualPass[64:]
        hashPassword = hashlib.pbkdf2_hmac('sha512', 
                                    enteredPass.encode('utf-8'), 
                                    salt.encode('utf-8'), 
                                    100000)
        hashPassword = binascii.hexlify(hashPassword).decode('utf-8')
        return hashPassword == actualPass

    def sign_in(self,email, password) -> bool:
        user_info = self.get_data(email)
        if(len(user_info) > 0):
            UserID = user_info[0][0]
            UserEmail = user_info[0][1]
            UserPassword = user_info[0][2]
            UserName = user_info[0][3]
            UserType = user_info[0][4]
            UserBanStatus = user_info[0][5]

            if(UserBanStatus == 0):
                if(self.verify_password(UserPassword, password)):
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