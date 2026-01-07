import streamlit as st

def main():
    st.set_page_config(page_title="Predicción de activos 2026", page_icon="💲", layout="centered")

    st.title("Predicción de activos 2026")
    st.write("**¿Qué tipo de información quiere?**")

    opcion = st.radio(
        "Seleccione una opción:",
        ("Situación actual de Bitcoin", "Predicción del precio de Bitcoin"),
        index=None
    )

    if opcion == "Situación actual de Bitcoin":
        st.page_link("pages/informacion.py", label="Situación actual", icon="ℹ️")

# Local: python -m streamlit run streamlit_tutorial.py
# Streamlit Sharing 