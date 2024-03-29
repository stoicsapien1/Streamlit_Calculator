import streamlit as st
st.title("Python Calculator➕➖✖️❤️")
a= st.text_input("Enter First number ")
b=st.text_input("Enter Second number")
try:
    a = float(a)
    b = float(b)
except ValueError:
    st.write("Please enter valid numeric values.")
options=["Add","Substract","Multiply","Divide"]
opr = st.radio("Choose an option:", options)
if type(a)==float and type(b)==float:
    if opr=="Add":
        result=a+b
    elif opr=="Substract":
        result=a-b
    elif opr=="Multiply":
        result=a*b
    elif opr=="Divide":
        if b!=0:
            result=a/b
        else:
            result="Can't divide by zero"
    if st.button("Calculate"):
        st.write(f"Result: {result}")
else:
    st.write("Result: Please enter Integer or Float Data Type💀💀💀⚡⚡")
