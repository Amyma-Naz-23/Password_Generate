import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")

st.markdown("""
### WELCOME TO PASSWORD STRENGTH CHECKER! 🔒  
Use this tool to check the strength of your password.  
We will tell you how strong your **password** is and what you can do to make it **stronger**.
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Check for uppercase & lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters.")

    # Check for at least one number
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one number.")

    # Check for at least one special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character.")

    # Determine password strength
    if score == 4:
        st.success("✅ Your password is strong! 🎉")
    elif score == 3:
        st.warning("🔶 Your password is medium. Consider adding more complexity.")
    else:
        st.error("🔴 Your password is weak. Please make it stronger.")

    # Display improvement suggestions if necessary
    if feedback:
        st.markdown("## 💡 Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter a password to check its strength.")
