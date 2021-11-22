from DataLayer.DBConnection import databaseConnection as DC

class LogIn:
    
    def GetData(self,email):
        query = "SELECT * FROM users WHERE Email = %s"
        parameters = (email)
        return DC.executeSelectStatement(query, parameters)

    def SignIn(self,email, password):
        UserInfo = self.GetData(email)
        if(UserInfo > 0):
            #check if banned
                #verify password
            pass
        else:
            pass

    def VerifyPassword():
        pass