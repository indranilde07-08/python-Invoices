import streamlit as st

st.set_page_config(layout="wide")#wide on your website
col1 , col2 = st.columns(2)

with col1:
    st.image("images/481217973_1842540879848818_8357691637776820431_n.png",width= 500)

with col2:
    st.title("Indranil de")
    content = """
    Hi, I am Indranil De. I graduated in 2024 in Electronic and Communication Engineering. 
    I am very interested in Python programming, automation, data processing, and data analysis. 
    This portfolio shows my skills 
    and what I have built in projects.
    """
    st.info(content)
