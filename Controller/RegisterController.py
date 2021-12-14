from Model.Register import Register

#manages registration
class RegisterController:
    
    def register(self, email, username, password):
        self.Register = Register()
        self.Register.Registration(email, username, password)

    def verify_email(self, email) -> bool:
        return True

    def verify_username(self, username) -> bool:
        return True

    def verify_password(self, password) -> bool:
        return True