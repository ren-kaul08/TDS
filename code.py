import streamlit as st

name = "main"

def find_largest(*args):
    return max(args)

def main():
    st.title("Find the Largest Number")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: {largest}")

if name == "main":
    main()
