import os
import tempfile
import openai
from fastapi import UploadFile

openai.api_key = os.getenv("OPENAI_API_KEY")

async def process_image(file: UploadFile):
    """
    Processes an uploaded image file and returns a detailed description using GPT-4o Vision.
    """
    # Save the uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    # Call OpenAI's GPT-4o vision model
    # Note: We send the image as base64 to the API
    with open(tmp_path, "rb") as img_file:
        img_data = img_file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Vision-capable model
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in detail."},
                    {"type": "image", "image_data": img_data}
                ]
            }
        ]
    )

    description = response.choices[0].message["content"]

    return description

