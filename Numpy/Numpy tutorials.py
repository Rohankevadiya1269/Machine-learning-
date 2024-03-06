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

# We can convert multi dimensional array into a single dimensional array

a = np.arange(30)
b=a.reshape(3,5,2)
print(b)
print()
# So now we have multidimensional array and to convert it again to a single dimensional array we use ravel function
c=b.ravel()
print(c)
print()
# We can also use another method called flatten
d = b.flatten()
print(d)
print()

# We can also have linear space between the starting and ending point of the array
# for example start is 20 and end is 40 and in between I want 4 intervals so by using linspace it will have elements -->
# 20 24 28 32 36 40  ---> so here we will get the four elements as 24 28 32 36 as we needed a linear or equal space between elements so it has got the increment by 4

vector = np.linspace(10,20,7) # here the first argument is starting point and the second argument is ending point and the third argument is the intervals
print(vector)
print()
# as we needed equal space between each element of the array the numbers are in decimals

# Now let us do some exercise 
# consider the sales record over 3 regions asia europe and pacific
# each region has sales record for 4 quarters for the year and has one dimensional array
Asia_sales = [1002, 4523, 4123 , 3584]
Europe_sales= [7854, 9654, 4582, 8543]
Pacific_sales = [7845, 4512, 3652, 7452]

# Now we will create one multi dimensional array from the above all one dimensional array
Total_sales = np.array([Asia_sales,Europe_sales,Pacific_sales])
print(Total_sales)
print()
# output will be 
'''
[[1002 4523 4123 3584]
 [7854 9654 4582 8543]  # But what if we need to access the third element of this second row 
 [7845 4512 3652 7452]]
'''
# --------  SLICING ---------- 
# as we know that there are 3 rows and 4 columns and the numbering starts from 0 same as index
# so to access the third element of second row we will use indexing
custom = Total_sales[1][2]  # the number one represents second row which is the 1st argument and the number two is 2nd argument which represents the column
print(custom)    # this should print 4582
print()

# but to access the sales record we need to remember the row and column, but what if there numberous rows and columns 
# Let us consider that we need to access the record of third quarter of the Europe_sales
# Now we will create a dictionary that consists the index no. of the regions and quarters so that it becomes easy to access the slicing element
region = {"Asia_sales":0,"Europe_sales":1,"Pacific_sales":2} # This is dictionary of regions and their respective indices
quarter ={"Q1":0,"Q2":1,"Q3":2,"Q4":3}
# Now we will slice the element using the region name and quarter number

cus_sales = Total_sales[region["Europe_sales"]][quarter["Q3"]]
# this should print 4582
print(cus_sales)
print()

# Array slicing :
# This is same as List and string slicing in python

ran_ge = np.arange(1,101)
print(ran_ge)
print()

# We can slice the elements as we want 
# case 1: For example we need the first 15 characters
print(ran_ge[:15])
print()
# Case 2: For example we need to access all the elements starting from 69 to end
print(ran_ge[68:])
print()

# Case 3: For example we need to access all the elements from 47 to 85
print(ran_ge[46:85])
print()

# case 4: For example we need to access the elements with and increment
print(ran_ge[::10]) # this will print the array elements with an increment of 10
print()

'''
[0 1 2]
[3 4 5]
[6 7 8]
'''
# consider this is my array and I want to extract :
'''
[4 5]
[7 8]
'''
# this can be done by specfying the row and column to print, but here too we will do slicing
arr_S = np.arange(9)
a = arr_S.reshape(3,3)
# print(a)
cus = a[1:,1:]  # In above example of sales we saw that we can access the elements of array using the specification of row and column
# But in that specification we can also have slicing 
# The 1st argument is for the row where we have specified that print from row 2nd till end
# and then after comma we have done the same for column
print(cus)
print()

# We can know the information about the array 
# to know the shape or the number of rows and columns of the matrix we use shape function
print(a.shape)

# to know the dimension of the matrix we use ndim function
print(a.ndim)


# to know that how much memory does the array requires we use the itemsize function
print(a.itemsize)
print()

# We can also know the datatype of the array using dtype function
print(a.dtype)
# it will return int 32 int i.e intergers and 32 that is 4 byte of info because if we divide 32 by 8 bits then we get 4

# to know the size or the number of elements of the array we use size function
print(a.size)

# We can also find out the minimum and maximum value of the array
print(a.min())
print(a.max())

# to know about all the commands of the numpy we can use dir function
print(dir(np))
print()

# sum function will return the sum of all the elements of the array
print(a.sum())

# there are also commands like sqrt(array name) to return the square root of the individual elements or the array
# also there is a command called std(array name) to return standard deviation of the array

# lets consider that we have to create an empty array then we will use empty function
b= np.empty((3,3),dtype=int)
c= np.empty((3,3),dtype=float)
d= np.empty((3,3),dtype=bool)
e= np.empty((3,3),dtype=str)
print(b)
print(c)
print(d)
print(e)

print()