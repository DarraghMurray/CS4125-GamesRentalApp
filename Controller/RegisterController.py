from Model.Register import Register

#manages registration
class RegisterController:
    
    def Register(self, email, username, password):
        self.Register = Register()
        self.Register.Registration(email, username, password)