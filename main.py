import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}!")


def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api.vercel.app/money_quotes")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["money_quote"]
        else:
            return ("Freelancing")
        
    except:
        return ("Something went wrong!")


# Create a section for side hustle ideas
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):  # When user clicks button
    idea = fetch_side_hustle()  # Get a hustle idea
    st.success(idea)  # Show the idea


# Function to get money-related quotes from server
def fetch_money_quote():
    try:
        # Try to get quote from local server or deployed server
        response = requests.get(
            "https://fastapi-api.vercel.app/side_hustles"
        )
        if response.status_code == 200:  # If request successful
            quotes = response.json()  # Convert response to JSON
            return quotes["side_hustle"]  # Return the quote
        else:
            return "Money is the root of all evil!"  # Default quote if server fails
    except:
        return "Something went wrong!"  # Error message if request fails
    
    
# Create a section for motivation quotes
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):  # When user clicks button
    quote = fetch_side_hustle()  # Get a quote
    st.info(quote)  # Show the quote
    
