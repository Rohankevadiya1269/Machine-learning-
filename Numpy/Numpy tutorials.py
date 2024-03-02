# This is the numpy tutorials
# It is a python library that provides array objects 
# We can create arrays using numpy library
# numpy arrays are same as matrices in Mathematics

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

# an element in array is represented as A(0,0), A(0,1) where the number on the left reprents row and the number on the right reprents column
# which can also be seen as A(row,column)

# In numpy too we can use the range function to create an array
# but here the keyword is arange

arng = np.arange(9) # this will create one dimensional array from 0 to 5
print(arng)
# we can also specify the starting and ending point of the range just as python range
arng1 = np.arange(10,20)
print(arng1) # here an array will be created starting from 10 to 20
print()

# so this range function has only one row and column, but what if we need multi-dimensional array
# in this case we use reshape function
# Initially we need to create a range array and then reshape it in the form of 2x2, 3x3 and so on matrices
# If the array we create is of 4 elements then we have to reshape it into 2x2 matrix 
# so we can use reshape as per the number of elements in arange function

rshp = arng.reshape(3,3) # this 2,2, is rows and columns 
print(rshp)
# It is required to mention number of rows and columns
# It is not compulsory in the reshape function that the number of rows and columns should be equal
# we can also create 2x3, 5x2, 2x5, etc any sort of matrix
# for example see the next illustration
print()

rshp2 = arng1.reshape(2,5)
print(rshp2)
rshp2 = arng1.reshape(5,2)
print(rshp2)
print()
# we can also create a 3 dimensional array using this reshape function
# for example lets take a 1d array with 30 numbers from 0 to 29 and use the reshape function
# by using the normal reshape we can create a 2d array of either 2,6,5,3 rows and same number of columns
# but we can also create a 3d array

a = np.arange(30)
print(a)
# now we can reshape a as a.reshape(5,6) or (6,5) or (3,10) or (10,3) or (2,15) or (15,2)
 # but this will only create one 2d array 
 # if we want 2 different arrays we can do :
b=a.reshape(2,5,3) # the 1st arg is no of array and the next args is no of column and row
print(b)
print()
# Now if we need to create an array with any sort of dimension but all the elements must be zero, then we use .zero function
z=np.zeros((3,3)) # we can create the zeros array of any dimension
print(z)
print()

# same case goes with one , if we need all the values of the array as 1 then we could use .ones method
o=np.ones((3,4))
print(o)
print()

# we only have 0 and 1 as the standard function, but what if we need to array of all elements other than 0 or 1
# lets say if I want all elements of the array as 7 , so there is no dedicated function called .sevens that will create an array of all elements 7
# so instead of having a direct method we will use ones array and multiply it with 7
s = np.ones((4,4)) *7
print(s)
print()

a= np.arange(30)
b=np.reshape(a,(6,5),'F' ) # 'F' stands for Fortran order which is column wise contiguous, this will arrange the elements of array column wise
c=np.reshape(a,(6,5),'C' ) # 'C' stands for C order which is default order, it will arrange the elements of array row wise
print(b) # in simple words here the number will increase one below another in column
print()
print(c) # and here number will increase sidewards i.e row wise 
print()
# We can also create a Transpose of a matrix or array
# Transpose means that the rows and columns gets interchanged
transpose_arr  = b.T
print(transpose_arr)
print()

# We can also perform arithmatic operation on matrix / array such as add, subtract, multiply, division
# let's create 2 different arrays to see the operations

arr_1=np.arange(1,10)
arr_1r = arr_1.reshape(3,3)

arr_2=np.arange(5,14)
arr_2r = arr_2.reshape(3,3)
print(arr_1r)
print("--------")
print(arr_2r)
print()
# So now that we have created two 2d arrays, let's have a look at operations
# 1--> Addition

a = arr_1r+arr_2r
print("----- Addition of two arrays is : \n",a)
print()

#2--> Subtraction
s= arr_2r-arr_1r
print("---- Subtraction of two arrays is: \n",s)
print()

#3--> Multiplication
m=arr_1r*arr_2r
print("---- Multiplication of two arrays is: \n", m)
print()

# but this is not proper matrix multiplication, it is simply multiplying element to element
# but in real matrix multiplication each row is multiplied by  simultaneous column and added to get an element
# so to do the matrix multiplication we use @ symbol instead of *

m_m = arr_1r@arr_2r
print(m_m)
print()

# 4--> Division
d = arr_1r/arr_2r
print("---- Division of two arrays is : \n",d)
print()

# we can also find the quotient and the remainder of the matrix division
# by using floor division and module

f_d = arr_1r//arr_2r # This will return the quotient
print("--- quotient using floor division : \n",f_d)
print()

r = arr_1r%arr_2r # This will return the remainder
print("--- remainder : \n", r)
print()