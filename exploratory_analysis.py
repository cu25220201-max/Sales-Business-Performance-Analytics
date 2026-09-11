import pandas as pd
from pathlib import Path

# -----------------------------
# File path
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

FILE = BASE_DIR / "data" / "cleaned" / "superstore_cleaned_data.csv"

# -----------------------------
# Check file
# -----------------------------
if not FILE.exists():
    print("ERROR: Cleaned dataset not found!")
    print("Expected file:")
    print(FILE)
    exit()

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv(FILE)

print("\n========================================")
print("SALES & BUSINESS PERFORMANCE ANALYSIS")
print("========================================")

print("\nDataset Shape:")
print(df.shape)

# -----------------------------
# Basic KPIs
# -----------------------------
total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()

print("\n========== KEY PERFORMANCE INDICATORS ==========")

print(f"Total Sales     : {total_sales:,.2f}")
print(f"Total Profit    : {total_profit:,.2f}")
print(f"Total Orders    : {total_orders:,}")
print(f"Total Customers : {total_customers:,}")


# -----------------------------
# Category Analysis
# -----------------------------
print("\n========== CATEGORY-WISE ANALYSIS ==========")

category_analysis = (
    df.groupby("category")
    .agg(
        Total_Sales=("sales", "sum"),
        Total_Profit=("profit", "sum")
    )
    .sort_values(
        "Total_Sales",
        ascending=False
    )
)

print(category_analysis)


# -----------------------------
# Top 10 Products
# -----------------------------
print("\n========== TOP 10 PRODUCTS BY SALES ==========")

top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

print(top_products)


# -----------------------------
# Top 10 Customers
# -----------------------------
print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

top_customers = (
    df.groupby("customer_name")["sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

print(top_customers)


# -----------------------------
# State Analysis
# -----------------------------
print("\n========== TOP 10 STATES BY SALES ==========")

state_sales = (
    df.groupby("state")["sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

print(state_sales)


# -----------------------------
# Monthly Sales
# -----------------------------
print("\n========== MONTHLY SALES ==========")

if "month_name" in df.columns:

    monthly_sales = (
        df.groupby("month_name")["sales"]
        .sum()
    )

    print(monthly_sales)


# -----------------------------
# Customer Segment
# -----------------------------
print("\n========== CUSTOMER SEGMENT ANALYSIS ==========")

segment_sales = (
    df.groupby("segment")["sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print(segment_sales)


# -----------------------------
# Profit Analysis
# -----------------------------
print("\n========== PROFIT ANALYSIS ==========")

profitable_sales = df[df["profit"] > 0]["profit"].sum()
loss_sales = df[df["profit"] < 0]["profit"].sum()

print(f"Total Positive Profit : {profitable_sales:,.2f}")
print(f"Total Loss            : {loss_sales:,.2f}")


# -----------------------------
# Final message
# -----------------------------
print("\n========================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("========================================")