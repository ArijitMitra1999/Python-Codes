"""Dictinoary"""
d1 ={}
print(type(d1))
d2 = {"Harry" : "Burger" , "Rohan" : "Fish" , "Prayash" : "Roti"}
print(d2["Harry"]) #Key value pair (Case Sensative)
#How we can add other dictionary
d2["Ankit"] = "Junk Food"
print("Updated Dictionary : ",d2)
#Remove from Dictionary
del d2["Ankit"]
print("After Deletion",d2)

"""Functions of Dictionary"""
#Copy Function
d3 = d2.copy() # .copy function copied totally from raw string like before update a string
print(d3)
#Update in library
d2.update({"Ankit" : "Biriyani"}) #we use 3rd Braces in it
print(d2)
#We can print keys and items
print("Keys present in dictionary : ",d2.keys())
print("Items present in dictionary : ",d2.items())