#Lists & List Function
Grocery = ("Harpic","Deodren","Bhindi","Soap","Chips",96)
print(Grocery)
print(Grocery[0])
#Soring
numbers = [23,65,96,78,54,12,3]
print(numbers) #Print the series without sorting
numbers.sort()
print("Sorted Numbers : ",numbers) #Print the series with sorting
"""Reverse numbers after sorting"""
numbers.reverse()
print("Reverse after sorting : ",numbers)

"""slicing"""
print(numbers[1:]) #It's don't take the number in 0 th position
print(numbers[0:4])#It's don't take the numbers after 3rd postion position (array starts with 0)
#Skip numbers from midddle like
print(numbers[::2])
""""[96, 78, 65, 54, 23, 12, 3] from this list it will print only [96, 65, 23, 3]"""
#Find Maximum and minimum number in a list
print("Maximum number of a list",max(numbers))
print("Minimum number of a list",min(numbers))
#Add anything in a new list at last position
number =[23,56,96,75,85]
print("New List: " , number)
number.append(78) #Add number in end of the list
print("After adding number : ",number)
#Add anything at any position
number.insert(0,56)
print(number)
#Concept of touple
tp = (1,2,3)
print(tp) #Tople is immutable that means we can not change touple
#For an example
#print(tp[1,8]) #It's gives error
"""Swapping two numbers in a easy way"""
a = 8
b = 1
print(a,b) # before swapping
a,b = b,a
print(a,b) # after swapping