import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 DNA Dataset EDA")

# Load data
df = pd.read_csv("Dataset/synthetic_dna_dataset.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

st.subheader("Class Distribution")

fig = px.histogram(
    df,
    x="Class_Label",
    color="Class_Label"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Disease Risk Distribution")

fig2 = px.pie(
    df,
    names="Disease_Risk"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("GC Content vs AT Content")

fig3 = px.scatter(
    df,
    x="GC_Content",
    y="AT_Content",
    color="Class_Label"
)

st.plotly_chart(fig3, use_container_width=True)