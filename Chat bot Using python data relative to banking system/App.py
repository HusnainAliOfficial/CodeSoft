import streamlit as st
import subprocess


st.title("Tic Tac TOe AI ")

user_input = st.text_input("Type 'bye' to close the app:")

if user_input.lower() == 'bye':
    st.write("Closing the app...")
    subprocess.Popen(["pkill", "streamlit"])
if st.button("Clear Content"):
    st.write("")
if st.button("Generate"):
    generated_text = cb.chat_with_user(user_input)
    st.write("Generated Text:", generated_text)


