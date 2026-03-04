"""
#ENCAPSULATION

class snapchat:
    def __init__(self, username, password, friends):   
        self.username = username
        self.__password = password
        self._friends = friends
        
    def getpassword(self):
        return self.__password

    def setpassword(self, new_password):
        self.__password = new_password
        
    @property
    def oprfriends(self):
        return  self._friends
        
    @oprfriends.setter
    def oprfriends(self,newfriend):
        self._friends.append(newfriend)
        
    
        
saaketh = snapchat("saaketh", "12345", ["praveen", "nikhil"])

print(f"Name before modification: {saaketh.username}")
saaketh.username = "shannu"
print(f"Name after modification: {saaketh.username}")
print(f"Password before modification: {saaketh.getpassword()}")
saaketh.setpassword("S@123")
print(f"Password after modification: {saaketh.getpassword()}")
print(f"friends before modifaction:{saaketh.oprfriends}")
saaketh.oprfriends='shannu'
print(f"friends after modification:{saaketh.oprfriends}" )

"""






from abc import ABC,abstractmethod  #ABC=Abstract Base Class
class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")
        
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited deposit")
    def withdraw(self):
        print("unlimited withdraw")
        
class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")
    def withdraw(self):
        print("1-2 lakhs per day you can withdraw")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20t-1L per day")
        
class PensionAccount(BankAccount):
    def deposit(self):
        print("no deposit")
    def withdraw(self):
        print("40t per day")
        
print("---abhinandhan---")
abhinandhan= SavingAccount()
abhinandhan.checkbalance()
abhinandhan.deposit()
abhinandhan.withdraw()

print("---praveen---")
praveen=CurrentAccount()
praveen.checkbalance()
praveen.deposit()
praveen.withdraw()

print("---saaketh_nikhil---")
saaketh_nikhil=JointAccount()
saaketh_nikhil.checkbalance()
saaketh_nikhil.deposit()
saaketh_nikhil.withdraw()

print("---shanmukh---")
shanmukh=SalaryAccount()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.withdraw()

print("---swapnil---")
swapnil=PensionAccount()
swapnil.checkbalance()
swapnil.deposit()
swapnil.withdraw()

































