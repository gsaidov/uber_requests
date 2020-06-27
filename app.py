import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Uber rides")
st.markdown(<strong>"This is an analysis of Uber rides at the airport and city"<strong>)

data = pd.read_csv('data/Uber Request Data.csv')
st.subheader("This is raw data")
st.write(data)

st.subheader("Distribution of trips by status")
sns.catplot(x = 'Status', kind = 'count', data= data)
st.pyplot()
