# This is the numpy tutorials
# It is a python library that provides array objects 
# We can create arrays using numpy library


# This is single dimensional array
# it stores the data in single data type
import numpy as np
adv = np.array([[10,2,30]])
print(adv)
print()
# Here to store in single data type it has stored each element in string 
# Because string cannot be converted to int, but int can be converted to string
adv2 = np.array([10,55,'one'])
print(adv2)
print()
# we can also have boolean value inside array
adv3=np.array([11,45,True])
print(adv3)
print()
# here true and false will be stored in the form of 0 and 1 

# numpy also provides multi-dimensional array
adv4 = np.array([[10,20,30],[47,85,69]])
print(adv4)
print()
# In multi-dimensional array it is required that the number of rows should be consistent i.e the number of elements should be equal


# we can create an array using another array
a = np.array([14,1,16,18,91])
print(a)
b = a[1:4]
print(b)
print()

# if we make changes in b then it will also reflect in a 
b[2]=7777 # this will change the third element of b i.e 18 to 7777
print(b)
print()
# now if we print a the element 18 will also be changed there to 7777
print(a)
print()

# to resist the change we can use .copy() method

adv5 = np.array([10,20,60,40,50])
print(adv5)
adv6 = adv5[1:5].copy()
print(adv6)
# now even if we change an element in adv6 it will not be reflected in adv5
print()

adv6[3] = 444
# This will change 50 to 444
print(adv6)
print(adv5)
print()

