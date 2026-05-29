from urllib import response

import streamlit as st
from google import genai


def run_text_to_text():

    st.header("Text → Text using Gemini")

    api_key = st.text_input(
        "Gemini API Key",
        type="password"
    )

    prompt = st.text_area(
        "Enter Prompt",
        height=150
    )

    if st.button("Generate"):

        if not api_key:
            st.error("Please enter Gemini API Key")
            return

        if not prompt:
            st.error("Please enter a prompt")
            return

        try:

            client = genai.Client(
                api_key=api_key
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.subheader("Response")

            st.success("Response Generated Successfully")

            st.markdown(response.text)

        except Exception as e:
            st.error(str(e))