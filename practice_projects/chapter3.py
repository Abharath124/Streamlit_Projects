import streamlit as st

st.title("Chai Taste Poll")

col1 ,col2 = st.columns(2)

with col1:
      st.header("Masala Chai")
      st.image("https://images.pexels.com/photos/814264/pexels-photo-814264.jpeg?auto=compress&cs=tinysrgb&w=600",width=200)
      vote1 = st.button("Vote for masala Chai")

with col2:
      st.header("Ginger Chai")
      st.image("https://images.pexels.com/photos/13220364/pexels-photo-13220364.jpeg?auto=compress&cs=tinysrgb&w=600",width=200)
      vote2 = st.button("Vote for ginger Chai")

if vote1:
      st.success("Thanks for voting for Masala Chai!")
elif vote2:
      st.success("Thanks for voting for ginger chai")


name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("Select your favorite tea:", ["Masala Chai", "Ginger Chai"])

st.write(f"Welcome {name} and your {tea} is getting ready")

with st.expander("Chai making instruction"):
      st.write("""
    1. Boil water with tea leaves.  
    2. Add milk and spices.  
    3. Serve hot.
    """)
      
st.markdown('### Welcome to my chai APP')
st.markdown('> backquote')