# import os

# import about
# import display
# import download
# import forms
# import query
# import repo
# import streamlit as st
# import utils
# import instructions

# env_file_path = ".env"
# log_file = "app.log"


# temp_dir = "/tmp/chatgpt-code-review"


# def app():
#     utils.load_environment_variables(env_file_path)
#     utils.set_environment_variables()
#     utils.configure_logging(log_file)

#     with utils.TempDirContext(temp_dir):
#         st.set_page_config(
#             page_title="ChatGPT Code Review",
#         )

#         session_state = st.session_state

#         st.title("ChatGPT Code Review :rocket:")

#         with st.expander("About ChatGPT Code Review"):
#             st.markdown(about.about_section, unsafe_allow_html=True)
#             st.write("")

#         default_repo_url = "https://github.com/domvwt/chatgpt-code-review"
#         repo_form = forms.RepoForm(default_repo_url)
#         with st.form("repo_url_form"):
#             repo_form.display_form()

#         # Check if the API key is valid before proceeding
#         if repo_form.clone_repo_button and not repo_form.is_api_key_valid():
#             st.stop()

#         repo_url, extensions = repo_form.get_form_data()

#         analyze_files_form = forms.AnalyzeFilesForm(session_state)
#         with st.form("analyze_files_form"):
#             if repo_form.clone_repo_button or session_state.get("code_files"):
#                 if not session_state.get("code_files"):
#                     session_state.code_files = (
#                         repo.list_code_files_in_repository(
#                             repo_url, extensions
#                         )
#                     )

#                 analyze_files_form.display_form()

#         # Analyze the selected files
#         with st.spinner("Analyzing files..."):
#             if session_state.get("analyze_files"):
#                 if session_state.get("selected_files"):
#                     recommendations = query.analyze_code_files(
#                         session_state.selected_files
#                     )

#                     # Display the recommendations
#                     st.header("Recommendations")
#                     first = True
#                     recommendation_list = []
#                     for rec in recommendations:
#                         if not first:
#                             st.write("---")
#                         else:
#                             first = False
#                         st.subheader(display.escape_markdown(rec["code_file"]))
#                         recommendation = (
#                             rec["recommendation"] or "No recommendations"
#                         )
#                         st.markdown(recommendation)
#                         with st.expander("View Code"):
#                             extension = os.path.splitext(rec["code_file"])[1]
#                             display.display_code(
#                                 rec["code_snippet"], extension
#                             )
#                         recommendation_list.append(rec)
#                     if recommendation_list:
#                         session_state.recommendation_list = recommendation_list
#                 else:
#                     st.error("Please select at least one file to analyze.")
#                     st.stop()

#         st.write("")

#         download.download_markdown(session_state.get("recommendation_list"))


# if __name__ == "__main__":
#     app()

# import os
# import about
# import display
# import download
# import forms
# import instructions  # Ensure this is created as per previous instructions
# import query
# import repo
# import streamlit as st
# import utils

# env_file_path = ".env"
# log_file = "app.log"
# temp_dir = "/tmp/chatgpt-code-review"

# def app():
#     utils.load_environment_variables(env_file_path)
#     utils.set_environment_variables()
#     utils.configure_logging(log_file)

#     # Page configuration and custom CSS
#     st.set_page_config(page_title="ChatGPT Code Review")
#     st.markdown("""
#     <style>
#         body {
#             font-family: 'Arial', sans-serif;
#         }
#         .stButton>button {
#             color: white;
#             background-color: #4CAF50;
#             padding: 10px 24px;
#             margin: 10px 0;
#             border: none;
#             border-radius: 12px;
#             cursor: pointer;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     with utils.TempDirContext(temp_dir):
#         if 'init' not in st.session_state:
#             st.session_state['init'] = True
#             instructions.show_instructions()
#             st.stop()

#         st.title("ChatGPT Code Review")

#         with st.expander("About ChatGPT Code Review"):
#             st.markdown(about.about_section, unsafe_allow_html=True)

#         default_repo_url = "https://github.com/domvwt/chatgpt-code-review"
#         repo_form = forms.RepoForm(default_repo_url)
#         with st.form("repo_url_form"):
#             repo_form.display_form()

#         # Check if the API key is valid before proceeding
#         if repo_form.clone_repo_button and not repo_form.is_api_key_valid():
#             st.stop()

#         repo_url, extensions = repo_form.get_form_data()

#         analyze_files_form = forms.AnalyzeFilesForm(st.session_state)
#         with st.form("analyze_files_form"):
#             if repo_form.clone_repo_button or st.session_state.get("code_files"):
#                 if not st.session_state.get("code_files"):
#                     st.session_state.code_files = repo.list_code_files_in_repository(repo_url, extensions)

#                 analyze_files_form.display_form()

#         # Analyze the selected files
#         with st.spinner("Analyzing files..."):
#             if st.session_state.get("analyze_files"):
#                 if st.session_state.get("selected_files"):
#                     recommendations = query.analyze_code_files(st.session_state.selected_files)

#                     # Display the recommendations
#                     st.header("Recommendations")
#                     first = True
#                     recommendation_list = []
#                     for rec in recommendations:
#                         if not first:
#                             st.write("---")
#                         else:
#                             first = False
#                         st.subheader(display.escape_markdown(rec["code_file"]))
#                         recommendation = rec["recommendation"] or "No recommendations"
#                         st.markdown(recommendation)
#                         with st.expander("View Code"):
#                             extension = os.path.splitext(rec["code_file"])[1]
#                             display.display_code(rec["code_snippet"], extension)
#                         recommendation_list.append(rec)
#                     if recommendation_list:
#                         st.session_state.recommendation_list = recommendation_list
#                 else:
#                     st.error("Please select at least one file to analyze.")
#                     st.stop()

#         st.write("")
#         download.download_markdown(st.session_state.get("recommendation_list"))

# if __name__ == "__main__":
#     if 'start_clicked' in st.session_state and st.session_state['start_clicked']:
#         app()
#     else:
#         instructions.show_instructions()


import os
import display
import download
import forms
import instructions
import query
import repo
import streamlit as st
import utils

env_file_path = ".env"

def app():
    utils.load_environment_variables(env_file_path)
    utils.set_environment_variables()

    # Page configuration and custom CSS
    st.set_page_config(page_title="Code Choreographer")
    st.markdown(
        """
   <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stButton > button {
            color: white;
            background-color: #4CAF50;
            padding: 10px 24px;
            margin: 10px 0;
            border: none;
            border-radius: 12px;
            cursor: pointer;
        }
        /* Custom styles for layout and spacing */
        .block-container {
            padding: 2rem;
            max-width: 100%;
        }
        .stTextInput, .stSelectbox {
            font-size: 0.85rem;
            padding: 8px;
        }
        /* Additional styles for column separation */
        .column {
            border-right: 1px solid #eee;
            padding-right: 20px;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Reorganized layout with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
       ## About Code Choreographer

**Code Choreographer** is a sophisticated application designed to assist software developers in enhancing the quality of their code. Utilizing the advanced capabilities of OpenAI's large language models, this tool analyzes code within a specified GitHub repository and provides targeted recommendations for improvement.

### How to Use Code Choreographer
To leverage this tool and receive valuable code insights, follow the steps outlined below:

1. **Access the App:** Start by opening the Code Choreographer app in your web browser.
2. **Enter the GitHub Repository URL:** Type the URL of the repository you wish to analyze into the "GitHub Repository URL" input field.
3. **Enter Your OpenAI API Key:** Provide your OpenAI API key in the "OpenAI API Key" input field. If you do not possess an API key, you can obtain one from the [OpenAI platform](https://platform.openai.com/account/api-keys).
4. **Select File Extensions:** Choose which file extensions you want to analyze.
5. **Clone the Repository:** Click the "Clone Repository" button. This will reveal the files available for analysis in a structured tree format.
6. **Select Files to Analyze:** Mark the checkboxes next to the files you intend to analyze and then hit the "Analyze Files" button.
7. **Review the Recommendations:** After analysis, the app will display recommendations in a clear and structured format, complete with code snippets and suggestions for enhancement.

### Best Practices
While Code Choreographer provides insightful recommendations, it is not infallible. It is crucial to apply your own expertise and judgment when evaluating the app's suggestions to ensure the best outcomes for your projects.

### Useful Links
- [OpenAI](https://openai.com/) - [API Keys](https://platform.openai.com/account/api-keys)

<!-- Custom CSS for styling -->
<style>
a {
    text-decoration: none;  /* Removes underline from links */
    color: #0175C2;  /* Sets link color */
}
a:hover {
    text-decoration: underline;  /* Adds underline on hover for better user interaction */
}
</style>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.title("Code Choreographer")

        default_repo_url = ""
        repo_form = forms.RepoForm(default_repo_url)
        with st.form("repo_url_form"):
            repo_form.display_form()

        # Check if the API key is valid before proceeding
        if repo_form.clone_repo_button and not repo_form.is_api_key_valid():
            st.stop()

        repo_url, extensions = repo_form.get_form_data()

        analyze_files_form = forms.AnalyzeFilesForm(st.session_state)
        with st.form("analyze_files_form"):
            if repo_form.clone_repo_button or st.session_state.get("code_files"):
                if not st.session_state.get("code_files"):
                    st.session_state.code_files = repo.list_code_files_in_repository(
                        repo_url, extensions
                    )

                analyze_files_form.display_form()

        # Analyze the selected files
        with st.spinner("Analyzing files..."):
            if st.session_state.get("analyze_files"):
                if st.session_state.get("selected_files"):
                    recommendations = query.analyze_code_files(
                        st.session_state.selected_files
                    )

                    # Display the recommendations
                    st.header("Recommendations")
                    first = True
                    recommendation_list = []
                    for rec in recommendations:
                        if not first:
                            st.write("---")
                        else:
                            first = False
                        st.subheader(display.escape_markdown(rec["code_file"]))
                        recommendation = rec["recommendation"] or "No recommendations"
                        st.markdown(recommendation)
                        with st.expander("View Code"):
                            extension = os.path.splitext(rec["code_file"])[1]
                            display.display_code(rec["code_snippet"], extension)
                        recommendation_list.append(rec)
                    if recommendation_list:
                        st.session_state.recommendation_list = recommendation_list
                else:
                    st.error("Please select at least one file to analyze.")
                    st.stop()

        st.write("")
        download.download_markdown(st.session_state.get("recommendation_list"))


if __name__ == "__main__":
    if "start_clicked" in st.session_state and st.session_state["start_clicked"]:
        app()
    else:
        instructions.show_instructions()
