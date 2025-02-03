FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    tesseract-ocr \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8501

RUN export PYTHONPATH="${PYTHONPATH}:."

CMD ["streamlit", "run", "app.py", "--server.enableCORS=false", "--server.port=8501"]