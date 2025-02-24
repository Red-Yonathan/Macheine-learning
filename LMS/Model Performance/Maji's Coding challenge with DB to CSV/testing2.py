import pandas as pd
import sqlite3

conn = sqlite3.connect("Maji_Ndogo_farm_survey_small.db")

# Read all tables into DataFrames
data_frames = {}
for table_name in pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn):
  data_frames[table_name[0]] = pd.read_sql_query(f"SELECT * FROM {table_name[0]}", conn)

# Concatenate DataFrames
all_data = pd.concat(data_frames.values(), ignore_index=True)

# Write to CSV
all_data.to_csv("all_tables.csv", index=False)

conn.close()

#__________________________________________________________________________________________________________
#calculating correlation codefficient 
import pandas as pd

# Sample data as a DataFrame
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]}
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)



#__________________________________________________________________________________________________________
#pd.rename
import pandas as pd

data = {'old_name1': [1, 2, 3], 'old_name2': [4, 5, 6]}
df = pd.DataFrame(data)

# Rename columns using a dictionary
new_names = {'old_name1': 'new_name1', 'old_name2': 'new_name2'}
df_renamed = df.rename(columns=new_names)

print(df_renamed)



#another way of renaing 
data = {'old_name1': [1, 2, 3], 'old_name2': [4, 5, 6]}
df = pd.DataFrame(data)

# Rename columns using list assignment
df.columns = ['new_name1', 'new_name2']

print(df)

#______________________________________________________________________________________________________

#here is how to use .apply 
import pandas as pd

# Create a DataFrame
data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'a']}
df = pd.DataFrame(data)

# Define functions for squaring and converting string to uppercase
def square(x):
  return x * x

def to_uppercase(x):
  if isinstance(x, str):  # Check if string
    return x.upper()
  else:
    return x  # Return original value for non-strings

# Apply squaring to each value (column-wise by default)
df_squared = df.apply(square)
print(df_squared)  # DataFrame with squared values

# Apply to rows (calculate sum) and columns (calculate mean)
df_sum_rows = df.apply(sum, axis=1)
df_mean_cols = df.apply(pd.Series.mean)
print(df_sum_rows)  # Series with sum of each row
print(df_mean_cols)  # Series with mean of each column

# Apply lambda function for string uppercasing (column-wise)
df_uppercase = df.apply(lambda x: to_uppercase(x))
print(df_uppercase)  # DataFrame with uppercase strings (if applicable)
