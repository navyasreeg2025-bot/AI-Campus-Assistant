import streamlit as st

st.title("AI Campus Assistant")

query = st.text_input("Ask anything about campus")

if query:
    st.write("Answer will appear here")
