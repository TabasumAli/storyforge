import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment variables
api_key = os.getenv("groq_api_key")

# Initialize Groq client using the API key from .env
client = Groq(
    api_key=api_key,  # API key fetched securely from .env
)

# Function to generate the game environment
def generate_game_environment(environment):
    message = f"Describe the setting of a game in the environment: {environment}."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Function to generate the protagonist
def generate_protagonist(protagonist):
    message = f"Create a detailed description of the protagonist: {protagonist}."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Function to generate the antagonist
def generate_antagonist(antagonist):
    message = f"Create a detailed description of the antagonist: {antagonist}."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Function to generate the game story
def generate_game_story(environment, protagonist, antagonist):
    message = f"Create a compelling game story set in {environment}, featuring {protagonist} as the protagonist and {antagonist} as the antagonist."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


# Streamlit app title and description
st.title("StoryForge")
st.write("StoryForge is an app designed to help game developers generate comprehensive Game Design Documents by providing essential details about their game's environment, protagonist, and antagonist.")

# Sidebar for user input
st.sidebar.header("Game Details")
game_environment = st.sidebar.text_input("Enter the Game Environment:", placeholder="e.g., A dystopian city in the year 2142")
protagonist = st.sidebar.text_input("Enter the Protagonist:", placeholder="e.g., A young hacker with a mysterious past")
antagonist = st.sidebar.text_input("Enter the Antagonist:", placeholder="e.g., A corrupt government official controlling the city")

# Generate button
if st.sidebar.button("Generate"):
    if not game_environment or not protagonist or not antagonist:
        # If any of the fields are empty, show an error message
        st.error("Please fill in all the fields (Game Environment, Protagonist, Antagonist) before generating the story.")
    else:
        # Main content layout
        col1, col2 = st.columns(2)

        # Column 1: Environment and Story
        with col1:
            st.header("Game Environment")
            st.write(generate_game_environment(game_environment))

            st.header("Game Story")
            st.write(generate_game_story(game_environment, protagonist, antagonist))

        # Column 2: Protagonist and Antagonist
        with col2:
            st.header("Protagonist")
            st.write(generate_protagonist(protagonist))

            st.header("Antagonist")
            st.write(generate_antagonist(antagonist))
