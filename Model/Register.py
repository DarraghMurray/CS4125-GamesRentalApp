from DataLayer.DBConnection import databaseConnection as DC

class Register:

    def checkEmail(self, email):
        query = "SELECT * FROM users WHERE Email = %s"
        parameters = (email)
        result = DC.executeSelectStatement(query, parameters)
        if(len(result) == 0):
            return True
        else:
             return False

    def checkUserName(self, username):
        query = "SELECT * FROM users WHERE Username = %s"
        parameters = (username)
        result = DC.executeSelectStatement(query, parameters)
        if(len(result) == 0):
            return True
        else:
             return False

    def Registration(self, email, username, password):

        if(self.checkEmail(email)):
            #no existing entries of that email
                #need a way to hash passwords
                #no need for transaction this time as only one table inserted
                # query = "INSERT INTO users(Email, Username, Password) VALUES (%s,%s,%s)"
                # params = (email,username,password
                # DC.executeStatement())
            pass
        pass