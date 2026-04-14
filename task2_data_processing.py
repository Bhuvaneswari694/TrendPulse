import json
import pandas as pd

# 1. Load JSON file
file_path = "data/trends_20260414.json" # task 1 output file

with open(file_path, "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Loaded {len(df)} stories from {file_path}")


# 2 — Clean Data

# Strip whitespaces in title
df["title"] = df["title"].str.strip()

# Drop rows with missing required values
df = df.dropna(subset=["post_id", "title", "score"])

print(f"After removing nulls: {len(df)}")

# Remove duplicates based on post_id
df = df.drop_duplicates(subset=["post_id"])

print(f"After removing duplicates: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)

# Remove low quality stories
df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")


# 3 — Category summary
print("\nStories per category:")
print(df["category"].value_counts())


# 4 — Save the cleaned file(dataframe to csv)
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")