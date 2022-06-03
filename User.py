class User():
    def __init__(self,namee=None):
        self.namee = namee
        
    def get_register(self, user_name, mail, password, repeatpass):
        self.user_name = user_name 
        self.mail = mail
        self.password = password
        self.repeatpass = repeatpass
        print("-----------------------------------User-----------------------------------")
        print()
        if password != repeatpass:
            print("Passwords must be same!")
        else:
            print("You registered")
            print()
            
    def login(self,l_name,l_mail,l_pass,):
        self.l_name = l_name
        self.l_mail = l_mail
        self.l_pass = l_pass
        if self.l_name != self.user_name or self.l_mail != self.mail or self.l_pass != self.password:
            print("Your information are wrong")
        else:
            print("You successfuly login")
            print()
            print("You must be consumer or purchaser")
            print()


    




        

