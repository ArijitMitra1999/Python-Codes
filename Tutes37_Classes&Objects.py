class Student :
    no_of_lives = 8
    pass

Harry = Student()
Rohan = Student()

Harry.name = "Harry"
Harry.salary = 10000
Harry.role = "Doctor"

Rohan.name = "Rohan"
Rohan.salary = 30000
Rohan.role  = "Enginner"
print(Harry.__dict__)
print(Student.no_of_lives)
Rohan.no_of_lives = 9
print(Rohan.__dict__)



