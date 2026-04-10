import json
import pandas as pd

# Read JSOn file
with open("raw_data.json", "r") as f:
  data=json.load(f)

#check what is inside data dictionary
#print(data)
#print(data.keys())
#print(data['hits'])

#Convert to dataframe
posts = data['hits']
df= pd.DataFrame(posts)

# Check structure 
df.info()

# Select required columns
df=df[['title', 'points', 'num_comments']]

# Clean data
df=df.dropna()

# Save as CSV
df.to_csv("clean_data.csv", index=False)

print(df.head())
print("clean data succesfully")
