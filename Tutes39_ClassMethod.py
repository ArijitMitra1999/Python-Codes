class arijit :
    no_of_gf = 2
    def __init__(self):
        self.name = "Sundori"
        self.anothername = "Kuschit"
    @classmethod
    #I can call this one with instance even with class too
    def classmethod(cls,new_no_of_gf):
        cls.no_of_gf = new_no_of_gf
c1 = arijit()
print(c1.name)
#classmethod
c1.new_no_of_gf = 9
print(c1.new_no_of_gf) #Calling with instance
"""That is how class method works"""
