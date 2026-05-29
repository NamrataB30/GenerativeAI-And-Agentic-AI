import streamlit as st
from google import genai
import tempfile
import time


def run_video_to_text():

    st.header("Video → Text using Gemini")

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        key="video_api_key"
    )

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4", "mov", "avi", "mkv"]
    )

    if uploaded_video:

        st.video(uploaded_video)

        if st.button("Analyze Video"):

            if not api_key:
                st.error("Please enter Gemini API Key")
                return

            try:

                client = genai.Client(
                    api_key=api_key
                )

                # Save uploaded video temporarily
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp4"
                ) as temp_video:

                    temp_video.write(
                        uploaded_video.read()
                    )

                    temp_path = temp_video.name

                with st.spinner("Uploading video to Gemini..."):

                    video_file = client.files.upload(
                        file=temp_path
                    )

                with st.spinner("Processing video... Please wait..."):

                    while True:

                        file_info = client.files.get(
                            name=video_file.name
                        )

                        state = str(file_info.state)

                        # Debug info
                        st.write(f"Current State: {state}")

                        if "ACTIVE" in state:
                            break

                        if "FAILED" in state:
                            st.error(
                                "Video processing failed."
                            )
                            return

                        time.sleep(2)

                with st.spinner("Generating summary..."):

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[
                            video_file,
                            """
                            Describe this video in detail.
                            Include:
                            1. Main scene
                            2. Objects present
                            3. Actions occurring
                            4. Overall summary
                            """
                        ]
                    )

                st.success(
                    "Video Analysis Complete"
                )

                st.subheader(
                    "Video Summary"
                )

                st.write(
                    response.text
                )

            except Exception as e:

                st.error(str(e))