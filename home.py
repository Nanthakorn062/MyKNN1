import streamlit as st
import pandas as pd 

st.title("☝︎☝︎☝︎Website Developing using Python☝︎☝︎☝︎")
st.header("Website Developing using Python")

st.image('/image/PP.jpg')
st.subheader("Nanthakorn Silpachai")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.write(dt.head(10))