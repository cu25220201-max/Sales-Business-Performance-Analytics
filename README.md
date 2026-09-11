# 📊 Sales & Business Performance Analytics

An end-to-end **Data Analytics project** that transforms raw sales data into meaningful business insights using **Python, SQL, MySQL, and Power BI**.

This project was developed as part of my **Data Analytics Internship at 3Skill Training**, providing practical experience in data cleaning, exploratory data analysis, SQL-based business analysis, dashboard development, and insight generation.

---

## 👩‍💻 3Skill Training Internship Context

**Internship:** Data Analytics Internship  
**Organization:** 3Skill Training  
**Project:** Sales & Business Performance Analytics

This project was developed as part of my internship learning experience at **3Skill Training**.

The project follows a complete data analytics workflow:

> **Raw Dataset → Data Cleaning → Exploratory Data Analysis → SQL Analysis → Power BI Dashboard → Business Insights**

The objective was to apply practical data analytics concepts to a structured sales dataset and convert raw data into useful business information for decision-making.

---

## 🎯 Project Objective

The primary objective of this project is to analyze sales and business performance data and identify important trends, patterns, and opportunities.

### Key Objectives

- Analyze overall sales and profit performance
- Identify monthly sales trends
- Compare category and sub-category performance
- Identify top-performing products
- Identify loss-making products
- Analyze customer segments
- Compare regional and state-wise performance
- Analyze shipping modes
- Evaluate year-wise sales growth
- Calculate important business KPIs
- Generate actionable business recommendations

---

## 🛠️ Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| 🐍 Python | Data Cleaning & Exploratory Data Analysis |
| 🐼 Pandas | Data Manipulation & Analysis |
| 📊 Matplotlib | Data Visualization |
| 🗄️ MySQL | Database Management |
| 💻 SQL | Business Data Analysis |
| 📈 Power BI | Interactive Dashboard & Reporting |
| 📁 CSV | Dataset Storage |
| 🔧 VS Code | Development Environment |

---

## 📂 Project Structure

```text
Sales-Business-Performance-Analytics/
│
├── data/
│   ├── raw/
│   │   └── superstore_raw_practice.csv
│   │
│   └── cleaned/
│       └── superstore_cleaned_data.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── visualizations.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_table.sql
│   └── analysis_queries.sql
│
├── powerbi/
│   └── Sales_Business_Performance_Analytics_Dashboard.pbix
│
├── images/
│   ├── dashboard_overview.png
│   ├── sales_profit_analysis.png
│   ├── monthly_sales_trend.png
│   ├── category_analysis.png
│   ├── regional_analysis.png
│   └── product_analysis.png
│
├── README.md
└── requirements.txt


##### 📊 Dataset Overview

The dataset contains 1,200 sales records representing customers, products, categories, regions, states, cities, shipping modes, sales, discounts, and profits.

Dataset Information
Records: 1,200
Columns: 24
Time Period: 2024–2025
Data Type: Structured sales/business data
Format: CSV
Dataset Columns
Order ID
Order Date
Ship Date
Ship Mode
Customer ID
Customer Name
Segment
Country
City
State
Postal Code
Region
Product ID
Category
Sub-Category
Product Name
Sales
Quantity
Discount
Profit
Year
Month
Month Name
Profit Margin
🧹 Data Cleaning

The raw dataset was cleaned and prepared using Python and Pandas before performing analysis.

## Data Cleaning Steps
Loaded the raw CSV dataset
Inspected dataset structure
Checked for missing values
Checked for duplicate records
Standardized column names
Converted date columns into appropriate date formats
Converted numerical columns into appropriate data types
Created Year and Month fields
Created Month Name
Calculated Profit Margin
Removed unnecessary duplicate records
Exported the final cleaned dataset
Cleaned Dataset

The final cleaned dataset contains:

1,200 records × 24 columns

The cleaned dataset was then used for Python analysis, SQL analysis, and Power BI visualization.

## 🐍 Python Exploratory Data Analysis

Python was used to explore the cleaned dataset and understand different aspects of business performance.

Analysis Performed
Sales distribution analysis
Profit distribution analysis
Monthly sales trend analysis
Category-wise sales analysis
Sub-category performance analysis
Regional performance analysis
Customer segment analysis
Top-performing product analysis
Loss-making product analysis
Profit margin analysis
Python Libraries
pandas
matplotlib

The analysis helped identify important trends and patterns before building the final dashboard.

## 🗄️ SQL Analysis

The cleaned dataset was imported into a MySQL database for structured business analysis.

## Database
Database: sales_analytics
Table: sales_data
SQL Analysis Includes
Total Sales
Total Profit
Total Orders
Total Customers
Total Quantity
Average Order Value
Monthly Sales
Category Performance
Sub-Category Performance
Top Products
Loss-Making Products
Customer Segment Analysis
Region-wise Performance
State-wise Performance
City-wise Performance
Shipping Mode Analysis
Year-wise Performance
Profit Margin Analysis
SQL Concepts Used
SELECT
WHERE
GROUP BY
ORDER BY
COUNT()
SUM()
AVG()
DISTINCT
HAVING
Aggregate Functions
Business-oriented SQL queries

## 📈 Power BI Dashboard

An interactive Power BI dashboard was developed to provide a consolidated view of sales and business performance.

#### SALES & BUSINESS PERFORMANCE ANALYTICS DASHBOARD

The dashboard converts analytical results into interactive visual reports that can be used to understand business performance quickly.



These KPIs provide a high-level summary of the overall business performance.


1. Dashboard Overview

2. Sales & Profit Analysis

3. Monthly Sales Trend

4. Category Analysis

5. Regional Analysis

6. Product Analysis


  #### Screenshots

  <img width="646" height="356" alt="image" src="https://github.com/user-attachments/assets/fe92ddb4-89a0-40e9-b72e-11341031abfd" />

  <img width="960" height="430" alt="image" src="https://github.com/user-attachments/assets/9bc5ee1a-4c6f-4c72-a842-64145a26fea6" />

  <img width="659" height="406" alt="image" src="https://github.com/user-attachments/assets/f1b436c8-9955-45e5-b699-1852cf132cb3" />

  <img width="701" height="445" alt="image" src="https://github.com/user-attachments/assets/264a6947-6f79-48fc-ba73-0cd83b765ee5" />

  <img width="693" height="419" alt="image" src="https://github.com/user-attachments/assets/98831e14-beaa-46e3-9d28-c0c185bacd6a" />

  <img width="682" height="431" alt="image" src="https://github.com/user-attachments/assets/8dde56d2-5dde-4792-a634-d2c329f0c81c" />


<img width="655" height="416" alt="image" src="https://github.com/user-attachments/assets/c91e0b19-279a-4933-8296-285593b32c6e" />

<img width="665" height="427" alt="image" src="https://github.com/user-attachments/assets/86ca96e9-8f3a-4b6b-b8bc-16f300ed631a" />


<img width="617" height="345" alt="image" src="https://github.com/user-attachments/assets/abc57409-c5e4-49ed-b9f5-d2d165b674dc" />

<img width="572" height="335" alt="image" src="https://github.com/user-attachments/assets/a005a593-d6e3-4fb5-ac5e-93e36713e992" />

<img width="665" height="356" alt="image" src="https://github.com/user-attachments/assets/2e954f73-5733-4e78-897e-5dee474359bc" />

<img width="337" height="341" alt="image" src="https://github.com/user-attachments/assets/4510343a-239a-40fb-a81c-1b82abcd0e7d" />

<img width="388" height="254" alt="image" src="https://github.com/user-attachments/assets/c1643ecd-b5ff-4003-8116-316d685fd576" />

<img width="540" height="274" alt="image" src="https://github.com/user-attachments/assets/f14b2c36-b7db-4736-bcf4-794660ade2a5" />

<img width="335" height="218" alt="image" src="https://github.com/user-attachments/assets/19b9a40b-842e-45cf-93c1-4308a4572ba7" />


<img width="612" height="436" alt="image" src="https://github.com/user-attachments/assets/e197fd2b-e75b-4853-b0cb-fe185082c597" />

<img width="654" height="259" alt="image" src="https://github.com/user-attachments/assets/b8b4ecb9-9957-434d-a534-b6a493c57faa" />


## 💡 Business Recommendations

Based on the analysis, the following recommendations can be considered:

1. Review Loss-Making Products

Analyze products with negative profit and evaluate:

Pricing strategy
Discount levels
Procurement costs
Shipping costs
Product demand
2. Focus on High-Performing Categories

Furniture and Technology show strong sales performance and can be prioritized for future growth strategies.

3. Strengthen the Consumer Segment

Since the Consumer segment contributes the highest sales, targeted marketing and customer retention strategies can be developed for this segment.

4. Improve Central Region Performance

The Central region has comparatively lower sales and profit. Regional marketing and customer acquisition strategies can be explored.

5. Monitor Monthly Sales Trends

Regular monitoring of monthly sales can help identify seasonal patterns and support better inventory, marketing, and sales planning.

## 🎓 Skills Demonstrated
Data Analytics
Data Cleaning
Data Preprocessing
Exploratory Data Analysis
Business Analysis
KPI Development
Business Insight Generation
Python
Python
Pandas
Matplotlib
Data Manipulation
Data Analysis
Data Visualization
SQL & MySQL
SQL Querying
Database Management
Aggregation
Filtering
Grouping
Business Analysis
Power BI
Dashboard Development
KPI Cards
Interactive Visualizations
Slicers
Business Reporting
Data Visualization

## 🚀 Project Workflow
Raw Dataset
     ↓
Data Cleaning
     ↓
Python EDA
     ↓
MySQL Database
     ↓
SQL Business Analysis
     ↓
Power BI Dashboard
     ↓
Business Insights
     ↓
Recommendations

## 📌 Project Outcome

This project demonstrates how raw sales data can be transformed into meaningful business insights through an end-to-end analytics workflow.

The project combines:

Python + SQL + MySQL + Power BI

to support data-driven decision-making.



## 👩‍💻 Author
Pratiksha Tomar

B.Tech AI/ML Student | Aspiring Data Analyst

Technical Skills

Python SQL MySQL Power BI Pandas Matplotlib Data Analytics Machine Learning

#DataAnalytics
#Python
#SQL
#MySQL
#PowerBI
#Pandas
#DataVisualization
#BusinessAnalytics
#DataScience
#Analytics
#Internship
#3SkillTraining
#BTech
#AIandML




