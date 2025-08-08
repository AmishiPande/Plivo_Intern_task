import os
import tempfile
import openai
from pydub import AudioSegment
from pyannote.audio import Pipeline

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize diarization pipeline (needs HuggingFace token in env)
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=os.getenv("HUGGINGFACE_TOKEN")
)

async def process_audio(file):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio = AudioSegment.from_file(file.file)
        audio.export(tmp.name, format="wav")
        audio_path = tmp.name

    # 1 — Transcription with OpenAI Whisper
    with open(audio_path, "rb") as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)

    transcript_text = transcription["text"]

    # 2 — Diarization (up to 2 speakers)
    diarization_result = pipeline(audio_path)
    diarization_output = []
    for segment, _, speaker in diarization_result.itertracks(yield_label=True):
        diarization_output.append({
            "speaker": speaker,
            "start": segment.start,
            "end": segment.end
        })

    return transcript_text, diarization_output

