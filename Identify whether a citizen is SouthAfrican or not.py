# Import packages 
# import ...
# Create a dataframe
data = data[['ID number', 'South African Citizen', '..................']]

# Identify if a citizen is South African or Not
data['ID_num_count'] = data['ID Number'].str.len()
# Use the new column that count the num of ID numbers
# In South Africa an ID number has 13 values
data['South African Citizen']  = data['ID_num_count'].apply(lambda x:
                                'Yes' if x == 13 else 'No')