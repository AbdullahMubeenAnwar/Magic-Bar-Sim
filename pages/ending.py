import streamlit as st

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

st.title("𝓔𝓵𝓲𝔁𝓲𝓻𝓼 𝓸𝓯 𝓐𝓻𝓬𝓪𝓷𝓪 - The End")

st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <h2>Congratulations!</h2>
    <p>You have completed your journey through the Elixirs of Arcana.</p>
    <p>Your choices have shaped the destiny of the bar and its patrons.</p>
    <p>Thank you for playing!</p>
    <p><strong>May your magic always be strong.</strong></p>
</div>
""", unsafe_allow_html=True)

if st.button("View Leaderboard"):
    st.switch_page("pages/leaderboard.py")

# <img src="https://via.placeholder.com/300x200.png?text=Elixirs+of+Arcana" alt="Elixirs of Arcana" style="border-radius: 10px;">