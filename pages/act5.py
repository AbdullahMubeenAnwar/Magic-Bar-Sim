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

def act5(username):
    profile = load_user_profile(username)
    
    if 'act5_step' not in profile:
        profile['act5_step'] = 0

    if profile['act5_step'] == 0:
        st.markdown("""
        ## The Aftermath

        After the intense battle with Malakar, the bar is in a state of uneasy calm. You feel a lingering darkness, indicating that Malakar’s influence is not completely eradicated.
        """)
        if st.text_input("Type 'reflect' to reflect on the recent events:").strip().lower() == "reflect":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 2})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 1:
        st.markdown("---")
        st.write("""
        As you rest, Eldric approaches you with a solemn expression.
        Eldric: We have won a battle, but the war is far from over. Malakar's power still lingers in this realm.
        """)
        if st.text_input("Type 'listen' to listen to Eldric:").strip().lower() == "listen":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 2})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 2:
        st.markdown("---")
        st.write("""
        Eldric: There is one final trial you must face. Malakar's essence has fused with the very fabric of magic in this place. You must choose how to confront it.
        """)
        if st.text_input("Type 'ask' to ask Eldric about the trial:").strip().lower() == "ask":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 2})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 3:
        st.markdown("---")
        st.write("""
        Eldric: You have two paths. Embrace the power of black magic to attempt to control and banish Malakar's essence forever, or uphold the purity of white magic to protect and heal, keeping Malakar's influence at bay.
        """)
        choice = st.radio("Choose your path:", ('Black Magic', 'White Magic'))
        if st.button("Confirm Choice"):
            profile['act5_choice'] = choice
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 4:
        st.markdown("---")
        if profile['act5_choice'] == 'Black Magic':
            st.write("""
            You decide to embrace the power of black magic. The allure of immense power is too strong to resist.
            Eldric: Be cautious. The path of black magic is fraught with peril and temptation.
            """)
            changes = update_stats_v2(profile, {'BMP': 100})
        else:
            st.write("""
            You choose to uphold the purity of white magic, focusing on protection and healing.
            Eldric: A wise choice. White magic will strengthen your resolve and shield against the darkness.
            """)
            changes = update_stats_v2(profile, {'BMP': 100})
        display_changes(profile, changes)
        if st.text_input("Type 'prepare' to prepare for the final trial:").strip().lower() == "prepare":
            if profile['act5_choice'] == 'Black Magic':
                changes = update_stats_v2(profile, {'XP': 5, 'BMP': 10})
            else:
                changes = update_stats_v2(profile, {'XP': 5, 'WMP': 10})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 5:
        st.markdown("---")
        st.write("""
        With your decision made, you gather your strength and step into the heart of the bar where the magical energies converge. The air crackles with power as you confront Malakar's essence.
        """)
        if st.text_input("Type 'confront' to confront Malakar's essence:").strip().lower() == "confront":
            changes = update_stats_v2(profile, {'XP': 50})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 6:
        st.markdown("---")
        if profile['act5_choice'] == 'Black Magic':
            st.write("""
            You harness the dark power within you, channeling it to overpower Malakar's essence. The struggle is intense, but you feel the dark magic responding to your command.
            """)
        else:
            st.write("""
            You call upon the purity of white magic, creating a protective barrier around you. The essence of Malakar crashes against it, but your resolve holds firm.
            """)
        if st.text_input("Type 'continue' to continue the trial:").strip().lower() == "continue":
            changes = update_stats_v2(profile, {'XP': 10})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 7:
        st.markdown("---")
        st.write("""
        The final confrontation pushes you to your limits. With a last burst of energy, you release your chosen magic, enveloping the essence of Malakar.
        """)
        if st.text_input("Type 'release' to release your magic:").strip().lower() == "release":
            changes = update_stats_v2(profile, {'XP': 100})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)

    if profile['act5_step'] == 8:
        st.markdown("---")
        if profile['act5_choice'] == 'Black Magic':
            st.write("""
            The dark magic consumes Malakar's essence, binding it under your control. The bar falls silent as the dark energies dissipate.
            Eldric: You have done it. But remember, with great power comes great responsibility. Use it wisely.
            """)
        else:
            st.write("""
            The white magic purifies Malakar's essence, dispersing the dark energy harmlessly. The bar is bathed in a warm, soothing light.
            Eldric: You have done it. Your purity and strength have saved us all.
            """)
        if st.text_input("Type 'finish' to conclude the journey:").strip().lower() == "finish":
            changes = update_stats_v2(profile, {'XP': 10, 'Wisdom': 5})
            display_changes(profile, changes)
            profile['act5_step'] += 1
            save_user_profile(username, profile)
        if profile['WMP'] > profile['BMP']:
            profile['Moral_Alignment'] = 'Positive'
        else:
            profile['Moral_Alignment'] = 'Negative'

    if profile['act5_step'] == 9:
        st.markdown("---")
        st.write("""
        The bar returns to its peaceful state, with Eldric and the patrons safe once more. Your journey has reached its end, but the lessons and powers you have gained will stay with you forever.
        """)
        st.markdown("""
        ---
        ## Conclusion

        Act 5 concludes with your ultimate choice shaping the future of the Elixirs of Arcana. Whether you embraced the power of black magic or upheld the purity of white magic, your legacy is now part of the bar's history.
        """)

        if st.button("Continue"):
            st.switch_page("pages/ending.py")

if __name__ == "__main__":
    act5(read_username())