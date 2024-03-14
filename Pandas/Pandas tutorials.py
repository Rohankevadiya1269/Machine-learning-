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

# Let's say if I need data from one column, so we will mention the column name
# from the above dataframe that contains name,age and qualification we need to print the data of age
print(datafrm2['Age'])
print()

# we can also create a data frame with list inside list

lst2 =[["Rohan",23,9.44],["Smit",22,9.60],["Om",21,9.50]] # inside the list the first arg is name, 2nd is age and 3rd is CGPA
datafrm3 = pd.DataFrame(lst2)
print(datafrm3)
print()

# we can create series with custom index name
print(pd.Series([10,11,12,13],index=['a','b','c','d']))
print()

# now we will create a data frame using multiple series
ser_ies = {'Name':pd.Series(["Rohan","Om","Smit","Navin"],index=[1,2,3,4]),'Age':pd.Series([23,22,22,21],index=[1,2,3,4])}
datafrm4= pd.DataFrame(ser_ies)
print(datafrm4)
print()
# we can also add one more data column to the above data frame which already contains name and age
# for example we need to add a column named salary
datafrm4['Salary']=pd.Series([12000,3000,2500,50000],index=[1,2,3,4])
print(datafrm4)
print()

# to know all the column names ⬇️
print(datafrm4.columns)
print()

# we can have slicing in columns
print(datafrm4.columns[1])
print(datafrm4.columns[0:2])
print(datafrm4.columns[:3])
print(datafrm4.columns[0:])
print(datafrm4.columns[::2])
print()

# this is to print all the values of the mentioned columns
print(datafrm4[datafrm4.columns[0:2]])
# this is to print all the values of the mentioned rows
print(datafrm4[0:3])
print()

# to print the desired row we have to do this
print(datafrm4.loc[2]) # this will print the data of the row 2 i.e of Om
print()

# to print the row similar to series we should do this
print(datafrm4.loc[[3]])
print()

# similar to row slicing we can do row slicing
print(datafrm4.loc[2:4])
print()

# when we don't know the row name we can access them using the index number that is called index location
print(datafrm4.iloc[[2]])
print(datafrm4.iloc[0:3])
print()

# to know the row values i.e row names
print(datafrm4.index.values)
print()

# from the entire set of data in datafrm4 i.e 4 names 4 ages and 4 salaries what if we need only 2 fields from each row and column
print(datafrm4.iloc[1:3,0:2]) # in the bracket the 1st argument which is slicing is for row and the 2nd argument after comma is for column
print()

# ------------

student_data = {"Student_id":[221,222,223,224,225],"First_name":["Ram","Tirth","Jai","Milan","Kishan"],"Last_name":["Sharma","Singh","Patel","Mishra","Banerjee"]}
stud_dtfrm= pd.DataFrame(student_data,columns=["Student_id","Last_name","First_name"]) # so this way I can customize the order of column as I want
print(stud_dtfrm)
print()

# Let us create another data frame that contains info about the courses of the students
course_details = {"stu_id":[221,222,223,224,225],"Course_name":["Machine Learning","Data Science","Computer science","Bsc.IT","BBA"],"Duration(Years)":[2,2,2,3,3]}
course_det = pd.DataFrame(course_details,columns = ["stu_id","Course_name","Duration(Years)"])
print(course_det)
print()

# now to join these two data frame we need to use merge method and there will be a need to define which are the columns based on we need to merge 
# so here we have student id. In student details data frame we have Student_id and in course details data frame we have stu_id
# so we need to mention that. Also the interpreter will merge only those data whose mentioned column details match 
#In this case student id

merged_data = pd.merge(stud_dtfrm,course_det,left_on = 'Student_id', right_on = 'stu_id', how = 'inner')
# the last argument is how whichh is the type of joint inner means the data will be shown which is common in both the data frames
# 2 type is left joint in which every detail from the data frame mentioned in left will be displayed and the corresponding data from the right data frame will be shown. 
# If there is no data in right dataframe corresponding to left data frame in this case it will show Nan 
# and vice versa for right joint 
# And if we need each and every data from both the data frames we will use outer joint

print(merged_data) # but in this case it will print student ids 2 times as it is mentioned in student details as well as course details
print()
# so to delete it we will drop one of the duplicate column by using the drop method
merged_data.drop(columns=["stu_id"], inplace= True)
print(merged_data)