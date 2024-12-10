import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    return pd.read_csv('data/data.csv')

data = load_data()

# Title
st.title("Solar Data Dashboard")

# Data preview
if st.checkbox("Show Raw Data"):
    st.write(data.head())

# Histogram
st.header("Histogram")
column = st.selectbox("Select a column:", data.columns)
plt.hist(data[column].dropna(), bins=30, alpha=0.7)
st.pyplot(plt)
