import  pandas as pd
import os

# Create a sample Dataframe with column names.
data = {"Name":["anu","sus","charlie"],
        "age":[22,25,30],
        "city": ['New york',"los angelos","chicago"]}

df =pd.DataFrame(data)

# # Adding new row to df for v2
new_row_loc = {"Name":"New_person","age":20,"city":"city1"}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for v3
# new_row_loc2= {"Name":"v3", "age":30,"city":"city1"}
# df.loc[len(df.index)] = new_row_loc2

# Ensure the "data " directory exists at the root level
data_dir ="data"
os.makedirs(data_dir,exist_ok=True)

# Define the file path 
file_path = os.path.join(data_dir, "sample_data.csv")

# Save the Dataframe to a CSV file,including column names
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")