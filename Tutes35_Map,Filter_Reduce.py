from functools import reduce
numbers = [2,3,5,6]
print("Original List : ", numbers)

#Done task in one line with map
print ("After Adding : ",list(map(lambda a : a+2 , numbers )))

#Filter

func = list(filter(lambda a : a>= 5 , numbers))
print(func) #Print all greater then equls 5 number

"""Reduce Function"""
"""Reduce is part of functool function"""
list = [1,2,3,4,5,6]
func = reduce(lambda a,b : a + b ,list )
print(func)

"""
* The reduce() method reduces the array to a single value.
* The reduce() method executes a provided function for each value of the array (from left-to-right).
* The return value of the function is stored in an accumulator (result/total).
* Note: reduce() does not execute the function for array elements without values.
"""

