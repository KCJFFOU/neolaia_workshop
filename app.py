import streamlit as st
import pandas as pd

st.set_page_config(page_title="Jazykové indexy textů", layout="centered")

st.title("📋 Jazykové indexy jednotlivých textů")

# Načtení dat
@st.cache_data
def load_data():
    return pd.read_excel("capek-pca.xlsx")

df = load_data()

# Roller pro výběr textu
text_names = df.iloc[:, 0].tolist()
selected = st.selectbox("Vyber text pro zobrazení indexů:", text_names)

# Zobrazení tabulky s indexy
if selected:
    st.write("### Hodnoty indexů:")
    st.dataframe(
        df[df.iloc[:, 0] == selected]
        .iloc[:, 1:]
        .T
        .rename(columns={df.columns[0]: "Hodnota"})
        .style.format("{:.3f}")
    )
