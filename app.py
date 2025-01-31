import pytesseract
import streamlit as st
import os
import whisper
import io
import tempfile
import PyPDF2
from PIL import Image
from pathlib import Path
from openai import OpenAI
import helper

def resetSessionState():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.session_state.processed_data = []

resetSessionState()

st.title("Content Summarizer")
st.write("Application providing a solution for generating summaries from various types of content, including images, audio, and video.")

st.divider()

uploaded_files = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "mp3", "mp4", "pdf"], accept_multiple_files=True)

if uploaded_files is not None and len(uploaded_files) > 0:
    resetSessionState()
    st.write("Results:")
    with st.spinner("Loading..."):
        for uploaded_file in uploaded_files:
            file_extension = Path(uploaded_file.name).suffix
            
            if file_extension in [".mp3", ".mp4"]:
                result = helper.transcribeSTT(uploaded_file)

            elif file_extension in [".pdf"]:
              result = helper.pdfToText(uploaded_file)

            else:
                result = helper.ocr(uploaded_file)

            with st.expander(f"{uploaded_file.name}"):
                st.write(result)

            st.session_state.processed_data.append(result)



if st.button("Generate summary", disabled=not st.session_state.processed_data):
    st.divider()
    with st.spinner("Generating..."):
        api_key = os.getenv('OR_API_KEY')
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=f"{api_key}",
        )
        stream = client.chat.completions.create(
            model="meta-llama/llama-3.1-70b-instruct:free",
            messages=[
                {
                    "role": "developer", 
                    "content": """
                        Make university grade summary of provided content.
                        Detect which language is the main one used in the provided content, and make your summary using only that language.
                    """
                },
                {
                    "role": "user", 
                    "content": f"{' '.join(st.session_state.processed_data)}"
                }
            ],
            stream=True,
        )
        output = st.empty()
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                output.markdown(full_response, unsafe_allow_html=True)

        st.divider()
        if st.button("Clear all", icon=":material/delete_sweep:", type="primary"):
            output.empty()


