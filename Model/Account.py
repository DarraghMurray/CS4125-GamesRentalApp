class Account:
    def __init__(self, usertype):
        self.__usertype = usertype

    def get_user_type(self):
        return self.__usertype

    def change_user_type(self, usertype):
        self.__usertype = usertype