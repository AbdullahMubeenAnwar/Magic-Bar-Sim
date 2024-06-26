import os
import json
import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        color: #4b0082;
        font-size: 3em;
    }
    """, unsafe_allow_html=True)

def read_player_data(folder_path, important_stats):
    player_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):  # Assuming player data files have .json extension
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                # Select only important stats from the player's data
                selected_data = {key: data[key] for key in important_stats if key in data}
                player_data.append(selected_data)
    return player_data

def show_leaderboard(player_data, important_stats, sort_by='XP', ascending=False):
    # Sort player data based on sort_by stat
    player_data_sorted = sorted(player_data, key=lambda x: x.get(sort_by, 0), reverse=ascending)

    # Prepare data for table display
    leaderboard_data = []
    for index, player_stats in enumerate(player_data_sorted):
        row = {'Rank': index + 1}  # Start index from 1
        for stat_name, value in player_stats.items():
            row[stat_name] = value
        leaderboard_data.append(row)

    # Create a DataFrame from leaderboard data
    df_leaderboard = pd.DataFrame(leaderboard_data)
    st.dataframe(df_leaderboard.set_index('Rank')[important_stats].style.set_properties(**{'text-align': 'center'}).hide_index())

if __name__ == "__main__":
    folder_path = 'Players' 
    important_stats = ['username', 'XP', 'Wisdom', 'Health', 'Mana', 'WMP']  # Define the stats to display

    player_data = read_player_data(folder_path, important_stats)

    if len(player_data) > 0:
        st.title("Leaderboard")
        show_leaderboard(player_data, important_stats, sort_by='XP', ascending=False)
    else:
        st.write("No player data found. Ensure your folder_path is correct and contains valid JSON files.")
