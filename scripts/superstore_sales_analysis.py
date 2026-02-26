import os
os.makedirs("charts", exist_ok=True)

# # Superstore Sales Analysis
# 
# This project analyzes retail sales data to uncover trends in revenue,
# profitability, and discount impact.
# 
# The goal is to demonstrate practical data analysis skills using
# Pandas and Matplotlib.

# ## 1 Import Libraries and Load Dataset

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/superstore_dataset.csv")
data.head()


# ## 2 Data Cleaning
# 
# - Convert date columns to datetime
# - Check missing values
# - Verify data types

data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

data.isnull().sum()


# ## 3 Exploratory Data Analysis
# 
# ###  Sales by Category


sales_cat = data.groupby('Category')['Sales'].sum().sort_values()

sales_cat.plot(kind='barh')
plt.title("Total Sales by Category")
plt.xlabel("Sales")
plt.savefig("charts/sales_by_category.png", dpi=300, bbox_inches="tight")
plt.show()


# ### Monthly Sales Trend

monthly_sales = data.set_index('Order Date').resample('M')['Sales'].sum()

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.savefig("charts/monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()


# ###  Profit vs Discount

plt.scatter(data['Discount'], data['Profit'], alpha=0.4)
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Profit vs Discount")
plt.savefig("charts/profit_vs_discount.png", dpi=300, bbox_inches="tight")
plt.show()


# ### Profit Margin Per Category


margin = data.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "sum"
})

margin["Profit Margin %"] = (margin["Profit"] / margin["Sales"] * 100).round(2)
margin.sort_values("Profit Margin %", ascending=False)


# ### Top 10 Customers by Revenue

top_customers = (
    data.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_customers.plot(kind="bar")
plt.title("Top 10 Customers by Sales")
plt.savefig("charts/top_customers.png", bbox_inches="tight")
plt.show()


# ### Region vs Category

pivot = pd.pivot_table(
    data,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum"
)

pivot


# ## Based on the analysis:
# 
# - Focus on high-performing categories such as Technology to maximize revenue.
# - Review discount policies to prevent profit erosion.
# - Optimize inventory based on seasonal sales trends.
# - Retain high-value customers through targeted strategies.
# - Investigate loss-making products and adjust pricing or sourcing.
# 
# Overall, data-driven decision making can significantly improve both revenue growth and operational efficiency.
