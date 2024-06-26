import streamlit as st
import json
import os

def load_user_profile(username):
    try:
        with open(f"./Players/{username}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def save_user_profile(username, data):
    if not os.path.exists('./Players'):
        os.makedirs('./Players')
    with open(f"./Players/{username}.json", "w") as file:
        json.dump(data, file)

def update_stats_v2(profile, updates):
    changes = {}
    for stat, change in updates.items():
        if stat in profile:
            profile[stat] += change
            changes[stat] = change
    save_user_profile(profile['username'], profile)
    return changes

def display_changes(profile, changes):
    for stat, change in changes.items():
        if change > 0:
            st.write(f"**{stat}**: {profile[stat]} (↑ {change}) :green_heart:")
        elif change < 0:
            st.write(f"**{stat}**: {profile[stat]} (↓ {change}) :red_circle:")

def list_users():
    return [f.split('.')[0] for f in os.listdir('./Players') if f.endswith('.json')]

def create_new_user(username, password):
    profile = {
        "username": username,
        "password": password,
        'WMP': 0,  # White Magic Proficiency
        'BMP': 0,  # Black Magic Proficiency
        'Corruption': 0 ,
        'Reputation': 50,  # Neutral starting reputation
        'Mana': 100,  # Starting mana
        'Health': 100,  # Starting health
        'XP': 0,  # Experience Points
        'Wisdom': 0,  # Inventory list
        'Quests_Completed': 0,  # Number of quests completed
        'Moral_Alignment': 'Neutral',  # Neutral starting moral alignment
        'Potion_Mastery': 0,  # Potion Mastery
        'Influence': 0,  # Influence
    }
    save_user_profile(username, profile)
    return profile

def verify_password(username, password):
    profile = load_user_profile(username)
    return profile and 'password' in profile and profile['password'] == password

def store_username(username):
    with open('pages/logged_in_as.txt', 'w') as f:
        f.write(username)

def read_username():
    username = None
    try:
        with open('pages/logged_in_as.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                username = lines[-1].strip()
    except FileNotFoundError:
        st.write("No logged in user found.")
    return username








