import streamlit as st
import json
import os
from helper_funtions import verify_password, load_user_profile, store_username, create_new_user

st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        color: #4b0082;
        text-align: center;
        font-size: 3em;
    }

    h2 {
        color: #800080;
        text-align: center;
        font-size: 2em;
    }

    .stButton button {
        color: white !important;
        background-color: #4b0082 !important;
        border-radius: 12px !important;
        font-size: 1.2em !important;
        padding: 10px 20px !important;
        margin: 10px auto !important;
        display: block !important;
        width: 200px !important;
        text-align: center;
    }

    .stButton button:hover {
        background-color: #800080 !important;
    }

    .error {
        color: red;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

def login_page():
    if "login_failed" not in st.session_state:
        st.session_state["login_failed"] = False

    username = st.text_input("Username", key="username", placeholder="Enter your username", help="Your unique username")
    password = st.text_input("Password", type="password", key="password", placeholder="Enter your password", help="Your secure password")

    if st.session_state.login_failed:
        st.markdown("<p class='error'>Incorrect username or password.</p>", unsafe_allow_html=True)

    if st.button("Log In", key="login", help="Log in to your account"):
        if verify_password(username, password):
            st.session_state.user_profile = load_user_profile(username)
            st.write("Succesfully logged in!")
            store_username(username)
            st.switch_page("pages/stats.py")
        else:
            st.session_state.login_failed = True

    if st.button("Create New Account", key="create_account", help="Create a new account"):
        if username and password:
            if not load_user_profile(username):
                st.session_state.user_profile = create_new_user(username, password)
                st.write("Account created!")
                store_username(username)
                st.switch_page("pages/stats.py")
            else:
                st.markdown("<p class='error'>Username already exists. Choose a different username.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='error'>Please enter both username and password.</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.markdown("## 𝓔𝓵𝓲𝔁𝓲𝓻𝓼 𝓸𝓯 𝓐𝓻𝓬𝓪𝓷𝓪 ")
    login_page()