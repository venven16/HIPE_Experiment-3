#Importing the library needed 
import pandas as pd 


#Loading the cvs file given to us 
cars = pd.read_csv('cars.csv')

# Display the first five rows
print("First five rows:")
cars.head()

# Display the first five rows
print("Last five rows:")
cars.tail()