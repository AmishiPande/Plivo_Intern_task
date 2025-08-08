## Overview
This repository contains a full-stack application for processing media files, including:
- **Audio processing**
- **Image processing**
- **Document processing**

The backend is built with **Python (FastAPI)**, and the frontend is built with **React**.  
This project requires environment variables to be set for proper operation.

---

## Project Structure
.
├── README.md
├── backend/ # FastAPI backend
│ ├── app/
│ │ ├── audio_processing.py
│ │ ├── docs_processing.py
│ │ ├── image_processing.py
│ │ └── main.py
│ ├── requirements.txt
│ └── venv/ # Python virtual environment (optional)
│
├── frontend/ # React frontend
│ ├── public/
│ └── src/


---

## Requirements
### Backend
- Python 3.10+
- pip

### Frontend
- Node.js 16+
- npm or yarn

---

## Environment Variables
Create a `.env` file in the **root directory** of the project with the following variables:

```env
# Server configuration
PORT=
HOST=

# Plivo API credentials
PLIVO_AUTH_ID=
PLIVO_AUTH_TOKEN=

# Storage (example: AWS S3)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET_NAME=
AWS_S3_REGION=

# Other configuration
OPENAI_API_KEY=

## Installation

### 1. Clone the repository
```git clone https://github.com/AmishiPande/Plivo_Intern_task.git
cd Plivo_Intern_task```

### 2. Backend setup
```cd backend
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
pip install -r requirements.txt```

### 3. Frontend setup
```cd ../frontend
npm install```

## Running the Application
### Backend
```cd backend
source venv/bin/activate
uvicorn app.main:app --reload```

###This will start the FastAPI server at:
```http://127.0.0.1:8000```

## Frontend
### In a new terminal:

```cd frontend
npm start```
This will start the React development server at:
```http://localhost:3000```
