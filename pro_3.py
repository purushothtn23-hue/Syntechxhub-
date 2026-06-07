import pandas as pd
# load a dataset with a missing value and its get 
# from"https://www.kaggle.com/datasets/himelsarder/retail-product-dataset-with-missing-values" 
data=pd.read_csv("synthetic_dataset.csv")
print(data)
# drop the missing values without handling missing values,
# get a clear concept of the missing values and get a clear 
#  knowelege about the missing values and save with sample variable
f_data=data.dropna(inplace=False)
print("the data after dropping the missing values without handling missing values")
print (f_data)
# fill the missing values with mean for numerical columns and mode for categorical columns
data["Price"]=data["Price"].fillna(data["Price"].mean())
data["Rating"]=data["Rating"].fillna(data["Rating"].mean())
data["Discount"]=data["Discount"].fillna(data["Discount"].mean())
data["Category"] = data["Category"].fillna(data["Category"].mode()[0])
data["Stock"] = data["Stock"].fillna(data["Stock"].mode()[0])
print("the data after filling the missing values")
print(data)
# check the missing values after filling the missing values
print(data.isna().sum())
# drop the missing values after filling the missing values
print("the data after dropping the missing values")
print(data.dropna().sum())
# remove the duplicate values from the dataset and store with a temporary variable
dd_data=data.drop_duplicates(inplace=False)
print("the data after removing duplicate values")
print(dd_data)
### to save a file after handling the missing values and 
# removing the duplicate values in a new csv file
dd_data.to_csv("cleaned_synthetic_dataset.csv", index=False)
d=pd.DataFrame(dd_data)

