import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Sales & Business Performance Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# PROJECT PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = (
    BASE_DIR
    / "data"
    / "cleaned"
    / "superstore_cleaned_data.csv"
)

# =========================================================
# TITLE
# =========================================================

st.title("📊 Sales & Business Performance Analytics Dashboard")

st.markdown(
    """
    **Interactive Business Intelligence Dashboard**

    Analyze sales, profit, customers, products, categories,
    regions and monthly business performance.
    """
)

# =========================================================
# CHECK DATASET
# =========================================================

if not DATA_FILE.exists():

    st.error("❌ Cleaned dataset not found!")

    st.write("Expected file:")
    st.code(str(DATA_FILE))

    st.stop()

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv(DATA_FILE)

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🔎 Dashboard Filters")

# Category filter
if "category" in df.columns:

    categories = sorted(df["category"].dropna().unique())

    selected_categories = st.sidebar.multiselect(
        "Select Category",
        categories,
        default=categories
    )

    df = df[
        df["category"].isin(selected_categories)
    ]

# Region filter
if "region" in df.columns:

    regions = sorted(df["region"].dropna().unique())

    selected_regions = st.sidebar.multiselect(
        "Select Region",
        regions,
        default=regions
    )

    df = df[
        df["region"].isin(selected_regions)
    ]

# Segment filter
if "segment" in df.columns:

    segments = sorted(df["segment"].dropna().unique())

    selected_segments = st.sidebar.multiselect(
        "Select Customer Segment",
        segments,
        default=segments
    )

    df = df[
        df["segment"].isin(selected_segments)
    ]

# =========================================================
# KPI CALCULATIONS
# =========================================================

total_sales = df["sales"].sum()

total_profit = df["profit"].sum()

total_orders = df["order_id"].nunique()

total_customers = df["customer_id"].nunique()

average_order_value = (
    total_sales / total_orders
    if total_orders > 0
    else 0
)

# =========================================================
# KPI CARDS
# =========================================================

st.subheader("📌 Business KPIs")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Sales",
        f"₹{total_sales:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"₹{total_profit:,.2f}"
    )

with col3:
    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )

with col4:
    st.metric(
        "Total Customers",
        f"{total_customers:,}"
    )

with col5:
    st.metric(
        "Average Order Value",
        f"₹{average_order_value:,.2f}"
    )

st.divider()

# =========================================================
# MONTHLY SALES TREND
# =========================================================

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    df.groupby("month")["sales"]
    .sum()
    .reset_index()
    .sort_values("month")
)

fig_monthly = px.line(
    monthly_sales,
    x="month",
    y="sales",
    markers=True,
    title="Monthly Sales Performance"
)

fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

# =========================================================
# CATEGORY ANALYSIS
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📦 Category-wise Sales")

    category_sales = (
        df.groupby("category")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )

    fig_category = px.bar(
        category_sales,
        x="category",
        y="sales",
        title="Sales by Category"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

with col2:

    st.subheader("💰 Profit by Category")

    category_profit = (
        df.groupby("category")["profit"]
        .sum()
        .reset_index()
        .sort_values("profit", ascending=False)
    )

    fig_profit = px.bar(
        category_profit,
        x="category",
        y="profit",
        title="Profit by Category"
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )

# =========================================================
# TOP 10 PRODUCTS
# =========================================================

st.subheader("🏆 Top 10 Products by Sales")

top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products.sort_values("sales"),
    x="sales",
    y="product_name",
    orientation="h",
    title="Top 10 Products"
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)

# =========================================================
# CUSTOMER SEGMENT
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("👥 Customer Segment")

    segment_sales = (
        df.groupby("segment")["sales"]
        .sum()
        .reset_index()
    )

    fig_segment = px.pie(
        segment_sales,
        names="segment",
        values="sales",
        title="Sales by Customer Segment"
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )

with col2:

    st.subheader("🗺️ Region-wise Sales")

    region_sales = (
        df.groupby("region")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )

    fig_region = px.bar(
        region_sales,
        x="region",
        y="sales",
        title="Sales by Region"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

# =========================================================
# STATE ANALYSIS
# =========================================================

st.subheader("📍 State-wise Sales")

state_sales = (
    df.groupby("state")["sales"]
    .sum()
    .reset_index()
    .sort_values("sales", ascending=False)
    .head(15)
)

fig_state = px.bar(
    state_sales,
    x="sales",
    y="state",
    orientation="h",
    title="Top 15 States by Sales"
)

st.plotly_chart(
    fig_state,
    use_container_width=True
)

# =========================================================
# DATA PREVIEW
# =========================================================

with st.expander("📋 View Dataset"):

    st.write(
        f"Showing {len(df):,} filtered records"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    ### 📊 Sales & Business Performance Analytics

    **Technology:** Python | Pandas | Plotly | Streamlit

    **Project Workflow:** Data Cleaning → EDA → SQL Analysis → Dashboard

    © 2026 Sales Business Performance Analytics
    """
)