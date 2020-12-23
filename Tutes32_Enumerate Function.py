
l1 = ["Arijit","Prayash","Sayandeep"]
# i = 1
# for item in l1 :
#     if i % 2 is not 0 :
#         print(f"please buy {item}")
#     i += 1
"""Enumerate"""
print("Index with list : ",list(enumerate(l1)))
for index,item in enumerate (l1) :
        if index % 2 == 0 : print(f"{item} please buy  ")



