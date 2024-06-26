import streamlit as st

st.set_page_config(
    page_title="Elixirs of Arcana", page_icon=":crystal_ball:", initial_sidebar_state="collapsed"
)

def main_menu():
    st.title("𝓔𝓵𝓲𝔁𝓲𝓻𝓼 𝓸𝓯 𝓐𝓻𝓬𝓪𝓷𝓪")
    st.markdown("## 𝕬 𝕸𝖆𝖌𝖎𝖈𝖆𝖑 𝕬𝖉𝖛𝖊𝖓𝖙𝖚𝖗𝖊 𝕬𝖜𝖆𝖎𝖙𝖘")
    
    st.markdown("""
    ## 𝕾𝖊𝖙𝖙𝖎𝖓𝖌
    In a mystical world where magic flows through the very air, there exists a legendary bar called **Elixirs of Arcana** This bar is hidden deep within the enchanted forests, only accessible to those who truly believe in magic. The bar is run by an enigmatic bartender known as Eldric, who is rumored to be a powerful wizard himself. The bar offers a wide array of potions, elixirs, and concoctions that can enhance magical abilities and level up the drinker's powers.

    ## 𝓞𝓫𝓳𝓮𝓬𝓽𝓲𝓿𝓮
    Your goal is to level up your magical abilities by drinking different potions. Weaker potions enhance white magic (healing, protection), while stronger potions enhance black magic (destruction, offense). Choose your path wisely and uncover the secrets of the bar.
    
    Embark on a quest to uncover your mystic abilities. Navigate to the sidebar and invoke the 'Stats' scroll.""")
    
    st.markdown("---")
    
    if st.button("PLAY"):
        st.switch_page("pages\login.py")
    if st.button("LEADERBOARD"):
        st.switch_page("pages/leaderboard.py")

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

if __name__ == "__main__":
    main_menu()
    # st.write("Streamlit version:", st.__version__)



















# import streamlit as st
# from login import login_user

# def main_menu():
#     st.title("Elixirs of Arcana")
#     st.subheader("A Magical Adventure Awaits")
    
#     st.markdown("""
#     ### Setting
#     In a mystical world where magic flows through the very air, there exists a legendary bar called **Elixirs of Arcana** This bar is hidden deep within the enchanted forests, only accessible to those who truly believe in magic. The bar is run by an enigmatic bartender known as Eldric, who is rumored to be a powerful wizard himself. The bar offers a wide array of potions, elixirs, and concoctions that can enhance magical abilities and level up the drinker's powers.

#     ### Objective
#     Your goal is to level up your magical abilities by drinking different potions. Weaker potions enhance white magic (healing, protection), while stronger potions enhance black magic (destruction, offense). Choose your path wisely and uncover the secrets of the bar.
#     """)
    
#     st.markdown("---")
    
#     if st.button("PLAY"):
#         play_game()
#     if st.button("LEADERBOARD"):
#         st.switch_page("leaderboard")
        
# # Initialize session state
# if 'progress' not in st.session_state:
#     st.session_state.progress = 'start'
# if 'inventory' not in st.session_state:
#     st.session_state.inventory = []
# if 'quest_log' not in st.session_state:
#     st.session_state.quest_log = []
# if 'user_profile' not in st.session_state:
#     st.session_state.user_profile = None

# def play_game():
#     if st.session_state.progress == 'start':
#         st.write("Welcome to the Elixirs of Arcana!")
#         if st.button("Continue"):
#             st.session_state.progress = 'act1'
#             st.switch_page("act1")
#     elif st.session_state.progress == 'act1':
#         st.switch_page("act1")
#     elif st.session_state.progress == 'act2':
#         st.switch_page("act2")
#     elif st.session_state.progress == 'act3':
#         st.switch_page("act3")
#     elif st.session_state.progress == 'act4':
#         st.switch_page("act4")
#     elif st.session_state.progress == 'act5':
#         st.switch_page("act5")

# # Check for user authentication
# if st.session_state.user_profile is None:
#     login_user()
# else:
#     main_menu()