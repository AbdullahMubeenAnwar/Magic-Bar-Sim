import streamlit as st
import json
import os
from helper_funtions import load_user_profile, read_username

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

    h3 {
    color: #a64dff; /* Lighter shade of purple */
    text-align: center;
    font-size: 1em;
    
    }

    div.stButton > button {
        color: white;
        background-color: #4b0082;
        border-radius: 12px;
        font-size: 1.2em;
        padding: 10px 20px;
        margin: 10px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px;
    }

    div.stButton > button:hover {
        background-color: #800080;
    }
    </style>
    """, unsafe_allow_html=True)

def stats_page(username):
    # Load user profile data
    user_profile = load_user_profile(username)
    if user_profile is None:
        st.error("User profile not found.")
        return

    # Page title
    st.markdown("<h1 style='text-align: center; color: #4b0082;'>Player Statistics</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Display user stats
        st.markdown("<h2 style='text-align: center; color: #800080;'>General Stats</h3>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"<h3>Username: {user_profile['username']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>XP: {user_profile['XP']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Health: {user_profile['Health']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Mana: {user_profile['Mana']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Reputation: {user_profile['Reputation']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Wisdom: {user_profile['Reputation']}</h3>", unsafe_allow_html=True)

    with col2:
        # Additional stats section
        st.markdown("<h2 style='text-align: center; color: #800080;'>Additional Stats</h3>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"<h3>White Magic Proficiency (WMP): {user_profile['WMP']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Black Magic Proficiency (BMP): {user_profile['BMP']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Corruption: {user_profile['Corruption']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Moral Alignment: {user_profile['Moral_Alignment']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Potion Mastery: {user_profile['Potion_Mastery']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Influence: {user_profile['Influence']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>Quests Completed: {user_profile['Quests_Completed']}</h3>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    # Button to check leaderboard
    if st.button("Continue Playing"):
        st.switch_page("pages/act1.py")

if __name__ == "__main__":
    stats_page(read_username())