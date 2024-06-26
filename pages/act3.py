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

def act3(username):
    profile = load_user_profile(username)
    
    if 'act3_step' not in profile:
        profile['act3_step'] = 0
        profile['act3_choice'] = ""

    if profile['act3_step'] == 0:
        st.markdown("""
        ## The Lure of Power

        Having mastered the basics of white magic, Eldric now deems you ready to learn about the more potent but risky black magic.
        """)
        if st.text_input("Type 'learn' to start learning about black magic:").strip().lower() == "learn":
            changes = update_stats_v2(profile, {'XP': 5})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 1:
        st.markdown("---")
        st.write("""
        Eldric: You have shown great promise in white magic. However, there exists a darker, more powerful form of magic: black magic.
        It offers immense power but comes with significant risks and moral dilemmas.
        """)
        if st.text_input("Type 'understand' to acknowledge the risks:").strip().lower() == "understand":
            changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 2})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 2:
        choice = st.radio("Choose your path:", ('Embrace black magic and its power?', 'Focus on mastering white magic and avoiding the risks of black magic?'))
        if st.button("Confirm Choice"):
            profile['act3_choice'] = choice
            if profile['act3_choice'] == "Embrace black magic and its power?":
                changes = update_stats_v2(profile, {'XP': 10, 'BMP': 5})
                display_changes(profile, changes)
                profile['act3_step'] += 1
            elif profile['act3_choice'] == "Focus on mastering white magic and avoiding the risks of black magic?":
                changes = update_stats_v2(profile, {'XP': 5, 'Wisdom': 5})
                display_changes(profile, changes)
                profile['act3_step'] = 8
            save_user_profile(username, profile)

    if profile['act3_step'] == 3:
        st.markdown("---")
        st.write("You decide to embrace black magic, driven by the allure of its power.")
        if st.text_input("Type 'continue' to continue your journey:").strip().lower() == "continue":
            changes = update_stats_v2(profile, {'BMP': 5, 'XP': 5})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 4:
        st.markdown("---")
        st.write("""
        As you begin to explore the potential of black magic, you encounter a rival wizard who challenges you to a duel.
        Rival Wizard: So, you have dabbled in the dark arts. Let's see if you can handle the true power of black magic.
        """)
        if st.text_input("Type 'duel' to accept the challenge:").strip().lower() == "duel":
            changes = update_stats_v2(profile, {'BMP': 10, 'XP': 5, 'Reputation': -2})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 5:
        st.markdown("---")
        st.write("""
        The duel is intense, with both of you wielding dark energies. You can feel the corruption trying to seep into your soul with each spell cast.
        """)
        if st.text_input("Type 'fight' to continue the duel:").strip().lower() == "fight":
            changes = update_stats_v2(profile, {'BMP': 10, 'XP': 5, 'Corruption': 5})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 6:
        st.markdown("---")
        st.write("""
        With a final powerful spell, you manage to defeat the rival wizard. The victory is bittersweet, as you feel the weight of the dark magic on your spirit.
        """)
        if st.text_input("Type 'reflect' to reflect on your actions:").strip().lower() == "reflect":
            changes = update_stats_v2(profile, {'BMP': 5, 'XP': 10, 'Corruption': 5})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 7:
        st.markdown("---")
        st.write("""
        Eldric: You have tasted the power of black magic and survived. But remember, every use of dark power leaves a mark on your soul.
        Choose your path wisely.
        """)
        if st.text_input("Type 'continue' to move forward:").strip().lower() == "continue":
            changes = update_stats_v2(profile, {'Wisdom': 5, 'XP': 5})
            display_changes(profile, changes)
            profile['act3_step'] += 2
            save_user_profile(username, profile)

    if profile['act3_step'] == 8:
        st.markdown("---")
        st.write("Eldric: It is wise to tread carefully. The path of white magic offers its own rewards and protections.")
        if st.text_input("Type 'continue' to continue your journey of white magic:").strip().lower() == "continue":
            changes = update_stats_v2(profile, {'WMP': 15, 'XP': 5, 'Wisdom': 15})
            display_changes(profile, changes)
            profile['act3_step'] += 1
            save_user_profile(username, profile)

    if profile['act3_step'] == 9:
        st.markdown("---")
        st.write("""
        With Eldric's warning echoing in your mind, you contemplate the future and the choices that lie ahead.
        """)
        st.markdown("""
        ---
        ## Conclusion

        Act 3 concludes with your initiation into the realm of black magic, facing its temptations and the moral challenges it presents.
        """)
        if st.button("Continue your journey"):
            st.switch_page("pages/act4.py")

if __name__ == "__main__":
    act3(read_username())