import streamlit as st
import pandas as pd

st.set_page_config(page_title="Indexy pro jednotlivé texty", layout="wide")
st.title("🧾 Hodnoty jazykových indexů pro jednotlivé texty")

# Načti data
df = pd.read_excel("capek-pca.xlsx", sheet_name="List1")

# Zobraz tabulku
st.dataframe(df, use_container_width=True)
