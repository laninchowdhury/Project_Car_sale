import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import os
import numpy as sns
from pathlib import Path
import statsmodels.api as sm





file_path = Path('vehicles_us.csv')

if file_path.exists():
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print("File does NOT exist.")
df.head()

st.set_page_config(page_title="Car Listing", page_icon=":bar_chart:", layout= "wide")

# Header with title
st.title(":bar_chart : Car Sales Analysis")

# Header for sctions
st.header('Price of Distribution')



# Histogram
fig_hist = px.histogram(df, x='price', nbins=10, title='Price Distribution')
st.plotly_chart(fig_hist)


# Scatter plot with checkbox for trendline
st.header('Price vs. Odometer')
add_trendline = st.checkbox('Add Trendline')
scatter_fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer', trendline='ols' if add_trendline else None)
st.plotly_chart(scatter_fig)


# Checkbox to filter data
if st.checkbox('Show only cars with price above $10,000'):
    df_filtered = df[df['price'] > 10000]
    st.write(df_filtered)
else:
    st.write(df)