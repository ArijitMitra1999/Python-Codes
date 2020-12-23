"""
var1 = 32
var2 = 56
var3 = int(input()) #String can be str

if var3>var2 : #Use : this sign means run the if statemant
    print("Var3 is greater than Var2")
elif var3==var2 : #It is short form of else if
    print("Var3 is equals to Var2")
else :
    print("Var3 is Less than Var2")
"""
"""Condition Check from a List"""
List = [5,6,3,8]
if 5 in List :
    print("it is in list : ",List)
if 15 not in List :
    print("It is not in list : ",List)

"""Driving License"""
print("What is your Age ?")
age = int(input())
if age>18 :
    print("You are eligble for driving license")
elif age==18 :
    print("Okay Your driving license is in processing")
else :
    print("You are not eligible")

