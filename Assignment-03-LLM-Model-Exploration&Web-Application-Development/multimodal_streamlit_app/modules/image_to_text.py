import streamlit as st
from google import genai
from PIL import Image


def run_image_to_text():

    st.header("Image → Text using Gemini")

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        key="image_api_key"
    )

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("Analyze Image"):

            try:

                client = genai.Client(
                    api_key=api_key
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        "Describe this image in detail",
                        image
                    ]
                )

                st.subheader("Analysis")

                st.write(response.text)

            except Exception as e:
                st.error(str(e))