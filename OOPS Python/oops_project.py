import sys
class Chatbook:

    __user_id = 0

    def __init__(self):
        self.id = Chatbook.__user_id
        Chatbook.__user_id += 1
        self.__name ="Default user"
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    # getter
    def get_name(self):
        return self.__name

        # setter
    def set_name(self,value):
        self.__name= value

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?

        1. Press 1 to signup
        2. Press 2 to signin
        3. Press 3 to write a post
        4. Press 4 to message a friend
        5. Press any other key to exit

        """)

        if user_input == "1":
            self.signup()

        elif user_input == "2":
            self.signin()

        elif user_input == "3":
            self.my_post()

        elif user_input == "4":
            self.sendmsg()

        else:
            sys.exit()

    def signup(self):
        email = input("Enter your email here..")
        pwd = input("Setup your password here..")

        self.username = email
        self.password = pwd

        print("You have signed up successfully!!")
        print("\n")

        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the menu")

        else:
            uname = input("Enter your email/username here..")
            pwd = input("Enter your password here..")

            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!!")
                self.loggedin = True

            else:
                print("Please input correct credentials")

        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin:
            txt = input("Enter your message here..")
            print(f"Following content has been posted: {txt}")

        else:
            print("You need to signin first to post something..")

        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin:
            txt = input("Enter your message here..")
            frnd = input("Whom to send the msg? ")

            print(f"Your message has been sent to {frnd}")

        else:
            print("You need to signin first to send a message..")

        print("\n")
        self.menu()


obj = Chatbook()

