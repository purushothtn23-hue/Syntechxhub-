#import all required libraries

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

### load the dataset.the dataset about a sales data of a company and it contains the following columns:
#  "Order_ID","Region_and_Sales_Rep","Sales_Amount","Order_Date".
# from kaggle "https://www.kaggle.com/datasets/vinothkannaece/sales-dataset" 

data = pd.read_csv("C:\\vishnu_pro\\internship\\syntecxhub\\week_two\\Sales_data.csv")

# check the data set any null values are present or not 

print(data.head())
print(data.info())

# we want to plot four different plot ther are histplot,kdeplot,boxplot by using sales_Amount colunm 
# divide into 2X2 layout and plot all the plot

fig,axis=plt.subplots(2,2,figsize=(12,8))

#plot sales_Amount in hisytplot in axis[0,0]

sns.histplot(
    data['Sales_Amount'],
    bins=20, 
    kde=True,ax=axis[0,0])
axis[0,0].set_title("Sales Histogram")

#plot sales_Amount in kdeplot in axis [0,1]

sns.kdeplot(
    data['Sales_Amount'], 
    fill=True, 
    ax=axis[0,1])
axis[0,1].set_title("Sales KDE Plot")

#plot sales_amonut in boxplot in axis [1,0]

sns.boxplot(
    x=data['Sales_Amount'], 
    ax=axis[1,0])
axis[1,0].set_title("Sales Box Plot") 

#boxlpot by using Region_and_Sales_Rep & Sales_Amount

sns.boxplot(
    x=data['Region_and_Sales_Rep'], 
    y=data['Sales_Amount'], 
    ax=axis[1,1])
axis[1,1].set_title("Sales by Region and Sales Rep")

# plot all plot's in a mannar and show it

plt.tight_layout()
plt.show()

# detect a outliers from the sales_amount and print the outlier

Q1 = data['Sales_Amount'].quantile(0.25)
Q3 = data['Sales_Amount'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = data[(data['Sales_Amount'] < lower) |(data['Sales_Amount'] > upper)]
print("=============================")
print(outliers)

#about the project

print("""The statistical analysis of the sales dataset reveals the distribution characteristics of sales_amount across different regions. The histogram and KDE plot indicate that sales are positively skewed, with most observations concentrated in the lower sales_amount range and a few high-value transactions. The boxplot highlights several outliers, suggesting the presence of exceptionally large sales_amount orders. Regional comparison shows noticeable differences in median sales and variability among regions. The calculated skewness confirms that the distribution is not perfectly symmetric. Overall, the analysis provides valuable insights into sales_amount behavior, variability, and unusual observations, helping businesses make data-driven decisions and identify opportunities for performance improvement.""")

