"""
abstraction -- hiding the implementation details of a class and only showing the essential features to the user

"""

# abstraction
class Car:
    def __init__(self):
        self.acc = False        # accelerator
        self.brk = False        # break
        self.clutch = False     # clutch

    def start(self):
        self.clutch = True
        self.acc = True         # here we hind the details for clutch and acc while printing, bcoz it was not needed to. And we only showed the printing statement
        print('CAR STARTED')
        # print(self.clutch, self.acc)      # uncomment this line and run this code


c1=Car()
c1.start()






