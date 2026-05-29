import streamlit as st
from gtts import gTTS
import tempfile


def run_text_to_audio():

    st.header("Text → Audio using gTTS")

    text = st.text_area(
        "Enter Text",
        height=150
    )

    if st.button("Generate Audio"):

        if not text:
            st.error("Please enter text")
            return

        try:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp3"
            ) as temp_audio:

                output_path = temp_audio.name

            tts = gTTS(
                text=text,
                lang="en"
            )

            tts.save(output_path)

            st.success(
                "Audio Generated Successfully"
            )

            st.audio(output_path)

        except Exception as e:

            st.error(str(e))