# import pandas 
import pandas as pd

###  load a data set for perfoming a basic data analysis using pandas library
#  in python. from kaggle:"https://www.kaggle.com/datasets/zeeshier/student-information-dataset"

data=pd.read_csv("students.csv")
print("___________________________________________________")

# print first 5 rows in the data set

print("first 5 rows of the student dataset are:")
print (data.head())

# print last 5 rows in the data set

print("___________________________________________________")
print ("last 5 rows of the student dataset are:")
print(data.tail())

# print entier data in a dataset

print("___________________________________________________")
print("The student dataset is")
print(data)

# get info about the dataset
#  like number of rows, columns, data types, memory usage etc

print("___________________________________________________")
print ("Info of student dataset is ")
print(data.info())

### find the data type of the dataset like wich column is int, float, object etc

print("___________________________________________________")
print("show the data type of the dataset")
print(data.dtypes)

### to perform a statistical operation 
# to find the mean, median, mode, standard deviation of the gpa column in the dataset

print("___________________________________________________")
print("show the description of the dataset")
print(data.describe())

### to perform a filtering operation 
# to find students with gpa less than 3.5 and slice the dataset 
# to show only name, age and gpa of the students 

f_gpa=data[data["GPA"]<3.5]
print("___________________________________________________")
print ("the students with gpa less than 3.5 are:")
print(f_gpa)
# perform a slicing operation to show only name, age and gpa  from the dataset
print("___________________________________________________")
print(data[["Name", "Age", "GPA"]])

### to save the filtered data to a new csv file for students with gpa less than 3.5

print("___________________________________________________")
f_gpa.to_csv("students_gpa_less_than_3.5.csv", index=False)