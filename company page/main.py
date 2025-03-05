import streamlit as st
import lorem
import pandas as pd


st.set_page_config(layout="wide")
st.title("The Best Company")

random_text = lorem.paragraph()
st.write(random_text)

st.subheader("Our Team")
col1, col2, col3 = st.columns([10,10,10])
df = pd.read_csv("data.csv", sep=",")
print(df)

with col1:
    for index, item in df[:4].iterrows():
        st.subheader(f'{item["first name"].title()} {item["last name"].title()}')
        st.write(item["role"])
        st.image("images/"+item["image"])

with col2:
    for index, item in df[4:8].iterrows():
        st.subheader(f'{item["first name"].title()} {item["last name"].title()}')
        st.write(item["role"])
        st.image("images/"+item["image"])

with col3:
    for index, item in df[8:].iterrows():
        st.subheader(f'{item["first name"].title()} {item["last name"].title()}')
        st.write(item["role"])
        st.image("images/"+item["image"])
