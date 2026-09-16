from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import io
import uvicorn

from config.services.gemini_service import (
    generate_outreach,
    parse_response
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    profile: str
    tone: str
    goal: str

@app.post("/api/generate")
async def generate_single(request: GenerateRequest):
    try:
        response = generate_outreach(request.profile, request.tone, request.goal)
        result = parse_response(response)
        return result
    except Exception as e:
        # Return a 400 Bad Request or 500 Internal Server error with the exception details
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-batch")
async def generate_batch(file: UploadFile = File(...), tone: str = Form(...), goal: str = Form(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    
    if "profile" not in df.columns:
        return {"error": "CSV needs a 'profile' column."}
        
    subjects = []
    emails = []
    followups = []

    for index, row in df.iterrows():
        profile = str(row["profile"])
        try:
            response = generate_outreach(profile, tone, goal)
            result = parse_response(response)
            subjects.append(result["subject"])
            emails.append(result["email"])
            followups.append(result["followup"])
        except Exception as e:
            subjects.append("Generation failed")
            emails.append(str(e))
            followups.append("")

    df["generated_subject"] = subjects
    df["generated_email"] = emails
    df["generated_followup"] = followups

    output = io.StringIO()
    df.to_csv(output, index=False)
    
    return {"csv_data": output.getvalue()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
