import streamlit as st
from modules.text_to_text import run_text_to_text
from modules.text_to_image import run_text_to_image
from modules.image_to_text import run_image_to_text
from modules.text_to_audio import run_text_to_audio
from modules.audio_to_text import run_audio_to_text
from modules.text_to_video import run_text_to_video
from modules.video_to_text import run_video_to_text

st.set_page_config(
    page_title="Multimodal AI Application",
    layout="wide"
)

st.title("Multimodal AI Application")

task = st.sidebar.selectbox(
    "Choose Modality",
    [
        "Text → Text",
        "Text → Image",
        "Image → Text",
        "Text → Audio",
        "Audio → Text",
        "Text → Video",
        "Video → Text"
    ]
)

if task == "Text → Text":
    run_text_to_text()
elif task == "Text → Image":
    run_text_to_image()
elif task == "Image → Text":
    run_image_to_text()
elif task == "Text → Audio":
    run_text_to_audio()
elif task == "Audio → Text":
    run_audio_to_text()
elif task == "Text → Video":
    run_text_to_video()
elif task == "Video → Text":
    run_video_to_text()