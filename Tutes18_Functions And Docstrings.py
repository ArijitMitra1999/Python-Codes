#Built in Function
a = 9
b = 8
c = sum((a,b))
print(c)
#User Defined Function
def function(a,b) :
    print("Hello!", a+b)
function(2,3)
def function2(a,b) :
    """This is User Defined Function"""
    average =(a+b)/2
    print(average)
    return average
v = function2(3,5)
print(v)
print(function2.__doc__) #Doc String 