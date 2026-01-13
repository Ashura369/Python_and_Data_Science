class persons:
    college = 'Nirmalya'

    def __init__(self, name, age, location): # this is a constructor    # self -> this object
        self.name = name
        self.age = age
        self.location = location
        # print(f"The person's name is {name}, he is about {age} year old, and he is from {location}. Studying at college {persons.college}") 
    
    def print_data(self):
        print(f"""
            name        : {self.name}
            age         : {self.age}
            location    : {self.location}
""")
    
    def welcome(self):      # instance method
        print('WELCOME TO THE WORLD OF HEROS')


    # type 1
    def relationship1(self):
        print(f'Both {p1.name} and {p2.name} are getting married soon')

    # type 2
    def relationship2(self, other):
        print(f'Both {self.name} and {other.name} are couples')

# ************************************************************************************************************************************************

name = 'Biswajeet Pradhan'
age = 25
location = 'India'

p1 = persons(name, age, location)
# p2 = persons(name, interest, goal)

'''METHODS'''

p2 = persons('Aisha Sinha', 26, 'UK')

# welcome()     [in py you cant just call welcome method as you used to do in java, in py the methods must be called after an object]
p1.welcome()    # [here welcome is being called within the p1 object]
p1.print_data()
p2.print_data()

p2.relationship2(p1)
p1.relationship1()


