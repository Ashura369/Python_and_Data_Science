class stds:
    def __init__(self, name, num, clas):
        self.name = name
        self.num = num
        self.clas = clas

    def __data(self):
        return f"Name of the student is {self.name}, with the roll numner {self.num}, from class {self.clas}"
    
    def call(self):
        return self.__data()


s1 = stds('Ravi', 23, '10th')
print(s1.call())

