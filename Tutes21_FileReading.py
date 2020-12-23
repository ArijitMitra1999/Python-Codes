#Read file as Harry.txt
f = open("Harry.txt","r+")
print(f.readlines())
# content = f.read()
# print(content)
"""Read line by line"""
# for line in f :
#     print(line,end="")

f.close()