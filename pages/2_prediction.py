import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🧬 DNA Classification Prediction")

st.write("Enter DNA feature values below:")

gc = st.slider("GC Content", 0.0, 100.0, 50.0)

at = st.slider("AT Content", 0.0, 100.0, 50.0)

length = st.number_input(
    "Sequence Length",
    min_value=1,
    value=100
)

num_a = st.number_input(
    "Number of A",
    min_value=0,
    value=25
)

num_t = st.number_input(
    "Number of T",
    min_value=0,
    value=25
)

num_c = st.number_input(
    "Number of C",
    min_value=0,
    value=25
)

num_g = st.number_input(
    "Number of G",
    min_value=0,
    value=25
)

kmer = st.slider(
    "3-mer Frequency",
    0.0,
    1.0,
    0.5
)

mutation = st.selectbox(
    "Mutation Flag",
    [0, 1]
)

if st.button("Predict"):

    features = np.array([
        [
            gc,
            at,
            length,
            num_a,
            num_t,
            num_c,
            num_g,
            kmer,
            mutation
        ]
    ])

    prediction = model.predict(features)

    predicted_class = label_encoder.inverse_transform(prediction)

    st.success(f"Predicted Class: {predicted_class[0]}")