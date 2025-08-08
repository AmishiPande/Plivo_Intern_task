from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from .audio_processing import process_audio

from .image_processing import process_image
from fastapi import UploadFile, File

from fastapi import Form
from .docs_processing import process_document, process_url

app = FastAPI()

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is working"}

@app.post("/audio")
async def audio_endpoint(file: UploadFile = File(...)):
    transcript, diarization = await process_audio(file)
    return {
        "transcript": transcript,
        "diarization": diarization
    }

@app.post("/image")
async def image_endpoint(file: UploadFile = File(...)):
    description = await process_image(file)
    return {"description": description}

@app.post("/summarize/document")
async def summarize_document(file: UploadFile = File(...)):
    try:
        summary = await process_document(file)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

@app.post("/summarize/url")
async def summarize_url(url: str = Form(...)):
    try:
        summary = await process_url(url)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

