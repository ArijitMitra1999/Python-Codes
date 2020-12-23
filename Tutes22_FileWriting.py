# f = open("Harry2.txt","w") #f = file Handle
# a = f.write("Harry is good\n")
# #f.write function return number of character
# print(a)
# f.close()

"""Handle read and Write"""
f = open("Harry2.txt","r+") #r+ = read + write
f.read()
f.write("Thank you")
f.close()