import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_data.csv")

top = df.sort_values(by='points', ascending=False).head(10)

plt.bar(top['title'], top['points'])
#to not overlapping x- axis names 
plt.xticks(rotation=90)
plt.xlabel("Post title")
plt.ylabel("Points")
plt.title("Top 10  Treanding Posts by Points")
plt.show()