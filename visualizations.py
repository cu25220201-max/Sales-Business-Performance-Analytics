import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------------------
# Project directory
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------
# Correct cleaned dataset path
# -----------------------------------------
DATA_FILE = (
    BASE_DIR
    / "data"
    / "cleaned"
    / "superstore_cleaned_data.csv"
)

# -----------------------------------------
# Images folder
# -----------------------------------------
IMAGE_DIR = BASE_DIR / "images"

IMAGE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# -----------------------------------------
# Check dataset
# -----------------------------------------
if not DATA_FILE.exists():
    print("\nERROR: Cleaned dataset not found!")
    print("Expected file:")
    print(DATA_FILE)
    exit()

# -----------------------------------------
# Load dataset
# -----------------------------------------
print("\n========================================")
print("LOADING CLEANED DATASET")
print("========================================")

df = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)


# =========================================
# 1. MONTHLY SALES TREND
# =========================================

print("\nCreating Monthly Sales Trend...")

monthly_sales = (
    df.groupby("month")["sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(monthly_sales.index)

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "sales_trend.png",
    dpi=300
)

plt.close()

print("Created: sales_trend.png")


# =========================================
# 2. CATEGORY-WISE SALES
# =========================================

print("\nCreating Category-wise Sales...")

category_sales = (
    df.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "category_analysis.png",
    dpi=300
)

plt.close()

print("Created: category_analysis.png")


# =========================================
# 3. TOP 10 PRODUCTS
# =========================================

print("\nCreating Top 10 Products...")

top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "top_products.png",
    dpi=300
)

plt.close()

print("Created: top_products.png")


# =========================================
# FINAL MESSAGE
# =========================================

print("\n========================================")
print("VISUALIZATIONS CREATED SUCCESSFULLY!")
print("========================================")

print("\nImages saved in:")
print(IMAGE_DIR)

print("\nFiles created:")
print("1. sales_trend.png")
print("2. category_analysis.png")
print("3. top_products.png")

print("\nPython Visualization Part COMPLETED!")