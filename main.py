import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Leo!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Leo - ChatBot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
# Input field for user's message
user_prompt = st.chat_input("Ask with -Leo...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)


# """Step 1: After the extract the zip file from the Github...we need to ensure that in the code 
# editor like the VS Code the python library like the streamlit, dotenv, google.generativeai is installed in 
# the system or not...install it if not.

# Step 2). After the install the Certain Libraries ensure that (.venv) folder are there where extract..
# if not there in code editor the notification comes in when the time of execution that your virtual environment 
# is not created...we need to create it in the code editor. 

# Step 3). Then for the execution go the new terminal only and write the synatx of running..{streamlit run main.py}
# """
