# Content Summarizer - AI-Powered Multi-Format Content Summarization Tool

## 🚀Live Demo
[![APP STATUS](https://img.shields.io/badge/app%20status-up-brightgreen?style=for-the-badge)](https://summarizer-app.almapas.com/)

**Try the application online:** [summarizer-app](https://summarizer-app.almapas.com/)

## 📖 Overview
Content Summarizer is an AI-powered application that extracts and summarizes text from various types of content, including PDFs, images, audio, and video files. Leveraging OCR and AI models, it provides quick and efficient summaries, making information more accessible and digestible.

## ✨ Features
- 🖼 **Image OCR** - Optical Character Recognition, which allows for text extraction from images.
- 🔊 **Audio/Video Transcription** - Converts spoken words into text.
- 📄 **PDF** - Extracts text from PDF documents.
- 🧠 **AI-Powered Summarization** - Uses advanced LLM models to create high-quality summaries.
- 🌍 **Cross-Platform** - Accessible on any modern web browser without installation.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Frontend:** Streamlit
- **OCR & Image Processing:** Pillow, Pytesseract
- **PDF File Handling:** PyPDF2
- **ASR Model:** OpenAI Whisper
- **LLM API:** OpenAI API

## 📜 Installation & Development Setup
If you wish to run the project locally, follow these steps:

### Prerequisites
- [Docker](https://www.docker.com/)
- File `.env` - added to project directory:
  ```bash
  OR_API_KEY="API key for authentication with the LLM provider"
  BASE_URL="Base URL for the LLM provider's API"
  MODEL="Selected LLM model"  # (Current version in use - Meta: Llama 3.1 70B Instruct)
  ```

### Running Locally with Docker Compose
1. Clone the repository:
   ```
   git clone https://github.com/Alex555eu/content-summarizer.git
   cd content-summarizer
   ```

2. Create an `.env` file from the template file filled with necessary data:
   ```
   cp .env-template .env
   ```

3. Build and start the application:
   ```
   docker compose up 
   ```

4. Access the application by navigating to: [http://localhost:8501](http://localhost:8501).


---
**Happy Summarizing! 📝✨**

