# Multimodal AI Application

## Project Overview

This project is a Multimodal AI Application developed as part of the LLM Model Exploration & Web Application Development Assignment.

The application demonstrates how modern AI models process and generate information across multiple modalities such as text, image, audio, and video.

---

## Supported Modalities

### 1. Text → Text
- Model: Google Gemini 2.5 Flash
- Functionality:
  - Accepts text input
  - Generates intelligent text responses

### 2. Text → Image
- Model: Hugging Face / Stable Diffusion
- Functionality:
  - Generates images from text prompts

### 3. Image → Text
- Model: Google Gemini 2.5 Flash
- Functionality:
  - Accepts image uploads
  - Generates image descriptions and analysis

### 4. Text → Audio
- Model: gTTS (Google Text-to-Speech)
- Functionality:
  - Converts text into spoken audio

### 5. Audio → Text
- Model: OpenAI Whisper
- Functionality:
  - Accepts audio uploads
  - Converts speech into text

### 6. Text → Video
- Model: Replicate (MiniMax Video Model)
- Functionality:
  - Generates videos from text prompts
  - Requires Replicate API credits

### 7. Video → Text
- Model: Google Gemini 2.5 Flash
- Functionality:
  - Accepts video uploads
  - Generates video summaries and descriptions


---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- OpenAI Whisper
- Hugging Face
- Replicate
- gTTS
- PIL (Pillow)

---

## Project Structure

```
multimodal_streamlit_app/
│
├── app.py
│
├── modules/
│   ├── text_to_text.py
│   ├── image_to_text.py
│   ├── audio_to_text.py
│   ├── text_to_audio.py
│   ├── video_to_text.py
│   ├── text_to_image.py
│   └── text_to_video.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd multimodal_streamlit_app
```

### Install Dependencies

uv add -r requirements.txt
```

---

## Running the Application

uv run streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## API Keys Required

### Google Gemini API

Get your API Key from:

https://aistudio.google.com/app/apikey

Used for:

- Text → Text
- Image → Text
- Video → Text

---

### Hugging Face Token

Get your token from:

https://huggingface.co/settings/tokens

Used for:

- Text → Image

---

### Replicate API Token

Get your token from:

https://replicate.com/account/api-tokens

Used for:

- Text → Video

Note:
Video generation may require paid credits.

---

## Assignment Objectives Covered

✔ Text → Text
✔ Text → Image
✔ Image → Text
✔ Text → Audio
✔ Audio → Text
✔ Text → Video
✔ Video → Text


---

## Learning Outcomes

Through this project, the following concepts were explored:

- Large Language Models (LLMs)
- Multimodal AI Systems
- Generative AI APIs
- Speech Recognition
- Text-to-Speech Systems
- Image Generation Models
- Video Understanding Models
- Streamlit Web Application Development
- API Integration

---

## Author

Namrata Bhattacharjee
M.Sc. Statistics
Data Scientist