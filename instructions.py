import streamlit as st

def show_instructions():
    st.title("Welcome to Code Choreographer")
    
    # CSS to style the button
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #000000; /* Black */
        color: #ffffff; /* White text */
        border-radius: 0.3em; /* Rounded corners */
        border: 1px solid #ffffff; /* White border */
    }
    div.stButton > button:hover {
        background-color: #555555; /* Lighter black for hover */
        color: #ffffff; /* White text */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    **1. Enter the GitHub Repository URL**  
    _Provide the URL for the repository where your project is hosted._
    
    **2. Input Your OpenAI API Key**  
    _Supply your valid OpenAI API key to authenticate and enable the analysis._
    
    **3. Select Relevant File Extensions**  
    _Choose the file extensions that correspond to the code files you wish to analyze._
    
    **4. Clone and Select Files**  
    _The tool will automatically clone the repository. You will then need to select specific files for analysis._
    
    **5. Review the Analysis Results**  
    _After the analysis is complete, examine the provided recommendations and insights._
    """)

    if st.button("Let's Get Started"):
        handle_button_click()

def handle_button_click():
    # Change the state only if it's not already set
    if 'start_clicked' not in st.session_state or not st.session_state['start_clicked']:
        st.session_state['start_clicked'] = True
        st.rerun()

if __name__ == "__main__":
    if 'start_clicked' in st.session_state and st.session_state['start_clicked']:
        st.write("Navigating to the next page...")
    else:
        show_instructions()

