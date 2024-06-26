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

def act2(username):
    profile = load_user_profile(username)
    
    if 'act2_step' not in profile:
        profile['act2_step'] = 0
        profile['act2_choice'] = ""

    if profile['act2_step'] == 0:
        st.markdown("""
        ## Advanced White Magic

        Having gained some basic knowledge of white magic, Eldric now trusts you with more potent and advanced potions.
        """)
        if st.text_input("Type 'learn' to start learning advanced white magic:").strip().lower() == "learn":
            changes = update_stats_v2(profile, {'XP': 5})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 1:
        st.markdown("---")
        st.write("""
        Eldric: You have shown great potential. Now, it's time to delve deeper into the art of white magic.
        Are you willing to accept this journey?
        """)
        if st.text_input("Type 'accept' to accept the potion:").strip().lower() == "accept":
            changes = update_stats_v2(profile, {'XP': 5, 'Reputation': 2})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 2:
        st.markdown("""
        Eldric begins to teach you about advanced white magic potions. These potions are known to have profound healing and protective effects.
        """)
        if st.text_input("Type 'learn' to learn more:").strip().lower() == "learn":
            changes = update_stats_v2(profile, {'WMP': 5, 'XP': 5})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 3:
        st.markdown("---")
        st.write("Eldric: These potions can mend even the gravest of wounds and create barriers that are nearly impenetrable. However, they require a great deal of skill to master.")
        if st.text_input("Type 'practice' to practice with the potions:").strip().lower() == "practice":
            changes = update_stats_v2(profile, {'WMP': 10})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 4:
        st.markdown("---")
        st.write("You spend hours practicing with the potions, feeling your skills and understanding of white magic grow.")
        choice = st.radio("Choose your path:", ('Continue practicing to master the potions?', 'Ask Eldric about the next steps in your journey?'))
        if st.button("Confirm Choice"):
            profile['act2_choice'] = choice
            if profile['act2_choice'] == "Continue practicing to master the potions?":
                changes = update_stats_v2(profile, {'WMP': 10, 'XP': 5})
                display_changes(profile, changes)
                profile['act2_step'] += 1
            elif profile['act2_choice'] == "Ask Eldric about the next steps in your journey?":
                changes = update_stats_v2(profile, {'Reputation': 5, 'XP': 5})
                display_changes(profile, changes)
                profile['act2_step'] = 6
            save_user_profile(username, profile)

    if profile['act2_step'] == 5:
        st.markdown("---")
        st.write("You continue practicing diligently, honing your skills to perfection.")
        if st.text_input("Type 'talk' to talk to Eldric about the next steps:").strip().lower() == "talk":
            changes = update_stats_v2(profile, {'WMP': 5, 'XP': 5})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 6:
        st.markdown("---")
        st.write("""
        Eldric: Excellent. Now, you must practice your new abilities. There are patrons in need of your help.
        Go and assist them to strengthen your skills.
        """)
        if st.text_input("Type 'assist' to go and help the patrons:").strip().lower() == "assist":
            changes = update_stats_v2(profile, {'Reputation': 5, 'XP': 10})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 7:
        st.markdown("---")
        st.write("""
        You approach a group of patrons. One of them, a young elf, looks at you with pleading eyes.
        Elf: Please, can you help heal my injured friend?
        """)
        if st.text_input("Type 'heal' to heal the injured friend:").strip().lower() == "heal":
            changes = update_stats_v2(profile, {'WMP': 5, 'XP': 10, 'Reputation': 5})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 8:
        st.markdown("---")
        st.write("""
        As you channel your newly enhanced healing abilities, the elf's friend begins to recover rapidly.
        The patrons are amazed by your power.
        """)
        if st.text_input("Type 'thank' to receive their gratitude:").strip().lower() == "thank":
            changes = update_stats_v2(profile, {'Reputation': 10, 'XP': 5})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 9:
        st.markdown("---")
        st.write("""
        Eldric: Well done. Your compassion and skill have earned you the trust of these patrons.
        There is much more to learn, but you are on the right path.
        """)
        if st.text_input("Type 'continue' to proceed:").strip().lower() == "continue":
            changes = update_stats_v2(profile, {'WMP': 5, 'XP': 5, 'Reputation': 5})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 10:
        st.markdown("---")
        st.write("""
        Eldric: The journey of mastering white magic is long and arduous, but with each step, you grow stronger and wiser.
        Continue to seek knowledge and help those in need.
        """)
        if st.text_input("Type 'explore' to continue your journey:").strip().lower() == "explore":
            changes = update_stats_v2(profile, {'WMP': 5, 'XP': 10})
            display_changes(profile, changes)
            profile['act2_step'] += 1
            save_user_profile(username, profile)

    if profile['act2_step'] == 11:
        st.markdown("---")
        st.write("""
        As you finish your conversation with Eldric, you feel a sense of purpose and readiness for the challenges ahead.
        """)
        st.markdown("""
        ---
        ## Conclusion

        Act 2 concludes with your growing mastery of white magic and a strengthened resolve to help those in need.
        """)
        save_user_profile(username, profile)
        if st.button("Continue your journey"):
            st.switch_page("pages/act3.py")

if __name__ == "__main__":
    act2(read_username())