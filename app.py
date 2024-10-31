# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load sample data
@st.cache
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31")
    data = pd.DataFrame({
        "date": dates,
        "sales": np.random.poisson(lam=200, size=len(dates)),
        "expenses": np.random.poisson(lam=150, size=len(dates))
    })
    data['profit'] = data['sales'] - data['expenses']
    return data

data = load_data()

# Title
st.title("Demo Dashboard")

# KPIs
total_sales = data['sales'].sum()
total_expenses = data['expenses'].sum()
total_profit = data['profit'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Expenses", f"${total_expenses:,.0f}")
col3.metric("Total Profit", f"${total_profit:,.0f}")

# Date Filter
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", data["date"].min())
end_date = st.sidebar.date_input("End Date", data["date"].max())

filtered_data = data[(data["date"] >= pd.to_datetime(start_date)) & 
                     (data["date"] <= pd.to_datetime(end_date))]

# Data Visualization
st.subheader("Sales & Expenses Over Time")
fig = px.line(filtered_data, x="date", y=["sales", "expenses"], 
              labels={"value": "Amount", "variable": "Metric"}, 
              title="Sales vs Expenses Over Time")
st.plotly_chart(fig)

# Profit Distribution
st.subheader("Profit Distribution")
fig2 = px.histogram(filtered_data, x="profit", nbins=30, title="Profit Distribution")
st.plotly_chart(fig2)

# Data Table
st.subheader("Data Table")
st.write(filtered_data)