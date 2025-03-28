import streamlit as str
import pandas as pd 
import os
import streamlit as st

# Home Page
st.title("Growth Mindset Challenge")
st.subheader("What is Growth Mindset?")

st.write("""A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes.
This mindset encourages you to embrace challenges and stay positive through difficulties.
""")
st.write("Welcome! Let's develop a growth mindset through challenges and learning.")



question =st.subheader("How do you feel about challenges?")
question = st.radio(
    "select",
    ("I tend to avoid challenges because they feel uncomfortable","I see challenges  as opportunities to learn and grow")
)

if question == ("I see challenges  as opportunities to learn and grow"):


    st.success("Great! You're on the right track.")
else:
    st.warning("Don't worry! Challenges help you grow keep going")

# Set Learning Goals
st.subheader("Set Your Learning Goals")
goal = st.text_input("What is your learning goal for this month?")
if goal:
    st.success(f"Your goal is set: {goal}")

# Show Motivational Quotes
st.subheader("Stay Inspired!")
quotes : str= ["life is like  riding a bicycle. To keep your balance,you must keep moving---Albert Einstein"]
        #   "It's not about being the best. It's about being better than you were yesterday."]
st.write(quotes[0])
