import os
import tempfile
import openai
import pdfplumber
import docx
from newspaper import Article
from fastapi import UploadFile

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(path: str) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(path: str) -> str:
    text = ""
    doc = docx.Document(path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text_from_url(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text

async def process_document(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    if file.filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(tmp_path)
    elif file.filename.lower().endswith((".doc", ".docx")):
        text = extract_text_from_docx(tmp_path)
    else:
        raise ValueError("Unsupported file format")

    return summarize_text(text)

async def process_url(url: str):
    text = extract_text_from_url(url)
    return summarize_text(text)

def summarize_text(text: str):
    if len(text.strip()) == 0:
        return "No text found to summarize."

    prompt = f"Summarize the following text in a concise paragraph:\n\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]

