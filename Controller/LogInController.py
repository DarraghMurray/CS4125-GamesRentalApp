from Model.LogIn import LogIn
#from View.LogInUI import LogInUI

#manages log-in
class LogInController:
    
    def LogIn(self, email, password):
        self.logIn = LogIn()
        print(email)
        print(password)
        self.logIn.SignIn(email, password)