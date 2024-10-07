import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import os
import numpy as sns


# Read the dataset's csv file
df = pd.read_csv("C:\\Users\\nsuka\\PROJECT_CAR_SALE\\vehicles_us.csv")
df.info()

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