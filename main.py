# ==============================
# UNEMPLOYMENT ANALYSIS IN INDIA
# ==============================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Display First 5 Rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset Info
print("\nDATASET INFO")
print(df.info())

# Remove Extra Spaces
df.columns = df.columns.str.strip()

# Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Rename Columns
df.columns = [
    "States",
    "Date",
    "Frequency",
    "Estimated_Unemployment_Rate",
    "Estimated_Employed",
    "Estimated_Labour_Participation_Rate",
    "Area"
]

# Convert Date Column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Statistical Summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Average Unemployment Rate
avg_rate = df["Estimated_Unemployment_Rate"].mean()
print("\nAverage Unemployment Rate:", avg_rate)

# State Wise Unemployment
state_unemployment = df.groupby("States")[
    "Estimated_Unemployment_Rate"
].mean().sort_values(ascending=False)

print("\nSTATE WISE UNEMPLOYMENT")
print(state_unemployment)

# ==============================
# VISUALIZATION
# ==============================

# Bar Plot
plt.figure(figsize=(14,7))

sns.barplot(
    x=state_unemployment.index,
    y=state_unemployment.values
)

plt.xticks(rotation=90)
plt.title("Average Unemployment Rate by State")
plt.xlabel("States")
plt.ylabel("Unemployment Rate")

plt.show()

# Line Plot
plt.figure(figsize=(12,6))

sns.lineplot(
    x="Date",
    y="Estimated_Unemployment_Rate",
    data=df
)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")

plt.xticks(rotation=45)

plt.show()

# Box Plot
plt.figure(figsize=(8,5))

sns.boxplot(
    x="Area",
    y="Estimated_Unemployment_Rate",
    data=df
)

plt.title("Area Wise Unemployment")

plt.show()

# Heatmap
plt.figure(figsize=(8,5))

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# Final Insights
print("\nPROJECT INSIGHTS")
print("1. Unemployment varied across states.")
print("2. Some states showed higher unemployment.")
print("3. Urban and rural unemployment differed.")
print("4. COVID-19 increased unemployment.")