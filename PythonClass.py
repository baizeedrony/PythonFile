class user:
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input("enter your email:")
        password = input("enter your password:")

        if email == self.email and password == self.password:
            login = True
            print("login success")
        else:
            print("login failed")


    def logout(self):
        login = False
        print("Logged Out")

    def isLoggedin(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
       if isLoggedin():
           print(self.name, "\n",self.email)

       else:
           print("user is not loggedin")


user1 = user("Rony", "rony@gmail.com", "123456")




user1.login()
user1.profile()
