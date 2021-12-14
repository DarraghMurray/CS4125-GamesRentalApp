#manages user access
class UserControl:

    def __init__(self, user, account):
        self.__user = user
        self.__account = account

    def get_user_type(self):
        return self.__account