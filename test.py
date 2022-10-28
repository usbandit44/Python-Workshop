import imp


import math
from math import pi # to import pi for the math class and only get pi

print("hello", "world")

myVariable = 2 
print(myVariable, type(myVariable))
mtFloat = 2.69 #float is double or decimal

piValue = math.pi

print(piValue)

rootNum = math.sqrt(9)
exponent = 3 ** 2 #calcuate 3 to the power 2

print(exponent)

#if  1 == myVariable:
#    print("1")
#elif 2 == myFloat:
 #   print("2")
#else:
 #   print("no")

my_list = [1, 2, 3, 4, True, "happy"] #list can hold any data type together
print(my_list[2])
print(len(my_list))
my_list.append("scream")#add to list
my_list.insert(2, "co0l")#inserting to list 
print(my_list)

del my_list[1]#remove from list can use my_list.remove[1]
print(my_list)
