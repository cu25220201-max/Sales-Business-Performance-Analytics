import pandas as pd
from pathlib import Path

# -----------------------------
# File paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Actual raw dataset file
RAW_FILE = BASE_DIR / "data" / "raw" / "superstore_raw_practice.csv"

# Actual cleaned dataset file
CLEAN_FILE = BASE_DIR / "data" / "cleaned" / "superstore_cleaned_data.csv"


# -----------------------------
# Check if raw file exists
# -----------------------------
if not RAW_FILE.exists():
    print("\nERROR: Raw dataset file not found!")
    print("Expected file:")
    print(RAW_FILE)
    exit()


# -----------------------------
# Load raw dataset
# -----------------------------
print("\n========================================")
print("LOADING RAW DATASET")
print("========================================")

df = pd.read_csv(RAW_FILE)

print("Original Dataset Shape:", df.shape)

print("\nOriginal Columns:")
print(df.columns.tolist())


# -----------------------------
# Remove duplicate records
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate rows:", duplicates)

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# -----------------------------
# Clean column names
# -----------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# -----------------------------
# Remove extra spaces
# -----------------------------
text_columns = df.select_dtypes(
    include="object"
).columns

for column in text_columns:
    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# -----------------------------
# Convert dates
# -----------------------------
if "order_date" in df.columns:

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

if "ship_date" in df.columns:

    df["ship_date"] = pd.to_datetime(
        df["ship_date"],
        errors="coerce"
    )


# -----------------------------
# Convert numeric columns
# -----------------------------
numeric_columns = [
    "sales",
    "quantity",
    "discount",
    "profit"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# -----------------------------
# Missing values BEFORE cleaning
# -----------------------------
print("\n========================================")
print("MISSING VALUES BEFORE CLEANING")
print("========================================")

print(df.isnull().sum())


# -----------------------------
# Handle missing numeric values
# -----------------------------
for column in numeric_columns:

    if column in df.columns:

        median_value = df[column].median()

        df[column] = df[column].fillna(
            median_value
        )


# -----------------------------
# Handle missing text values
# -----------------------------
for column in text_columns:

    df[column] = df[column].replace(
        ["nan", "None", ""],
        pd.NA
    )

    df[column] = df[column].fillna(
        "Unknown"
    )


# -----------------------------
# Create date features
# -----------------------------
if "order_date" in df.columns:

    df["year"] = df["order_date"].dt.year

    df["month"] = df["order_date"].dt.month

    df["month_name"] = (
        df["order_date"]
        .dt.strftime("%B")
    )


# -----------------------------
# Create profit margin
# -----------------------------
if "sales" in df.columns and "profit" in df.columns:

    # Avoid division by zero
    df["profit_margin"] = (
        df["profit"]
        .div(df["sales"].replace(0, pd.NA))
        .fillna(0)
    )


# -----------------------------
# Save cleaned dataset
# -----------------------------
CLEAN_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    CLEAN_FILE,
    index=False
)


# -----------------------------
# Final information
# -----------------------------
print("\n========================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("========================================")

print("\nOriginal Dataset Shape:")
print("1202 rows × 20 columns (expected)")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

print("\nCleaned file saved at:")
print(CLEAN_FILE)

print("\n========================================")
print("PROCESS COMPLETED")
print("========================================")