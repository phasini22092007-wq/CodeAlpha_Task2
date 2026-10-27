
import pandas as pd

# Load the dataset
df = pd.read_csv("books_data.csv")
print("\n--- Questions for EDA ---")
print("1. Which book has the highest price?")
print("2. Which book has the lowest price?")
print("3. Which rating is most common?")
print("4. Is there a relationship between book price and rating?")
print("5. Are there missing values or duplicate records?")

# Display the first five rows
print("First five rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset information:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Display basic statistics
print("\nBasic statistics:")
print(df.describe())

import matplotlib.pyplot as plt

# Graph 1: Book prices
plt.figure(figsize=(10, 5))
plt.bar(df["Title"], df["Price"])
plt.title("Book Prices Comparison")
plt.xlabel("Book Title")
plt.ylabel("Price")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("book_prices.png")
plt.close()

# Graph 2: Book ratings
plt.figure(figsize=(8, 5))
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("book_ratings.png")
plt.close()

print("Both graph files have been created successfully!")
# Step 23: Find the highest and lowest book prices

print("\n--- Price Analysis ---")

highest_price = df.loc[df["Price"].idxmax()]
lowest_price = df.loc[df["Price"].idxmin()]

print("Most expensive book:", highest_price["Title"])
print("Highest price:", highest_price["Price"])

print("Cheapest book:", lowest_price["Title"])
print("Lowest price:", lowest_price["Price"])
# Step 24: Analyze book ratings

print("\n--- Rating Analysis ---")

print("Rating counts:")
print(df["Rating"].value_counts().sort_index())

print("\nMost common rating:")
print(df["Rating"].mode()[0])

# Step 25: Check data quality

print("\n--- Data Quality Check ---")

print("Duplicate rows:", df.duplicated().sum())

print("Duplicate book titles:", df["Title"].duplicated().sum())

print("Invalid prices:", (df["Price"] <= 0).sum())

print("Ratings outside the 1-5 range:",
      ((df["Rating"] < 1) | (df["Rating"] > 5)).sum())

# Step 26: Relationship between price and rating

print("\n--- Price and Rating Relationship ---")

correlation = df["Price"].corr(df["Rating"])

print("Correlation between price and rating:", round(correlation, 2))

if correlation > 0.3:
    print("There is a positive relationship.")
elif correlation < -0.3:
    print("There is a negative relationship.")
else:
    print("There is a weak or no linear relationship.")
    
# Step 27: Visualize price vs rating

plt.figure(figsize=(8, 5))

plt.scatter(df["Rating"], df["Price"])

plt.title("Relationship Between Book Rating and Price")
plt.xlabel("Book Rating")
plt.ylabel("Book Price")
plt.tight_layout()

plt.savefig("price_vs_rating.png")
plt.close()

print("Price vs rating graph created successfully!")



