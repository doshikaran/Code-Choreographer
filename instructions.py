# # instructions.py
# import streamlit as st

# def show_instructions():
#     st.title("Welcome to ChatGPT Code Review")
#     st.markdown("""
#     ## How to Use This Tool
#     Follow these steps to analyze your code:
#     1. Enter the GitHub repository URL.
#     2. Input your OpenAI API Key.
#     3. Select the file extensions relevant to your project.
#     4. Clone the repository and select files to analyze.
#     5. Review the analysis and recommendations provided.
#     """)
#     if st.button("Let's Get Started"):
#         st.session_state['start_clicked'] = True


# import streamlit as st
# from graphviz import Digraph

# def create_flowchart():
#     dot = Digraph()
#     dot.node('A', 'Enter the GitHub repository URL:  Enter the URL for the repository where your project is hosted.')
#     dot.node('B', 'Input your OpenAI API Key: Supply your valid OpenAI API key to authenticate and enable the comprehensive analysis capabilities.')
#     dot.node('C', 'Select Relevant File Extensions: Choose the file extensions that correspond to the code files you wish to analyze within your project.')
#     dot.node('D', 'Clone and Select Files: The tool will automatically clone the repository. You will then need to select specific files for analysis.')
#     dot.node('E', 'Review the Analysis Results: After the analysis is complete, examine the provided recommendations and insights to enhance the quality and performance of your code.')
    
#     dot.edges(['AB', 'BC', 'CD', 'DE'])
#     # dot.edge('C', 'E', constraint='false')  # Optional direct edge if needed

#     return dot

# def show_instructions():
#     st.title("Welcome to Code Choreographer")
#     st.markdown("""
#     ## How to Use This Tool
#     Embark on your journey to polished and efficient code by following these simple steps:
#     """)
    
#     st.graphviz_chart(create_flowchart())

#     if st.button("Let's Get Started"):
#         st.session_state['start_clicked'] = True

# if __name__ == "__main__":
#     show_instructions()
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
        # Optionally navigate to another part of the app or refresh
        st.rerun()  # Rerun the app to reflect changes

if __name__ == "__main__":
    if 'start_clicked' in st.session_state and st.session_state['start_clicked']:
        # This is where you would redirect or show the next part of your application
        st.write("Navigating to the next page...")
        # You should implement the actual navigation or next steps here
    else:
        show_instructions()

