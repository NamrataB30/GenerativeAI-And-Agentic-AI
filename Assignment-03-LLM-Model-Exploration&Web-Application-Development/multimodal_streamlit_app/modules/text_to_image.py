import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image


def run_text_to_image():

    st.header("Text → Image using Hugging Face")

    hf_token = st.text_input(
        "Hugging Face Token",
        type="password"
    )

    prompt = st.text_area(
        "Enter Image Prompt",
        placeholder="A futuristic city with flying cars at sunset"
    )

    if st.button("Generate Image"):

        if not hf_token:
            st.error("Please enter Hugging Face Token")
            return

        if not prompt:
            st.error("Please enter a prompt")
            return

        try:

            client = InferenceClient(
                provider="hf-inference",
                api_key=hf_token
            )

            image = client.text_to_image(
                prompt,
                model="black-forest-labs/FLUX.1-schnell"
            )

            st.success("Image Generated Successfully")

            st.image(
                image,
                caption=prompt,
                use_container_width=True
            )

        except Exception as e:

            st.error(str(e))