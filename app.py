import streamlit as st
import pandas as pd

st.set_page_config(page_title="Indexy pro jednotlivé texty", layout="wide")

st.title("📄 Hodnoty jazykových indexů")

# Načíst soubor
df = pd.read_excel("capek-pca.xlsx")

# Vygenerovat scrollovatelnou tabulku s fixovaným headerem
st.markdown(
    """
    <style>
    .dataframe-container {
        height: 600px;
        overflow-y: auto;
        border: 1px solid #ddd;
        background-color: white;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='dataframe-container'>", unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)
