# Display the first five rows with odd-numbered columns
odd_columns = cars.iloc[:, ::2]

print("First five rows with odd-numbered columns:")
odd_columns.head()

# Display the row that contains the ‘Model’ of ‘Mazda RX4’
cars.loc[cars['Model'] == 'Mazda RX4']

cars = pd.read_csv('cars.csv')
cars 

# Display how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have
cars.loc[[23],['Model', 'cyl']]

# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
cars.loc[[1, 28, 18],['Model', 'cyl', 'gear']]