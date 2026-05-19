from users import Users
class Priv:
    def __init__ (self, privileges=["can add post","can delete post","can ban user"]):
        self.privileges=privileges
    def show_privileges (self):
        print (f"the admin can do the following: {self.privileges}")
   
class Admin (Users):
    def __init__ (self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilege=Priv()