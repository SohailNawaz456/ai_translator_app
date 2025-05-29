import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Define agents and their roles
agents = {
    "Booking Agent": (
        "You help the user book hotels, flights, and transport. "
        "Ask necessary details and suggest top-rated options with pricing."
    ),
    "Itinerary Planner": (
        "Create a detailed day-by-day travel itinerary including activities, travel time, rest breaks, and meals."
    ),
    "Travel Guide": (
        "Describe local tourist attractions, culture, history, food, and tips in a friendly and engaging way."
    ),
    "Budget Advisor": (
        "Analyze the user's travel budget and recommend affordable options without sacrificing quality."
    ),
    "Weather Assistant": (
        "Provide detailed weather forecasts for the destination and travel dates. Suggest appropriate clothing and precautions."
    ),
    "Packing Assistant": (
        "Recommend a personalized packing list based on destination, weather, length of stay, and activities planned."
    ),
    "Visa & Docs Agent": (
        "Inform about visa requirements, passport validity, and travel documents needed based on nationality and destination."
    ),
}

st.set_page_config(page_title="SmartTrip AI - Multi-Agent Travel Assistant", layout="centered")
st.title("✈️ SmartTrip AI - Multi-Agent Travel Assistant")
st.write("Created by **Sohail Nawaz** – Plan and book your trips effortlessly with specialized AI agents.")

# Sidebar with agent selection
agent = st.sidebar.selectbox("Choose an AI Agent:", list(agents.keys()))

st.markdown(f"### 🧠 You are chatting with: **{agent}**")
user_input = st.text_area("Ask your travel question or request here:", height=140)
btn_ask = st.button("Ask Agent")

if btn_ask and user_input.strip():
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        system_instruction = agents[agent]
        prompt = f"{system_instruction}\n\nUser: {user_input}\nAI:"
        response = model.generate_content(prompt)
        st.success(f"🤖 Response from {agent}:")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
else:
    st.info("Please enter your question or request and press 'Ask Agent'.")

# Optional: Footer with contact or credits
st.markdown("---")
st.write("© 2025 Sohail Nawaz | Powered by Gemini AI")
