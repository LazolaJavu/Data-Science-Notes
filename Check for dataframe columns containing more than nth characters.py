# Assuming you are working with a dataframe
data = #Assign a dataframe

# Use a for loop to identify the columns with the more than 64 columns
for col in df_check.columns:
    if (data[col].str.len()).max() > 64:
        print(col)
