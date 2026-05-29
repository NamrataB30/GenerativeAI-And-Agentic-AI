import streamlit as st
import whisper
import tempfile


def run_audio_to_text():

    st.header("Audio → Text using Whisper")

    uploaded_audio = st.file_uploader(
        "Upload Audio",
        type=["mp3", "wav", "m4a"]
    )

    if uploaded_audio:

        st.audio(uploaded_audio)

        if st.button("Transcribe Audio"):

            try:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp3"
                ) as temp_audio:

                    temp_audio.write(
                        uploaded_audio.read()
                    )

                    temp_path = temp_audio.name

                model = whisper.load_model(
                    "base"
                )

                result = model.transcribe(
                    temp_path
                )

                st.success(
                    "Transcription Complete"
                )

                st.subheader(
                    "Transcript"
                )

                st.write(
                    result["text"]
                )

            except Exception as e:

                st.error(str(e))