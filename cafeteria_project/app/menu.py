import pandas as pd
import streamlit as st

df = pd.read_csv("cardapio.csv")
st.dataframe(df)
