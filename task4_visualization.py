import pandas as pd
import matplotlib.pyplot as plt
import os

# 1.read data
df = pd.read_csv("data/trends_analysed.csv")
print("Loaded data:", df.shape)

#  Create output folder
os.makedirs("outputs", exist_ok=True)


# --------------------------- CHART 1 — Top 10 Stories by Score

top_10 = df.sort_values(by="score", ascending=False).head(10)

# shorten long titles
titles = []
for t in top_10["title"]:
    if len(t) > 50:
        titles.append(t[:50] + "...")
    else:
        titles.append(t)
top_10_titles = titles

plt.figure(figsize=(10, 6))
plt.barh(top_10_titles, top_10["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# ---------------------------CHART 2 — Stories per Category

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()


# ---------------------------CHART 3 — Score vs Comments

colors = df["is_popular"].map({True: "green", False: "red"})

plt.figure(figsize=(8, 5))
plt.scatter(df["score"], df["num_comments"], c=colors)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()


# ---------------------------
# BONUS — DASHBOARD (2x2 layout)
# ---------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("TrendPulse Dashboard", fontsize=16)

# Chart 1
axes[0, 0].barh(top_10_titles, top_10["score"])
axes[0, 0].set_title("Top Stories")
axes[0, 0].invert_yaxis()

# Chart 2
axes[0, 1].bar(category_counts.index, category_counts.values)
axes[0, 1].set_title("Categories")

# Chart 3
axes[1, 0].scatter(df["score"], df["num_comments"], c=colors)
axes[1, 0].set_title("Score vs Comments")

# Empty fourth plot (clean look)
axes[1, 1].axis("off")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")

print("\nAll charts saved successfully in outputs/")