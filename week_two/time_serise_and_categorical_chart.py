<<<<<<< HEAD
# importing the required libraries to perform time series and categoricol chart analysis

import pandas as pd
import matplotlib.pyplot as plt

### load a dataset for performing time series analysis and categorical chart analysis
# and from kaggle "https://www.kaggle.com/datasets/ahmedadam415/digital-currency-time-series"

data=pd.read_csv("C:\\vishnu_pro\\internship\\syntecxhub\\week_two\\dc.csv")
print(data)

#fill the missing colunm name "unnamed:0 to Periode" by using a rename function 

data.rename(columns={"Unnamed: 0":"Period"},inplace=True)   

# concert the period column to datetime format 

print(data)
data["Period"]=pd.to_datetime(data["Period"])

# group the data by data/month  and sum the low USD for each month

monthly_low_USD=data.groupby(data["Period"].dt.month)["low_USD"].sum()
print("this is the revenu by month",monthly_low_USD)

# plot the data by time periode in line and how the low USD changes by month
#give a title,x label and y label to the plot 

plt.plot(monthly_low_USD)
plt.title("Low USD by month")
plt.xlabel("Month")
plt.ylabel("Low USD")
plt.show()

# save the plot as a png file of the monthly low USD by month

plt.savefig("low_usd_by_month.png")
=======
# importing the required libraries to perform time series and categoricol chart analysis

import pandas as pd
import matplotlib.pyplot as plt

### load a dataset for performing time series analysis and categorical chart analysis
# and from kaggle "https://www.kaggle.com/datasets/ahmedadam415/digital-currency-time-series"

data=pd.read_csv("C:\\vishnu_pro\\internship\\syntecxhub\\week_two\\dc.csv")
print(data)

#fill the missing colunm name "unnamed:0 to Periode" by using a rename function 

data.rename(columns={"Unnamed: 0":"Period"},inplace=True)   

# concert the period column to datetime format 

print(data)
data["Period"]=pd.to_datetime(data["Period"])

# group the data by data/month  and sum the low USD for each month

monthly_low_USD=data.groupby(data["Period"].dt.month)["low_USD"].sum()
print("this is the revenu by month",monthly_low_USD)

# plot the data by time periode in line and how the low USD changes by month
#give a title,x label and y label to the plot 

plt.plot(monthly_low_USD)
plt.title("Low USD by month")
plt.xlabel("Month")
plt.ylabel("Low USD")
plt.show()

# save the plot as a png file of the monthly low USD by month

plt.savefig("low_usd_by_month.png")
>>>>>>> ae7076278cf7faa498c220a0223a4ec94df988fe
