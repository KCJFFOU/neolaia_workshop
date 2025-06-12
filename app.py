import streamlit as st
import pandas as pd

st.set_page_config(page_title="Jazykové indexy textů", layout="centered")

st.title("📋 Jazykové indexy jednotlivých textů")

# Načtení Excelového souboru
@st.cache_data
def load_data():
    return pd.read_excel("capek-pca.xlsx")

df = load_data()

# Roller pro výběr textu
text_names = df.iloc[:, 0].tolist()
selected_text = st.selectbox("Vyber text:", text_names)

# Zobrazení indexů pro vybraný text
selected_row = df[df.iloc[:, 0] == selected_text].iloc[:, 1:]
st.write("### Hodnoty indexů:")
st.dataframe(selected_row.T.rename(columns={selected_row.index[0]: "Hodnota"}))
