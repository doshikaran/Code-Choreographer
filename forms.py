import logging
import os
import repo
import openai
import streamlit as st
from streamlit_tree_select import tree_select
from utils import EXTENSION_TO_LANGUAGE_MAP


class RepoForm:
    """A class to encapsulate the repository form and its operations."""

    options = list(EXTENSION_TO_LANGUAGE_MAP.keys())

    def __init__(self, default_repo_url: str):
        self.default_repo_url = default_repo_url
        self.repo_url = ""
        self.api_key = ""
        self.extensions = []
        self.additional_extensions = ""

    def display_form(self):
        st.markdown(
            """
        <style>
        div.stButton > button {
            background-color: #000000;  
            color: white;               
            border-radius: 4px;         
            border: 1px solid #000000;  
        }
        div.stButton > button:hover {
            background-color: #555555;  
            color: white;
            border: 1px solid #333333;  
        }
        .stMultiSelect .css-12jo7m5 {
                background-color: #79b479; /* Change to a green color */
                color: white; /* Text color inside the tag */
            }
            .stMultiSelect .css-12jo7m5:hover {
                background-color: #66cc66; /* Slightly lighter green on hover */
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
        """Displays the repository form and its elements."""

        self.repo_url = st.text_input(
            "GitHub Repository URL:", placeholder="Enter the GitHub repository URL"
        )
        self.api_key = st.text_input(
            "OpenAI API Key:", "", placeholder="Paste your API key here"
        )
        self.extensions = st.multiselect(
            "File extensions to analyze",
            options=self.options,
            default=self.options,
        )
        self.clone_repo_button = st.form_submit_button("Clone Repository")

    def get_form_data(self):
        return (self.repo_url, self.extensions)

    def is_api_key_valid(self):
        if not self.api_key:
            st.error("Please enter your OpenAI API key.")
            return False
        openai.api_key = self.api_key
        return True


class AnalyzeFilesForm:
    def __init__(self, session_state):
        self.session_state = session_state

    def display_form(self):
        st.write("Select files to analyze:")
        file_tree = repo.create_file_tree(self.session_state.code_files)
        self.session_state.selected_files = tree_select(
            file_tree,
            show_expand_all=True,
            check_model="leaf",
            checked=self.session_state.get("selected_files"),
        )["checked"]
        logging.info("Selected files: %s", self.session_state.selected_files)
        self.session_state.analyze_files = st.form_submit_button(
            "Analyze Files"
        ) or self.session_state.get("analyze_files")
