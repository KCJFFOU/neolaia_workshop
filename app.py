import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="Interaktivní PCA", layout="wide")
st.title("📊 Interaktivní PCA biplot")

df = pd.read_excel("capek-pca.xlsx", sheet_name="List1")
text_names = df.iloc[:, 0]
data = df.iloc[:, 1:]

scaler = StandardScaler()
scaled = scaler.fit_transform(data)

pca = PCA(n_components=2)
scores = pca.fit_transform(scaled)
explained = pca.explained_variance_ratio_ * 100

viz_df = pd.DataFrame({
    "Text": text_names,
    "PC1": scores[:, 0],
    "PC2": scores[:, 1]
})

fig = px.scatter(
    viz_df,
    x="PC1",
    y="PC2",
    hover_name="Text",
    labels={
        "PC1": f"PC1 ({explained[0]:.1f} %)",
        "PC2": f"PC2 ({explained[1]:.1f} %)"
    }
)
fig.update_traces(marker=dict(size=12, color='crimson'))

st.plotly_chart(fig, use_container_width=True)

selected = st.selectbox("Vyber text pro zobrazení indexů:", text_names)
if selected:
    st.dataframe(df[df.iloc[:, 0] == selected].iloc[:, 1:].T.rename(columns={df.columns[0]: "Hodnota"}).style.format("{:.3f}"))
