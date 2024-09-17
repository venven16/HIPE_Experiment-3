#Importing the library needed 
import pandas as pd 


#Loading the cvs file given to us 
cars = pd.read_csv('cars.csv')

# Display the first five rows
print("First five rows:")
cars.head()

# Display the first 16 rows
print("First 16 rows:")
cars.head(16)

# Display the last five rows
print("Last five rows:")
cars.tail()

# Display the last 16 rows
print("Last 16 rows:")
cars.tail(16)
