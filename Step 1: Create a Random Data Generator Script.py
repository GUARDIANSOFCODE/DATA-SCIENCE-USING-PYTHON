import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)  # For reproducibility

num_records = 1000

# Data Generation
countries = ['Country_A', 'Country_B', 'Country_C', 'Country_D']
cities = ['City_X', 'City_Y', 'City_Z', 'City_W']
capital = ['Capital_A', 'Capital_B', 'Capital_C', 'Capital_D']
employee_names = [f"Employee_{i}" for i in range(1, num_records + 1)]
ages = np.random.randint(18, 65, num_records)  # Random ages between 18 and 65
population_density = np.random.randint(50, 500, num_records)  # Density per sq. km
wages = np.random.randint(20000, 120000, num_records)  # Random annual wages
medicare = np.random.choice(['Yes', 'No'], num_records)  # Medicare eligibility

# Creating a DataFrame
data = {
    'Country': np.random.choice(countries, num_records),
    'City': np.random.choice(cities, num_records),
    'Capital': np.random.choice(capital, num_records),
    'Employee_Name': employee_names,
    'Age': ages,
    'Population_Density': population_density,
    'Wages': wages,
    'Medicare_Eligibility': medicare
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('country_data.csv', index=False)
print("CSV file 'country_data.csv' generated successfully!")
