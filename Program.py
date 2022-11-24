import streamlit as st
import pandas as pd
#streamlit run .\Program.py
"""

python3 -m venv дириктория

streamlit run .\main_app.py

python -m streamlit run app.py

py -3.10 -m pip install streamlit
pip install streamlit==0.62.0
c born

"""

st.title("Hello")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.write(df)
