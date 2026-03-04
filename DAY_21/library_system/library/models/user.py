from library.models.admin import Admin
class Authservices:
    def __init__(self):
        self.admin= admin("admin","1234")
    def login(self,username,password):
        return username == self.admin.username and
    password == self.admin.password
