import streamlit as st

st.title("STUDENT REGISTRATION FORM")
st.image("VVIT_Logo.png", width=100)
n=st.text_input("NAME")
e=st.text_input("EMAIL")
a=st.number_input("AGE", 0, 100, 18)
num=st.number_input("PHONE NUMBER", 0, 9999999999,0)
s=st.selectbox("select your course",["CSE","CSM","ECE","MECH","CIVIL"])
add=st.text_area("ADDRESS")
if st.button("REGISTER"):
    if n and e and a and num and s and add:
        st.image("fake.png", width=500)
    else:
        st.error("PLEASE FILL ALL THE FIELDS")    
    
