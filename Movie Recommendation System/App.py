import streamlit as st
import subprocess      
import model as md


st.title("Movies Recommendation System")

user_input = st.text_input("Type Movie name 'bye' to close the app:")

if user_input.lower() == 'bye':
    st.write("Closing the app...")
    subprocess.Popen(["pkill", "streamlit"])
if st.button("Generate"):
   st.write("")
   text=md.recommend(user_input)
   st.write(text)
    

