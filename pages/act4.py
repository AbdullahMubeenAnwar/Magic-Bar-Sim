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

def act4(username):
    profile = load_user_profile(username)
    
    if 'act4_step' not in profile:
        profile['act4_step'] = 0

    if profile['act4_step'] == 0:
        st.markdown("""
        ## The Ominous Warning

        A dark entity threatens the bar and its patrons. Eldric gathers you and the other patrons to warn you of the impending danger.
        """)
        if st.text_input("Type 'warn' to listen to Eldric's warning:").strip().lower() == "warn":
            changes = update_stats_v2(profile, {'XP': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 1:
        st.markdown("---")
        st.write("""
        Eldric: The bar is under threat from a dark entity known as Malakar. This being seeks to drain the magical essence from this place and everyone within it.
        """)
        if st.text_input("Type 'ask' to ask Eldric about Malakar:").strip().lower() == "ask":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 2})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 2:
        st.markdown("---")
        st.write("""
        Eldric: Malakar is a powerful dark sorcerer from my past. His power is immense, but his heart is consumed by darkness. We must prepare for his arrival.
        """)
        if st.text_input("Type 'prepare' to prepare for Malakar's arrival:").strip().lower() == "prepare":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 2})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 3:
        st.markdown("---")
        st.write("""
        Eldric leads you to a hidden chamber beneath the bar. Inside, you find ancient tomes and powerful artifacts that can aid you in the upcoming trials.
        """)
        if st.text_input("Type 'explore' to explore the hidden chamber:").strip().lower() == "explore":
            changes = update_stats_v2(profile, {'XP': 5, 'WMP': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 4:
        st.markdown("---")
        st.write("""
        Eldric: These tomes contain spells and knowledge from ages past. Use them wisely, as they will be crucial in our fight against Malakar.
        """)
        if st.text_input("Type 'study' to study the tomes and artifacts:").strip().lower() == "study":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 5, 'WMP': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 5:
        st.markdown("---")
        st.write("""
        As you study, you discover spells that enhance your magical abilities. Eldric helps you master these spells, preparing you for the trials ahead.
        """)
        if st.text_input("Type 'master' to master the new spells:").strip().lower() == "master":
            changes = update_stats_v2(profile, {'XP': 10, 'WMP': 10})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 6:
        st.markdown("---")
        st.write("""
        Eldric: The time has come. Malakar approaches. We must stand together and face him.
        """)
        if st.text_input("Type 'face' to face Malakar:").strip().lower() == "face":
            changes = update_stats_v2(profile, {'XP': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 7:
        st.markdown("---")
        st.write("""
        As you emerge from the chamber, you feel the ground shake. The air grows colder, and a dark mist envelops the bar. Malakar appears, his eyes burning with malevolence.
        Malakar: So, Eldric, you have gathered your little apprentices. Let's see if they can withstand my power.
        """)
        if st.text_input("Type 'confront' to confront Malakar:").strip().lower() == "confront":
            changes = update_stats_v2(profile, {'XP': 5, 'BMP': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 8:
        st.markdown("---")
        st.write("""
        You and Eldric engage Malakar in a fierce battle. Spells clash, and the bar trembles under the onslaught of magic.
        """)
        if st.text_input("Type 'fight' to continue the battle:").strip().lower() == "fight":
            changes = update_stats_v2(profile, {'XP': 10, 'BMP': 10})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 9:
        st.markdown("---")
        st.write("""
        The battle reaches a critical point. Malakar summons dark minions to aid him, and you must fend them off while continuing to fight him.
        """)
        if st.text_input("Type 'defend' to defend against the minions:").strip().lower() == "defend":
            changes = update_stats_v2(profile, {'XP': 10, 'BMP': 5, 'Defense': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 10:
        st.markdown("---")
        st.write("""
        With a final, powerful spell, you manage to weaken Malakar. Eldric seizes the opportunity to banish him, but it takes a toll on his own strength.
        """)
        if st.text_input("Type 'banish' to help Eldric banish Malakar:").strip().lower() == "banish":
            changes = update_stats_v2(profile, {'XP': 15, 'BMP': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 11:
        st.markdown("---")
        st.write("""
        Malakar: This isn't over... I will return...
        With those words, Malakar vanishes into the void, but you know the threat isn't completely gone.
        """)
        if st.text_input("Type 'rest' to rest after the battle:").strip().lower() == "rest":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 12:
        st.markdown("---")
        st.write("""
        Eldric: You have done well, young wizard. But remember, the darkness always finds a way back. We must remain vigilant.
        """)
        if st.text_input("Type 'understand' to acknowledge Eldric's warning:").strip().lower() == "understand":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 5})
            display_changes(profile, changes)
            profile['act4_step'] += 1
            save_user_profile(username, profile)

    if profile['act4_step'] == 13:
        st.markdown("---")
        st.write("""
        The bar slowly returns to its serene state, but the memory of the battle lingers. You know that the fight against darkness is far from over.
        """)
        st.markdown("""
        ---
        ## Conclusion

        Act 4 concludes with the temporary banishment of Malakar, but the looming threat remains. You are more powerful and more aware of the challenges that lie ahead.
        """)
        if st.button("Continue your journey"):
            st.switch_page("pages/act5.py")

if __name__ == "__main__":
    act4(read_username())