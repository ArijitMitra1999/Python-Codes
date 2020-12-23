"""Set Theory"""
s = set()
print(type(s))
s = set([5,6,4,8,7])
print(type(s))
s.add(1)
s.add(2) #Set can not take unique value
s.add(2)
s.remove(5) #Remove function
print(s) #In set Compiler gives you the sorted answer
s1 = s.union((1,2,3)) #Union makes new set
print(s,s1)
s1 = s.intersection((1,2,3))
print("After Intersection it will gives you the common part of s and s1 : ",s,s1)

"""A set Disjoined or not"""
s = {1,2,3,4}
s1 = {6,8,7,9}
print(s.isdisjoint(s1)) #It is disjoined so gives you true value