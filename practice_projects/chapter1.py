import streamlit as st
st.title("Hello chai App")
st.subheader("I am just simply creating app for learning purpose")
st.text("Welcome to my simple app")
st.write("Choose your option below:")


chai = st.selectbox("Choose your fav job role:",["Machine Learning Engineer",
"Data Scientist", "Data Engineer", "AI Engineer", "Software Engineer"])


st.write(f"You choose:{chai}. Good nowadays this is demand job...") 

st.success("You selected value will be Successs...")