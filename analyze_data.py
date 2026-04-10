import pandas as pd
import numpy as np

df = pd.read_csv("clean_data.csv")

print("Average points:", np.mean(df['points']))
print("Max points:", np.max(df['points']))
print("Average comments: ", np.mean(df['num_comments']))

# Sorting and read Big values
top_posts = df.sort_values(by='points', ascending=False).head(10)

print("\nTop 10 posts:")
print(top_posts[['title', 'points', 'num_comments']])