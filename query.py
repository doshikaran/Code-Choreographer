import logging
from textwrap import dedent
from typing import Iterable

import openai
import streamlit as st
import tiktoken


def analyze_code_files(code_files: list[str]) -> Iterable[dict[str, str]]:
    """Analyze the selected code files and return recommendations."""
    return (analyze_code_file(code_file) for code_file in code_files)


def analyze_code_file(code_file: str) -> dict[str, str]:
    """Analyze a code file and return a dictionary with file information and recommendations."""
    with open(code_file, "r") as f:
        code_content = f.read()

    if not code_content:
        return {
            "code_file": code_file,
            "code_snippet": code_content,
            "recommendation": "No code found in file",
        }

    try:
        logging.info("Analyzing code file: %s", code_file)
        analysis = get_code_analysis(code_content)
    except Exception as e:
        logging.info("Error analyzing code file: %s", code_file)
        analysis = f"Error analyzing code file: {e}"

    return {
        "code_file": code_file,
        "code_snippet": code_content,
        "recommendation": analysis,
    }


def get_num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
    # Source: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        logging.debug("Model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":
        logging.debug(
            "gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301."
        )
        return get_num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        logging.debug(
            "gpt-4 may change over time. Returning num tokens assuming gpt-4-0314."
        )
        return get_num_tokens_from_messages(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = (
            4 
        )
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 4 
    return num_tokens


@st.cache_data(show_spinner=False)
def get_code_analysis(code: str) -> str:
    """Get code analysis from the OpenAI API."""
    prompt = dedent(
        f"""\
Please review the code below for potential issues and opportunities for improvement.
    Provide a detailed analysis addressing the following areas and suggest specific improvements.
    Keep the section headings as provided, and use bullet points for your responses.
    Ensure the examples given are relevant to the provided code and avoid repeating the illustrative examples.

    **Syntax and Logical Errors:**
- Review for common syntax mistakes and logic errors that could lead to unexpected behavior or runtime errors.
- Example: Incorrect indentation leading to errors in logical structure.
- Example: Missing closing parenthesis affecting the code execution.

**Code Refactoring and Quality Improvement:**
- Suggest changes that can simplify the structure and improve the readability and maintainability of the code.
- Example: Replace nested if-else statements with a switch-case or strategy design pattern for clarity.
- Example: Refactor large functions into smaller, more manageable pieces.

**Performance Optimization:**
- Identify areas where performance could be improved and propose solutions to optimize execution.
- Example: Suggest more efficient data structures or algorithms where applicable.
- Example: Recommend caching strategies or optimizations in loop structures.

**Security Vulnerabilities:**
- Point out potential security flaws that could be exploited and recommend preventive measures.
- Example: Highlight insecure data handling that could lead to data breaches and suggest secure practices.
- Example: Recommend best practices for securing database queries to prevent SQL injection.

**Code Complexity Analysis:**
- Discuss the complexity of the code and suggest ways to reduce cognitive load when understanding the code.
- Example: Identify complex conditional logic that could be simplified.
- Example: Suggest decomposition of complex functions into simpler, single-purpose functions.

**Detection of Code Smells:**
- **Duplicate Code:** Identify and recommend ways to abstract duplicated logic or data into reusable components.
- **Improper Names:** Point out variables, functions, or classes with names that do not clearly describe their purpose.
- **Long Functions, Methods, Classes:** Highlight overly long code blocks that could be broken into smaller, more focused functions.
- **Long Parameter Lists:** Suggest reducing the number of parameters for methods through object encapsulation or parameter objects.
- **Inconsistent Naming:** Identify and correct inconsistencies in naming conventions across the codebase.
- **Data Clumps:** Recommend restructuring related data fields and variables that often appear together into more coherent data structures.

**Adherence to Best Practices:**
- Evaluate the code's conformity to industry best practices and provide advice for alignment.
- Example: Ensure that coding standards for readability like naming conventions and documentation are followed.
- Example: Advise on the use of version control best practices and continuous integration workflows.

Code:
```
{code}
```
Your review:"""
    )
    messages = [{"role": "system", "content": prompt}]
    tokens_in_messages = get_num_tokens_from_messages(
        messages=messages, model="gpt-3.5-turbo"
    )
    max_tokens = 4096
    tokens_for_response = max_tokens - tokens_in_messages

    if tokens_for_response < 200:
        return "The code file is too long to analyze. Please select a shorter file."

    logging.info("Sending request to OpenAI API for code analysis")
    logging.info("Max response tokens: %d", tokens_for_response)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=tokens_for_response,
        n=1,
        temperature=0,
    )
    logging.info("Received response from OpenAI API")

    assistant_response = response.choices[0].message["content"]
    return assistant_response.strip()
