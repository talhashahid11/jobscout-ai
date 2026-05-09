from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import os

from services.cv_parser import extract_text
from services.ai_extractor import extract_candidate_data
from services.search_jobs import search_jobs
from services.scorer import score_jobs

app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "JobScout AI Running"
    }


@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    try:

        file_path = f"{UPLOAD_FOLDER}/{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # EXTRACT CV TEXT

        cv_text = extract_text(file_path)

        print("CV TEXT EXTRACTED")

        # AI DATA

        candidate_data = extract_candidate_data(cv_text)

        print("AI DATA GENERATED")

        # JOB SEARCH

        jobs = search_jobs(candidate_data)

        print("JOBS FETCHED")

        # AI SCORE

        ranked_jobs = score_jobs(
            candidate_data,
            jobs
        )

        print("JOBS RANKED")

        return {
            "candidate": candidate_data,
            "jobs": ranked_jobs
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "candidate": {},
            "jobs": []
        }