# import require library
#  
import numpy as np

#create a sample dataset for perform a  numpy operation

data=np.array([21,54,65,21,35,54])

#perfom a indeexing & sliceing

print(f"The value of position 3: {data[2]}")
print(f"The values between 54-54 is {data[2:-2]}")

# next perform a numerical and statestical operation
#  
print(f"the value after mean{np.mean(data)}")
print(f"the max value of data{np.max(data)}")
print(f"the min value of data{np.min(data)}")
print(f"the sum value of data is {np.sum(data)}")

# to perform a resape and brodcating

s_data= np.reshape(3,1)
print(f"convert one dimentoin to two dimention {s_data}")

# perfom a save and load operation

np.save("data.npy",data)
l_data=np.load("data.npy")
print(l_data)
