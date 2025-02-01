import streamlit as st
import whisper
import tempfile
import PyPDF2
import pytesseract
from PIL import Image
from pathlib import Path


def _speechToText(uploaded_file):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file: #verify delete flag !!
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name
    transcription = model.transcribe(tmp_file_path)
    return transcription['text']


def _pdfToText(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


def _ocr(uploaded_file):
    image = Image.open(uploaded_file)
    return pytesseract.image_to_string(image)


def _switch(suffix):
    ext_fun_map = {
        (".mp3", ".mp4", ".mpeg4") : _speechToText,
        (".png", ".jpg", ".jpeg") : _ocr,
        (".pdf",) : _pdfToText
    }
    for ext, func in ext_fun_map.items():
        if suffix in ext:
            return func
    return None


def extractText(uploaded_file):
    suffix = Path(uploaded_file.name).suffix
    function = _switch(suffix)
    if function:
        return function(uploaded_file)
    raise AttributeError(f"File extension {suffix} not supported.")
