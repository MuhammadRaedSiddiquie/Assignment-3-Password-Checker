import streamlit as st
import re
st.set_page_config(page_title="Python Password Checker", page_icon=":guardsman:", layout="wide")
st.title("Python Password Checker")
st.write("This is a simple password checker that checks the strength of your password. ")

password = st.text_input("Enter your password", type="password")

score=0

if password:
    # Check length
    if len(password) < 8:
        st.warning("Password must be at least 8 characters long.")
    else:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        st.warning("Password must contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        st.warning("Password must contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        st.warning("Password must contain at least one digit.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        st.warning("Password must contain at least one special character (@, $, !, %, *, ?, &).")
    # Check for common passwords
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "111111", "123123"]
    if password in common_passwords:
        st.warning("Password is too common. Please choose a different password.")
    else:
        score += 1
    if score == 6:
        st.success("Password is strong!")
    elif score >= 4:
        st.success("Password is medium.")   
    else:
        st.warning("Password is weak.")
    st.write("Password strength score: ", score)
    
