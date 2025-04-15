import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)  # Replace with your key


# Initialize model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-001")


# Streamlit UIsss
st.title("🤖 Gemini Chatbot")


# Show a title or message in the sidebar
st.sidebar.title("Login With Us")
st.sidebar.button("Email", type="secondary")
st.sidebar.button("Goolge", type="primary")
st.sidebar.button("Facbook", type="primary")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["context"])


# User input
if prompt := st.chat_input("Ask Gemini..."):
    # Add user message
    st.session_state.messages.append ({"role":"user", "context": prompt })
    with st.chat_message("user"):
        st.markdown(prompt)

    #Get Gemini repsonse
    with st.chat_message("assistance"):
        response = model.generate_content(prompt)
        st.markdown(response.text)

    #Add to History
    st.session_state.messages.append({"role":"user", "context": response.text})

