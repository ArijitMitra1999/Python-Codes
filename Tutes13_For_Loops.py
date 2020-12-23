list = [["Harry",56 ], ["Arijit",85],["Prayash",96],["Sayandeeep",83]]
dict1 = dict(list)
print(dict1)
for item,lollipop in dict1.items() :
    print(item,"Have",lollipop ,"Chocolates")
for item in dict1 :
    print(item)
"""Small Program"""
list=["Arijit",56,96,78,45,45,72,36,5,3,2,1,"Sayandeep"]
for item in list :
    if str(item).isnumeric() and item > 6:
        print(item)
