import pandas as pd

# Step 1: Define the data for 150 countries
countries = [
    'USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'China', 'Brazil', 
    'South Africa', 'Japan', 'South Korea', 'Italy', 'Spain', 'Russia', 'Mexico', 
    'Netherlands', 'Sweden', 'Norway', 'Argentina', 'Saudi Arabia', 'Turkey', 'Switzerland', 
    'Belgium', 'Austria', 'Denmark', 'Finland', 'Ireland', 'Portugal', 'Czech Republic', 
    'Greece', 'Hungary', 'Poland', 'Romania', 'Israel', 'Singapore', 'Malaysia', 'Indonesia', 
    'Thailand', 'Vietnam', 'Philippines', 'Nigeria', 'Kenya', 'Colombia', 'Chile', 'Peru', 
    'Egypt', 'Pakistan', 'Bangladesh', 'Iraq', 'Ukraine', 'Kazakhstan', 'Uzbekistan', 'Sri Lanka', 
    'Morocco', 'Algeria', 'Tanzania', 'Ethiopia', 'Angola', 'Zimbabwe', 'Ghana', 'Ivory Coast', 
    'Senegal', 'Cameroon', 'Uganda', 'Sudan', 'Jamaica', 'Dominican Republic', 'Costa Rica', 
    'Honduras', 'El Salvador', 'Nicaragua', 'Panama', 'Cuba', 'Puerto Rico', 'New Zealand', 
    'Fiji', 'Papua New Guinea', 'Samoa', 'Tonga', 'Vanuatu', 'Kiribati', 'Marshall Islands', 
    'Micronesia', 'Solomon Islands', 'Tuvalu', 'Bhutan', 'Maldives', 'Mongolia', 'Laos', 
    'Myanmar', 'Cambodia', 'Brunei', 'Timor-Leste', 'Kuwait', 'Qatar', 'Bahrain', 'Oman', 
    'Cyprus', 'Malta', 'Estonia', 'Latvia', 'Lithuania', 'Slovakia', 'Slovenia', 
    'Bosnia and Herzegovina', 'Serbia', 'Montenegro', 'North Macedonia', 'Albania', 
    'Georgia', 'Armenia', 'Azerbaijan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan', 
    'Belarus', 'Moldova', 'Lithuania', 'Zambia', 'Malawi', 'Rwanda', 'Burundi', 
    'Gambia', 'Sierra Leone', 'Togo', 'Benin', 'Central African Republic', 'Chad', 
    'Republic of the Congo', 'Democratic Republic of the Congo', 'Equatorial Guinea', 
    'Gabon', 'Lesotho', 'Eswatini', 'Mauritius', 'Seychelles', 'Comoros', 'Djibouti'
]

# Step 2: Create the data dictionary with consistent lengths
num_entries_per_country = 10  # 10 entries per country
data = {
    'Country': [],
    'City': [],
    'Age': [],
    'Population_Density': [],
    'Wages': [],
    'Medicare_Eligibility': [],
    'Employees': []
}

# Populate the data dictionary
for country in countries:
    for i in range(num_entries_per_country):
        data['Country'].append(country)
        data['City'].append(f"{country} City {i+1}")  # Example city name
        data['Age'].append(25 + (i % 45))  # Age between 25 and 70
        data['Population_Density'].append(100 + (i * 10))  # Example density
        data['Wages'].append(30000 + (i * 1000))  # Example wage
        data['Medicare_Eligibility'].append(i % 2 == 0)  # Alternate eligibility
        data['Employees'].append(200 + (i * 10))  # Example employee count

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Save DataFrame to CSV
df.to_csv('country_data_large_150.csv', index=False)
print("CSV file 'country_data_large_150.csv' generated successfully!")
