import streamlit as st
import pandas as pd

st.title("Hello")

chart_data = pd.DataFrame(
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
