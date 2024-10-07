import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import os
import numpy as sns
from pathlib import Path


# Read the dataset's csv file
df = pd.read_csv("C:\\Users\\nsuka\\PROJECT_CAR_SALE\\vehicles_us.csv")
df.info()

file_path = Path("c:/users/nsuka/PROJECT_CAR_SALE/vehicles_us.csv")
if file_path.exists():
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print("File does NOT exist.")

df.head()




# Add header
st.header ("Car Listings Analysis")

# Create a Plotly express histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Add a scatterplot for 'price' vs 'odometer'
fig_hist = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.write(fig_hist)

# Checkbox to show/hide trendline in scatter plot
show_trendline = st.checkbox("Show Trendline in Scatter Plot")