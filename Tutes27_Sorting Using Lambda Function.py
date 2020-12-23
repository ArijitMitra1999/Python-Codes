# def a_first(a) :
#     return a[1] # 1 is index of a every list
# a = [[2,23],[5,13],[4,17]]
# a.sort(key=a_first)
# print(a)

"""            """
"""    Using Lambda        """
a = [[2,23],[5,13],[4,17]]
a.sort(key= lambda a : a[1]) #Lambda is kind of a object so we need to store it
print(a)
