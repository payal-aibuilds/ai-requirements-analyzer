from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import List
from fastapi import FastAPI, HTTPException
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI()


class RequirementRequest(BaseModel):
    requirement: str


class RequirementAnalysis(BaseModel):
    problem_statement: str
    functional_requirements: List[str]
    non_functional_requirements: List[str]
    user_stories: List[str]
    acceptance_criteria: List[str]
    risks_and_assumptions: List[str]
    architecture: str


@app.get("/")
def home():
    return {"message": "AI Requirements Analyzer is running!"}


@app.post("/analyze")
def analyze_requirement(request: RequirementRequest):
    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are an expert Business Analyst and Solution Architect.

Analyze the following business requirement:

{request.requirement}

Return the analysis using exactly these sections:
Problem statement
Functional requirements
Non-functional requirements
User stories
Acceptance criteria
Risks and assumptions
Suggested high-level architecture
"""
                }
            ]
        )

        return {
            "requirement": request.requirement,
            "analysis": response.content[0].text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )