l = 10 #Global
def function2() :
    l = 5
    def function():
        global l
        l = 6
    function()
    print("For Function : ",l)

function2()
print("For Function 2 : ",l) #Global