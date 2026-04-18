import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Dashboard", layout="wide")

# Title
st.title("📊 My Streamlit Dashboard")

# Sidebar
st.sidebar.header("Filter Options")

# Dummy data
data = pd.DataFrame({
    "Category": ["A", "B", "C", "A", "B", "C"],
    "Values": [10, 20, 15, 25, 30, 35]
})

# Sidebar filter
category = st.sidebar.selectbox("Select Category", data["Category"].unique())

# Filter data
filtered_data = data[data["Category"] == category]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total", filtered_data["Values"].sum())
col2.metric("Average", round(filtered_data["Values"].mean(), 2))
col3.metric("Max", filtered_data["Values"].max())

# Chart
st.subheader("📈 Chart")
st.bar_chart(filtered_data.set_index("Category"))

# Table
st.subheader("📋 Data Table")
st.dataframe(filtered_data)

# User input
st.subheader("🧮 Add New Data")

new_category = st.selectbox("Category", ["A", "B", "C"])
new_value = st.number_input("Value", min_value=0)

if st.button("Add Data"):
    st.success(f"Added {new_category} with value {new_value}")