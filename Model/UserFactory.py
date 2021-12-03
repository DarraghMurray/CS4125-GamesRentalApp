from abc import ABC, abstractmethod
from User import User
from AdminUser import AdminUser
from RegularUser import RegularUser
from SubscribedUser import SubscribedUser
#might scrap idea
class UserFactory(ABC):
    def createPizza(UserTypeID):
        
        user = None

        if (UserTypeID == 1) :
            user = AdminUser()
        elif (UserTypeID == 2):
            user = RegularUser()
        elif (UserTypeID == 3):
            user = SubscribedUser()

        return user
    
