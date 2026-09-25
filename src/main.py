from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from anthropic import Anthropic
from src.services.analyzer import analyze_requirement
from src.models import RequirementRequest, RequirementAnalysis
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Requirements Analyzer is running!"}


@app.post("/analyze")
def analyze(request: RequirementRequest):
    try:
        analysis = analyze_requirement(request.requirement)
       
        return {
            "requirement": request.requirement,
            "analysis": analysis.model_dump()
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )