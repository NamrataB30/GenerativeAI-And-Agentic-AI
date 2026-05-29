import streamlit as st
import replicate


def run_text_to_video():

    st.header("Text → Video using Replicate")

    api_token = st.text_input(
        "Replicate API Token",
        type="password"
    )

    prompt = st.text_area(
        "Enter Video Prompt",
        placeholder="A drone flying over the Himalayas at sunrise"
    )

    if st.button("Generate Video"):

        if not api_token:
            st.error("Please enter Replicate API Token")
            return

        if not prompt:
            st.error("Please enter a prompt")
            return

        try:

            client = replicate.Client(
                api_token=api_token
            )

            with st.spinner("Generating video... This may take a few minutes."):

                output = client.run(
                    "kwaivgi/kling-v1.6-standard",
                    input={
                        "prompt": prompt
                    }
                )

            video_url = str(output)

            st.success("Video Generated Successfully")

            st.video(video_url)

            st.markdown(
                f"[Open Video]({video_url})"
            )

        except Exception as e:

            st.error(str(e))