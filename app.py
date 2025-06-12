import streamlit as st
import pandas as pd

st.set_page_config(page_title="Indexy textů", layout="centered")

st.title("📋 Jazykové indexy jednotlivých textů")

# Načtení dat
df = pd.read_excel("capek-pca.xlsx")

# Výběr textu
text_names = df.iloc[:, 0].tolist()
selected_text = st.selectbox("Vyber text:", text_names)

# Výpis indexů pro vybraný text
selected_row = df[df.iloc[:, 0] == selected_text].iloc[:, 1:]
st.write("### Hodnoty indexů:")
st.dataframe(selected_row.T.rename(columns={selected_row.index[0]: "Hodnota"}))
