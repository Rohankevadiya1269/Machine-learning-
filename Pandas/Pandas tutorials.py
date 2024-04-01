import pandas as pd
import numpy as np
import os
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
print()

# Now we will read the data from the csv file that we have converted from an excel file
# for that there is a command that is read

rd = pd.read_csv("C:\\Users\\kevad\\Downloads\\Personal_Shortlist(1).csv")  #  There is also an option to read csv, excel, html and various other files
print(rd)
print()
# now this file contains 20 rows and if I need to show the top 5 rows then,..

print(rd.head())
print()
# but what if we do not want 5 rows every time, in case we need 3 rows or maybe 7 rows then?
# then we will use head command as --> rd.head(3) if we want 3 rows or rd.head(7) if we need 7 rows

# to print the last 5, we will use tail,.. 
print(rd.tail())
print()

# we can also know the no. of rows and columns
print(rd.shape)
print()

# If we only want to know the number of rows then we will use the command len(rd)
# If we want to know the columns details
print(rd.columns)
print()

# we can change the name of the column
rd.columns = ['col/uni','Ilts','city','app fee','fee','schlrshp','remarks']
print(rd.head(2))
print()

# we can also create new column and do mathematical operation in it. let us try
list = rd.tail()
print(f'--->{list}')
print()
list['total_fee']=list['fee']+list["fee"]
print(list)
print()

# we can filter the output as per our needs, like if we need the colleges whose fees is less than 20,000
# then we can do this --> print(list.fees<20000)
# we can also put multi filter inside it using and/or statement
# for example --> print(list.fee<20000 & list.scholarship>7500)

# for or statement -->print(list.fee<20000 | list.scholarship>7500)
# we can filter the output using == sign as well 
print("----->")
nl = rd[(rd.Ilts =='6.5')]
print(nl)
print()


tips=pd.read_csv("C:/Users/kevad/Downloads/Tips_rate_example.csv")
print(tips)
print()
# to find the desired valued column we can find it with dataframe-name.contains,case=False,na=False(na=flase means no null values)
desired_tip=tips[tips['Country_Name'].str.contains('Af',case=False,na=False)] 
print(desired_tip)
print()
# We can also use dataframe_name.startswith,na=false to search for the desired element 
desired_tip1=tips[tips['Country_Name'].str.startswith('Af',na=False)] 
print(desired_tip1)
print()
# we can find the unique value by using the command ------->    dataframe_name.column_name.unique 
print(tips.Income_group.unique())
print()
# To know the current working directory/folder we can use os library

# If we need to print only specific columns then we can do it 
print(tips[['Country_Name', 'Tip_rate','Income_group']].head(7))
print("--------^")
# we are interested in the top 5 data from the column then we use head(5), but what if from that 5 data we need only top 2
# then we will have loc [1:2] after head (5) 1 and 2 are the starting and ending point 
print(tips.head(5).loc[1:2])
# it returns true or false based on the if the value of the columns of the row is NaN/ null or not
print(tips.Country_code.isna())
print()
# other property is group by ()
# consider that the tips csv file has various income groups, now we will find how many groups are there 
print(tips.groupby('Income_group').size())
print()
# we can also know that how many groups are there and in that group how much data is there using other method than size
# that is count()
print(tips.groupby('Income_group').count())
print()

# here we are trying to find the average tip rate for each income group and for that we are using the aggregate(agg) method
# as well as numpy's mean method
print(tips.groupby('Income_group').agg({'Tip_rate':np.mean,'Income_group':np.size}))
print()
# we can also do the sum instead of finding mean 
print(tips.groupby('Income_group').agg({'Tip_rate':np.sum,'Income_group':np.size}))
print()

print(tips.groupby('Income_group').agg({'Tip_rate':[np.size,np.mean,np.sum,np.min,np.max]}))
print()

# We can delete records as per conditions
new_tip = tips.drop(12) # there are 13 columns and we have to delete the column number 12 which is of norway country
print(new_tip)
print()

tips=tips.drop(0)
print(tips)
print()
# we can get various info about the data
# lets consider we want data which consists High Income 
print(tips[tips['Income_group']=='High Income'])
print()
# there are 2 same income groups by mistakely
# High income and High Income --> the difference is only capital and small I
# so we can delete the data where Income_group is High income
print('--------**')
# to know the index of the the data we need, we use index method
print(tips[tips['Income_group']=='High income'].index)
print()
# drop method need index to delete the data 
# so that was the reason we knew how to know the index
print(tips)
print()
tips = tips.drop(tips[tips['Income_group']=='High income'].index)
# As we can see here the index 6 which was of High income of country --> England was deleted from the table
print(tips)
print()
# Now we will know about the sorting 
# by this we have sorted values by internet user in the increasing order
tips_sorted = tips.sort_values(by=['Internet_user'])
print(tips_sorted)
print()
# Here we have sorted the data by the increasing (ascending) order of the tip rate 
print(tips.sort_values(by=['Tip_rate']))  # Here we can have multiple columns name for sorting

print()
# what if we need data in descending order ?
print(tips.sort_values(by=['Tip_rate'], ascending=False))
print()
# we can convert the data type of the data 
# example of the code is : tips['Tip_rate']=tips['Tip_rate'].astype('int')
tips['Tip_rate']=tips['Tip_rate'].astype('int')
print(tips)
print(".....")

# we can also check the data using the info method
# It will return all the information like how many columns are there,what are the names of the columns
# how many data types are present, how much memory is consumed in bytes
print(tips.info())




print()
print(os.getcwd())
# to change the current working directory we need to use the command chdir
# we will write the code --> os.chdir('path')  

# now if we dont have to write the whole path for reading the csv file then we can change the directory to current working directory
# and then we just have to write the file name

# for example if I change the working directory to (C:\Users\kevad\Downloads), then to read the csv file I just need 
# to mention the file name that is Personal_Shortlist(1).csv