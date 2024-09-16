# HIPE_Experiment 3 -  PYTHON DATA ANALYSIS (PANDAS)

This repository contains Python codes for solving the given programming problems for this experiment. Full details of each solution using Python are included in this repository.

### Intended Learning Outcomes 
#### 1. To determine which functions and codes are part of the Pandas library
#### 2. Applying and utilizing the many codes and functions to build a Python program with the Pandas library

#### Instruction: 
#### - In the Jupyter Notebook, write a Python script or code to solve the provided issues. Your Jupyter notebook can be turned in in the designated submission bin.

#### - Download and save the following file to your default user folder for this programming assignment: bit.ly/Cars_file  

## Problem 1 
### Library: import pandas as pd 

Description: Python's 'import pandas as pd' command brings in the Pandas library, an effective resource for working with and analyzing data. The library receives the alias pd from the as pd portion, which is shorter and easier to utilize in your code. This common approach facilitates efficient access to Pandas methods (such as DataFrame creation).

![image](https://github.com/user-attachments/assets/45c1fdc7-3476-4471-a18b-5226518d6021)

### Function: cars = pd.read_csv('cars.csv') 

Description: Reading data from a CSV file called "cars.csv" and loading it into a Pandas DataFrame is done with the function 'cars = pd.read_csv('cars.csv')'. With its table-format organization and easy manipulation and analysis features, the DataFrame organizes the data in the variable cars. Users use the read_csv() method to import CSV files into Pandas. 

![image](https://github.com/user-attachments/assets/03be1f0b-fc20-41aa-9a50-1ba93d43e6c6)

### Function: cars.head() 

Description: By default, Pandas' cars.head() function shows the first five rows of the DataFrame cars. It offers an overview of the data, which helps examine the DataFrame's composition and structure. If necessary, a different number of rows can be chosen to be viewed.

![image](https://github.com/user-attachments/assets/ee866d7c-43bf-42a9-b9b7-358ac3232b4d)

### Fucntion: cars.tail()

Description: By default, Pandas' cars.head() function shows the last five rows of the DataFrame cars. It offers an overview of the data, which helps examine the DataFrame's composition and structure. If necessary, a different number of rows can be chosen to be viewed. 

![image](https://github.com/user-attachments/assets/fbce7dce-9a08-4a72-a935-131fc8110dc4)

## Problem 2 
### Function: odd_columns = cars.iloc[:, ::2] and odd_columns.head()

Description: A new DataFrame odd_columns is created by selecting every second column (beginning with the first) from the DataFrame cars with the code odd_columns = cars.iloc[:, ::2]. Odd_columns.head() shows the first five rows of this new DataFrame, displaying just the odd-numbered columns. The print("First five rows with odd-numbered columns:") line gives context.

![image](https://github.com/user-attachments/assets/e445c7e6-c058-4c7a-bc7d-bf4c242932d0)


### Function: cars.loc[cars['Model'] == 'Mazda RX4'] 

Description: The DataFrame cars are filtered by the code cars.loc[cars['Model'] == 'Mazda RX4'] to only display the rows where the Model column contains the value 'Mazda RX4'. These rows are selected using a Boolean mask, and then they are returned in a new DataFrame. 

![image](https://github.com/user-attachments/assets/fea48d97-8495-4ece-8958-6bc9235f8234) 

### Function: cars.loc[[23],['Model', 'cyl']] 

Description: The DataFrame cars contain a row with index 23, which the code cars select.loc[[23], ['Model', 'cyl']] to extract only the Model and cyl columns for that row. It retrieves certain data utilizing label-based indexing. Index 23 contains the car model 'Camaro Z28'. 

![image](https://github.com/user-attachments/assets/ccf28ba6-5281-4808-aabc-b02ec005a75a)

### Function: cars.loc[[1, 28, 18],['Model', 'cyl', 'gear']] 

Description: Only the Model, cyl, and gear columns for the rows with indices 1, 28, and 18 are retrieved from the DataFrame cars using the code cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]. Indexes 1, 28, and 18 contain these car models: ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic.’ 

![image](https://github.com/user-attachments/assets/472d79c9-fbac-4cbc-b7dc-a1571af8fce0)











