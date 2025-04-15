import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel('gemini-1.5-pro-001')

# Streamlit UI
st.title("🤖 Gemini Chatbot")

# Sidebar login UI
st.sidebar.title("Login With Us")
st.sidebar.button("Email", type="secondary")
st.sidebar.button("Google", type="primary")
st.sidebar.button("Facebook", type="primary")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial system message if desired
    # st.session_state.messages.append({"role": "model", "content": "How can I help you today?"})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if prompt := st.chat_input("Ask Gemini..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with a spinner while generating
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Create chat history in the format Gemini expects
            chat = model.start_chat(history=[
                {"role": m["role"], "parts": [m["content"]]} 
                for m in st.session_state.messages if m["role"] in ["user", "model"]
            ])
            
            # Generate response from Gemini
            response = chat.send_message(prompt)
            response_text = response.text
            
            # Display the response
            st.markdown(response_text)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "model", "content": response_text})