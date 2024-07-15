# Leo - ChatBot
Leo is an interactive ChatBot powered by Google's Generative AI, built using Python and Streamlit.


# Features
- Natural Language Processing: Engage in natural conversations with Leo.
- Google Generative AI: Powered by Google's advanced AI models.
- Interactive Interface: User-friendly chat interface built with Streamlit.
- Customizable: Easily extend and modify with additional features.

# Note:

- Step 1: 
Checking and Installing Python Libraries
Before running your project in VS Code, you need to ensure that necessary Python libraries (streamlit, dotenv, google.generativeai) are installed on your system. 

- Here’s how you can check and install them if they are missing:

Open VS Code: Launch Visual Studio Code.

Open Terminal in VS Code: Press Ctrl + to open a new terminal within VS Code.

Check Installed Packages: Use pip to check if required packages are installed:

bash
Copy code
{pip show streamlit dotenv google-generativeai}
Install Missing Packages: If any of the packages are not installed, install them using pip:

bash
Copy code
{pip install streamlit dotenv google-generativeai}

- Step 2: Setting Up a Virtual Environment
Using a virtual environment (venv) is a good practice to isolate dependencies for different projects. Here’s how you can set up and activate a virtual environment:

Navigate to Project Directory: Change directory to your project folder where you extracted the files:

bash
Copy code
cd path/to/your/project
Create Virtual Environment: Create a virtual environment named .venv:

bash
Copy code
python -m venv .venv
Activate Virtual Environment:

Linux/MacOS:
bash
Copy code
source .venv/bin/activate
Windows:
bash
Copy code
.venv\Scripts\activate
You should see (.venv) appear in your terminal prompt, indicating the virtual environment is active.

- Step 3: 
Running Your Streamlit App
Once you have ensured all libraries are installed and activated your virtual environment, you can run your Streamlit app:

Open Terminal: If not already open, open a terminal in VS Code (Ctrl + ).

Run Streamlit App: Execute the following command to run your Streamlit app (main.py is assumed to be your main script):

bash
Copy code
streamlit run main.py
Access Your App: Once the app starts running, you will see output in the terminal with a local URL (usually http://localhost:8501). Open this URL in your web browser to access your Streamlit application.

# Installation
- Clone the repository:

bash
Copy code
git clone https://github.com/SachinMaurya2002/Leo-Chatbot.git
cd leo-chatbot

- Set up environment:

Create and activate a virtual environment (optional but recommended):
bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
- Install dependencies:
bash
Copy code
pip install -r requirements.txt
- Configuration:

Create a .env file in the root directory and add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key_here
- Usage
Run the Streamlit app:

bash
Copy code
streamlit run main.py

- Access Leo - ChatBot:

Open your web browser and go to http://localhost:8501.
Start chatting with Leo!
 

# Contributing
Contributions are welcome! If you want to contribute to Leo - ChatBot, feel free to fork this repository, create a new branch, and submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Streamlit: For providing a powerful framework for building interactive web applications with Python.
Google Generative AI: For enabling advanced conversational capabilities in Leo.

# Get Started
Explore Leo - ChatBot and start chatting today! If you encounter any issues or have suggestions, please feel free to open an issue or contact us.

