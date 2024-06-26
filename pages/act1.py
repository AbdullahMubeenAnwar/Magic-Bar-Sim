import streamlit as st
from helper_funtions import load_user_profile, save_user_profile, read_username, display_changes, update_stats_v2

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

def act1(username):
    profile = load_user_profile(username)
    
    if 'act1_step' not in profile:
        profile['act1_step'] = 0

    if profile['act1_step'] == 0:
        st.markdown("""
        ## The Hidden Entrance

        In a mystical world where magic flows through the very air, you stumble upon a hidden entrance within an enchanted forest. Intrigued by a faint glow, you venture forth and find yourself standing before the mysterious bar known as **𝓔𝓵𝓲𝔁𝓲𝓻𝓼 𝓸𝓯 𝓐𝓻𝓬𝓪𝓷𝓪**.
        """)
        if st.text_input("Type 'enter' to step inside:").strip().lower() == "enter":
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 1:
        st.markdown("---")
        st.write("You enter the bar and are greeted by a shimmering interior adorned with arcane symbols and shelves filled with magical potions.")
        if st.text_input("Type 'explore' to look around:").strip().lower() == "explore":
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 2:
        st.markdown("---")
        st.markdown("""
        ## Meeting Eldric

        As you explore, a figure emerges from the shadows. It is Eldric, the enigmatic bartender and guardian of ancient magical knowledge. His eyes sparkle with a hint of magic as he welcomes you.
        """)
        if st.text_input("Type 'greet' to greet Eldric:").strip().lower() == "greet":
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 3:
        st.markdown("---")
        st.write("Eldric: Welcome, traveler. You have found the 𝓔𝓵𝓲𝔁𝓲𝓻𝓼 𝓸𝓯 𝓐𝓻𝓬𝓪𝓷𝓪, a sanctuary for those seeking the wonders of magic through potions and elixirs.")
        if st.text_input("Type 'listen' to listen to Eldric:").strip().lower() == "listen":
            changes = update_stats_v2(profile, {'XP': 5, 'Mana': 10})
            display_changes(profile, changes)
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 4:
        st.markdown("---")
        st.write("Eldric gestures towards the shelves filled with bottles of various shapes and sizes, each containing swirling, colorful liquids.")
        if st.text_input("Type 'observe' to observe the potions:").strip().lower() == "observe":
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 5:
        st.markdown("---")
        st.write("Eldric: Here, you will learn the secrets of our potions. They range from enhancing your abilities with white magic to delving into the depths of black magic's power.")
        if st.text_input("Type 'understand' to acknowledge:").strip().lower() == "understand":
            changes = update_stats_v2(profile, {'XP': 5, 'WMP': 10})
            display_changes(profile, changes)
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 6:
        st.markdown("---")
        st.write("Eldric: Allow me to introduce you to the basics. This is a vial of basic white magic potion.")
        if st.text_input("Type 'drink' to drink the potion:").strip().lower() == "drink":
            st.write("You feel a surge of energy as you drink the potion. Your senses sharpen, and a faint glow surrounds you momentarily.")
            changes = update_stats_v2(profile, {'XP': 10, 'Potion_Mastery': 1})
            display_changes(profile, changes)
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 7:
        st.markdown("---")
        st.write("Eldric: This is just the beginning of your journey. Explore the bar, learn from the potions, and uncover the mysteries that lie within.")
        if st.text_input("Type 'explore' to explore the bar:").strip().lower() == "explore":
            profile['act1_step'] += 1
            save_user_profile(username, profile)

    if profile['act1_step'] == 8:
        st.markdown("---")
        st.write("Eldric: Remember, the 𝓔𝓵𝓲𝔁𝓲𝓻𝓼 𝓸𝓯 𝓐𝓻𝓬𝓪𝓷𝓪 holds many secrets waiting to be discovered. Enjoy your exploration, young wizard.")
        st.markdown("---")
        st.markdown("""
        ## Conclusion

        Act 1 concludes with Eldric's encouraging words, leaving you to explore the bar and contemplate the magical possibilities that await.
        """)
        save_user_profile(username, profile)
        if st.button("Continue your journey"):
            st.switch_page("pages/act2.py")

if __name__ == "__main__":
    act1(read_username())