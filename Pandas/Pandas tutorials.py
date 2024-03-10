import pandas as pd
# Pandas also have capacity of storing data in various dimensions such as one and two
# the one dimensional data storing structure is called --- SERIES 
# In numpy where in 1-d array the data is stored in row, here in series which is 1-d: data is stored in column
# The two dimensional data storing structure is called ----- DATA FRAME
# In numpy where the rows and columns are recongnized on the basis of index number
# In pandas it gives liberty to name the column and row whatever we feel like 


# In numpy the entire array should contain only single or one data type 
# But in pandas the data frame can contain mutiple data type in different columns
# but there is one compulsion that a column should have only one type of data 

# let's create a one dimensional data structure of pandas called series

series = pd.Series([54,36,18,48])
print(series) # this will display elements in columns along with its index and data type
print()

# We can also convert an array into series
import numpy
array = numpy.array([1,3,5,6,7,8])
print(array)
print()
ser_ies = pd.Series(array)
print(ser_ies)

# we can also have slicing 
print(ser_ies[3:])
print()
print(ser_ies[:4])
print()
print(ser_ies[::2])
print()

# when we print the series we get index number infront of series elements, so if want to get names infront of elements
# we can have dictionary and then convert it into series
dict_1 ={"Emp_1":"Riddham","Emp_2":"Harshal","Emp_3":"Navin","Emp_4":"Pratik"}
ser =pd.Series(dict_1)
print(ser)
print()
# We can also access the elements of the series using the key name
# Like we need to access the emp_2 to emp_4 we will use slicing just as index slicing 
# We can also change the element

print(ser['Emp_2':'Emp_4'])
print()

ser['Emp_2']= "Rohan"
print(ser)
print()
# Now let's see data frame

list1 = [12,33,43,556,42,761]
datafrm = pd.DataFrame(list1)
print(datafrm)
print()

# for multi-dimensional dataframe we need to create a list of dictionaries
lst = [{'Name':'Rohan','Age':'23','Qualification':'B.Tech CE'},{'Name':'Om','Age':'21','Qualification':'B.Tech IT'},
       {'Name':'Navin','Age':'21','Qualification':'B.Tech CE'},{'Name':'Smit','Age':'22','Qualification':'B.Tech IT'}]
dtfrm = pd.DataFrame(lst)
print(dtfrm)
print()
# but creating multiple dictionaries inside the list is the lengthy process
# so instead of creating dictionaries inside list, we will create a list inside dictionary

data2 = {"Name":["Rohan","Om","Smit","Dhruvik","Jenil"],"Age":[23,21,22,21,22],"Qualification":["B.Tech CE","B.Tech IT","B.Tech IT","B.Tech CE","B.Tech CE"]}
datafrm2 = pd.DataFrame(data2)
print(datafrm2)
print()