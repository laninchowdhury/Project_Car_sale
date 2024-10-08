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



# Ensure odometer is numeric and handle missing values
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
df['odometer'].fillna(df['odometer'].median(), inplace=True)

# Header with title
st.title('Car Sales Data Analysis')

# Scatter plot section
st.header('Price vs. Odometer')
add_trendline = st.checkbox('Add Trendline')
scatter_fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer', size='odometer', hover_data=['model'], trendline='ols' if add_trendline else None)
st.plotly_chart(scatter_fig)
   