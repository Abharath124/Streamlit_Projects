import streamlit as st
from datetime import date


st.title("-------AGE CALCULATOR-------")
name = st.text_input("Enter your name:")

#date range
min_val = date(1800,1,1)
max_val = date.today()

cal = st.date_input("Enter your Current:",value=date.today())
st.write(f"Your current date: {cal}")


cal2 = st.date_input("Enter your Birth Date:" , min_value=min_val , max_value = max_val , value = date(2000,1,1))
st.write(f"Your birth date: {cal2}")

# resul = cal - cal2
age = cal.year - cal2.year - ((cal.month, cal.day) < (cal2.month, cal2.day))
st.write(f"{name} Your age is : {age} years")