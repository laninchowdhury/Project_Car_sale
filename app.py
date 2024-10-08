import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import os
import numpy as sns
from pathlib import Path







file_path = Path('vehicles_us.csv')

if file_path.exists():
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print("File does NOT exist.")
df.head()


# Header with title
st.title('Car Sales Data Analysis')

# Header for sections
st.header('Price Distribution')

# Histogram
hist_fig = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(hist_fig)

# Scatter plot section
st.header('Price vs. Odometer')
add_trendline = st.checkbox('Add Trendline')
scatter_fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer', trendline='ols' if add_trendline else None)
st.plotly_chart(scatter_fig)

   