import streamlit as st
import pandas as pd
#streamlit run .\Program.py

st.title("Hello")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.write(df)
