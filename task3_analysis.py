import pandas as pd
import numpy as np

# 1.Load data
df = pd.read_csv("data/trends_clean.csv")

print("Loaded data:", df.shape)

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# checking averages
avg_score = np.mean(df["score"])
avg_comments = np.mean(df["num_comments"])

print("\nAverage score   :", avg_score)
print("Average comments:", avg_comments)


# 2.NumPy Analysis

print("\n--- NumPy Stats ---")

mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
std_score = np.std(df["score"])
max_score = np.max(df["score"])
min_score = np.min(df["score"])

print("Mean score   :", mean_score)
print("Median score :", median_score)
print("Std deviation:", std_score)
print("Max score    :", max_score)
print("Min score    :", min_score)


# Category has most stories
top_category = df["category"].value_counts().idxmax()
top_category_count = df["category"].value_counts().max()

print("\nMost stories in:", top_category, f"({top_category_count} stories)")


# Most commented story
top_comment_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:", 
      f"\"{top_comment_row['title']}\" — {top_comment_row['num_comments']} comments")


# 3.Add new columns

# engagement score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular 
df["is_popular"] = df["score"] > avg_score


# 4.Save final dataset into csv
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print("\nSaved to", output_file)