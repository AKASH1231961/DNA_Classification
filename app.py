import streamlit as st

st.set_page_config(
    page_title="DNA Classification App",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 DNA Classification App")

st.markdown("""
This application predicts the biological class of DNA samples using Machine Learning.

### Classes:
- Human
- Bacteria
- Virus
- Plant

Use the sidebar to navigate between pages.
""")

st.image(
    "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69",
    use_container_width=True
)