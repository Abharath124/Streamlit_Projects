import streamlit as st


st.title("CHAI MAKER APP")

if st.button("Make chai"):
      st.success("Your chai is being brewed")

add_masala = st.checkbox("Add masala")
if add_masala:
      st.write("Masala added to your chai..")

tea_type = st.radio("Pick your chai type...", ["Milk", "Water", "2-spoon sugar"])
st.write(f"Selected base{tea_type}")


sugar= st.slider("Sugar level",0,10,2)


cups =  st.number_input("How many number cups:",min_value = 1,max_value = 10 , step=1)
st.write(f"Selected sugar level:",{cups})

name = st.text_input("Enter your name:")
if name:
      st.write(f"Welcome , {name} ! your chai is on the way")



dob = st.date_input("Enter your dat of birth:")
st.write(f"your DOB is : {dob} ")