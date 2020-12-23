"""FAULTY  CALCULATOR"""
user = str(input("what do you want to do first : +,*,/"))
if user == "+" :
   n1 = int(input("enter the first number : "))
   n2 = int(input("enter the second number : "))
   if n1 == 57 and n2 == 9 :
       print("Sum is : 77")
   else :
       print("Sum is",n1 + n2)
elif user == "*" :
    n1 = int(input("enter the first number : "))
    n2 = int(input("enter the second number: "))
    if n1 == 45 and n2 == 3:
        print("Multiplication is : 555")
    else:
        print("Multiplication is", n1 * n2)
elif user == "/" :
    n1 = int(input("enter the first number : "))
    n2 = int(input("enter the second number : "))
    if n1 == 56 and n2 == 6:
        print("Division is : 4")
    else:
        print("Division", n1 / n2)