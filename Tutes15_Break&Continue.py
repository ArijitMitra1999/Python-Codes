i = 0
while (True) :
    if i+1 <5 :
        i= i +1
        continue
    print(i + 1, end=" ")
    if i==44 :
        i=i+1
        break
    i = i + 1

"""Small Program Regading While Loop"""
while(True) :
    user = int(input("Enter a Number (Greater than 100) : \n"))
    if user < 100 :
        print(user,"is smaller than 100\nSo try again")
        continue
    else :
        print("Congratulation!! ",user," is greater than 100")
        break;
