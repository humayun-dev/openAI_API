# The sentiment analyzer will response towards any sentiment as positive,negative or neutral
# The streamlit is integrated in the project 
# The commands are:
# pyhton -m venv .venv
# .venv\Scripts\activate
# pip install streamlit
# Author: Muhammad Humayun Khan


# import the essentials
import openai
from openai import OpenAI
import streamlit as st

# path to the key which is saved in a text file
config_path = "key.txt"

with open(config_path, 'r') as file:
    api_key = file.read().strip()

# Initialize the OpenAI client with the API key
client = openai.Client(api_key=api_key)

def analyze_sentiment(text):
    # Make the API call to GPT-3.5-turbo for sentiment analysis
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
            {
                "role": "system",
                "content": "You are a sentiment analysis assistant. Given a text, categorize its sentiment as Positive, Negative, or Neutral."
            },
            {
                "role": "user",
                "content": text
            },
        ],
      max_tokens=10,  # Limiting the tokens since we only need a short response such as +,- or neutral
      temperature=0  # Use 0 for more deterministic output - maximum is 1
  )
    # Extract the sentiment from the response
    sentiment = sentiment = response.choices[0].message.content
    return sentiment

# the streamlit work started here
st.title("Text Sentiment Analyzer")
model = 'gpt-3.5-turbo'
text = st.text_input("Provide input: ", value = "Turning data into insights")

if st.button('Submit'):
  with st.spinner("Sentiment Analysis in Progress"):
    sentiment = analyze_sentiment(text)
    st.success("Sentiment Analysis completed")

  st.write(f"Sentiment: {sentiment}")

