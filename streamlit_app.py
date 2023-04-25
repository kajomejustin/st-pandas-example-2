import streamlit as st
import pandas as pd

st.title('🐼 Pandas - A minimum working example')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
st.write(df)
  
if st.button('Show descriptive statistics analysis'):
  st.write(df.describe())
else:
  st.info('👆 Click on the button ')
