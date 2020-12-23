class Student :
    no_of_lives = 8
    #Constructor
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def method1(self):
        return(f"Name is {self.name}, Salary is {self.salary}, Role is {self.role}")

Arijit = Student("Arijit",70000,"Engineer")
print(Arijit.method1())

# Harry = Student("")
# Rohan = Student()

# Harry.name = "Harry"
# Harry.salary = 10000
# Harry.role = "Doctor"
# print(Harry.method1())
#
# Rohan.name = "Rohan"
# Rohan.salary = 30000
# Rohan.role  = "Enginner"
#
# print(Rohan.method1())
