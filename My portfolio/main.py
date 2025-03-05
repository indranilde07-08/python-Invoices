import streamlit as st
import pandas as pd
col1 , col2 = st.columns(2)

with col1:
    st.image("images/481217973_1842540879848818_8357691637776820431_n.png",width= 500)

with col2:
    st.title("Indranil de")
    content = """
    Hi, I am Indranil De! I graduated in 2024 in Electronic and Communication Engineering. 
    I am very interested in Python programming, automation, data processing, and data analysis. 
    This portfolio shows my skills 
    and what I have built in projects.
    """

    st.info(content)
content2 = """
          Below you can find some of the apps I have bulit in python.
          Feel free contact me!
           """
st.subheader(content2)

col3, empty_column, col4 = st.columns([2,1,2])

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index,item in df[:10].iterrows(): #Iterates over DataFrame rows
        st.header(item["title"])#Gets the title for that row
        st.write(item["description"])
        st.image("images/"+item["image"])
        st.write(f"[Source Code]({item['url']})")


with col4:
    for index,item in df[10:].iterrows():
        st.header(item["title"])
        st.write(item["description"])
        st.image("images/"+item["image"])
        st.write(f"[Source Code]({item['url']})")
