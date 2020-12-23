f = open("Harry2.txt")
print(f.tell()) #Searching File Pointer
print(f.readline())
print(f.tell())
f.seek(10)
print(f.readline())
f.close()
"""
The tell() method returns the current file position in a file stream. 
Tip: You can change the current file position with the seek() method.
"""