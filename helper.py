import streamlit as st
import whisper
import tempfile
import PyPDF2
import pytesseract
from PIL import Image


def transcribeSTT(uploaded_file):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name
    transcription = model.transcribe(tmp_file_path)
    return transcription['text']


def pdfToText(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


def ocr(uploaded_file):
    image = Image.open(uploaded_file)
    return pytesseract.image_to_string(image)