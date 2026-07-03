import pandas as pd
import matplotlib.pyplot as plt
import os

try:
    
    df = pd.read_csv("C:/Users/Admin/Desktop/Internship program/Week-4/sales_data.csv")

    
    if df.isnull().sum().sum() > 0:
        df = df.dropna()

    
    df["Date"] = pd.to_datetime(df["Date"])

    
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    print("Dataset Loaded Successfully")
    print(df.head())

    
    df["Month"] = df["Date"].dt.strftime("%B")
    monthly_sales = df.groupby("Month")["Total_Sales"].sum()

    
    category_sales = df.groupby("Category")["Total_Sales"].sum()

    
    os.makedirs("output", exist_ok=True)

    
    plt.figure(figsize=(8,5))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales (₹)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/monthly_sales.png")
    plt.show()

    
    plt.figure(figsize=(7,5))
    category_sales.plot(kind="bar")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales (₹)")
    plt.tight_layout()
    plt.savefig("output/category_sales.png")
    plt.show()

    
    print("\nOverall Sales:", df["Total_Sales"].sum())
    print("Average Sale:", df["Total_Sales"].mean())
    print("Highest Sale:", df["Total_Sales"].max())
    print("Lowest Sale:", df["Total_Sales"].min())

except FileNotFoundError:
    print("Error: Dataset file not found.")

except Exception as e:
    print("Unexpected Error:", e)