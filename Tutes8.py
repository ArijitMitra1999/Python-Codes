mystr = "harry is a good boy"
print(len(mystr)) #Finding Length of a string
print(mystr[::1]) #String Slicing using array
print(mystr[::-1]) #String start from last character to first character
#Type Casting
print("Type of mystr : ",type(mystr))
#Boolean data type
print(mystr.isalnum())
"""
isalnum() checks whether a string contains only letters or numbers or both.
isalnum() checks not take spaces so it's gives you error
"""
#endswith, startswith function
print(mystr.startswith("Harry"))
#count function
print("Count number of 'o' : ",mystr.count("o")) #It will count character or number like
#Capitalize function
print(mystr.capitalize()) # It will only capitalize first character of a string
#For full string upper case lower case
print("Full Upper Case : ",mystr.upper())
print("Full Lower Case : ",mystr.lower())
#Replace character or string
print("Replace a String or Character : ",mystr.replace("good","bad"))