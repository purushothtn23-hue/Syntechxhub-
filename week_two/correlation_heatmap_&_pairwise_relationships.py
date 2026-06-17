# import required package

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# load a dataset from kaggle"https://www.kaggle.com/datasets/mrsimple07/car-prices-prediction-data"

data=pd.read_csv("C:\\vishnu_pro\\internship\\syntecxhub\\week_two\\CarPricesPrediction.csv")

print(data.head())
print(data.info())
data.rename(columns={"Unnamed: 0":"S.no"},inplace=True)

# create a new dataset from the dataset with a only numerical values

num_col=data.select_dtypes(include=np.number)
print(num_col)

#create a correlation matrix

corr_matrix = num_col.corr()

print(corr_matrix)

# pair plot for num_col

sns.pairplot(
    num_col,
)
plt.title("Pari plot of num_col")
plt.show()

# heatmap for correlation

sns.heatmap(
    corr_matrix,
    annot=True,  
)
plt.title("heatmap for correlation")
plt.show()

# scatterplot for find a relation between year and price

sns.scatterplot(
    x='Year',
    y='Price',
    data=data,
)
plt.title("scatterplot of mileage vs Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

# to find a strong correlation of the dataset

corr_pairs = corr_matrix.unstack()

corr_pairs = corr_pairs.sort_values(
    ascending=False
)

print(corr_pairs)

# print a highest correlation and low correlation

print("The highest correlation is 'price & year'\n The lowest correlation is 'price and mileage' ")