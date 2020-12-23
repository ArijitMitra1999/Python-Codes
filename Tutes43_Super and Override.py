class A :
    classvar1 = "I am a class A"
    def __init__(self):
        self.var1 = "I am inside a Class A"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
class B (A):
    classvar1 = "I am a class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside a Class B"
        self.classvar1 = "Instance var in class B"

a = A()
b = B()

print(b.special,b.var1,b.classvar1)
