from Model.LogIn import LogIn

#manages log-in
class LogInController:
    
    def LogIn(self, email, password):
        self.logIn = LogIn()
        print(email)
        print(password)
        self.logIn.sign_in(email, password)