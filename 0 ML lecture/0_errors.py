import sys
from _0_dbhelper import DBhelper

class Facebook:
    def __init__(self):
        # connect to the data base
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
            1. Enter 1 to register
            2. Enter 2 to login
            3. Anything else to leave
                           
""")

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)


    def register(self):
        name = input('ENTER THE NAME : ')
        email = input('ENTER THE E-MAIL : ')
        password = input('ENTER THE PASSWORD : ')

        response = self.db.register(name, email, password)

        if response:
            print("REGISTRATION SUCCESSFUL")
        else:
            print("REGISTRATION FAILED")

        self.menu()

    def login(self):
        # Placeholder for login logic
        print("LOGIN FUNCTIONALITY NOT IMPLEMENTED YET")
        self.menu()

# **********************************************************************************************************************************************

obj = Facebook()

# AFTER SUCCESSFULLY ADDING A NEW USER, IT WILL ADD THAT USER'S DETAILS INTO THE DATABASE AT 'phpMyAdmin'

