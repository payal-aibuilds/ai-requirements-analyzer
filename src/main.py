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
            model="claude-haiku-4-5-20251001",  # cheapest/fastest model — good for trial runs
            max_tokens=2000,  # kept low for testing; raise if outputs get truncated
            tools=[
                {
                    "name": "submit_requirement_analysis",
                    "description": "Submit the structured business requirement analysis.",
                    "input_schema": RequirementAnalysis.model_json_schema(),
                }
            ],
            tool_choice={"type": "tool", "name": "submit_requirement_analysis"},
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are an expert Business Analyst and Solution Architect.

Analyze this business requirement:

{request.requirement}

Return a complete structured analysis.

You MUST provide ALL of these seven fields:

1. problem_statement
2. functional_requirements
3. non_functional_requirements
4. user_stories
5. acceptance_criteria
6. risks_and_assumptions
7. architecture

IMPORTANT:
- Do not omit any field.
- All seven fields must always be present.
- For list fields, return a list even if there is only one item.
- If something genuinely does not apply, return [].
- The architecture field must always contain a concise high-level architecture description.
- Do not return explanations outside these fields.
"""
                }
            ]
        )

        tool_use_block = next(
            block for block in response.content if block.type == "tool_use"
        )

        analysis = RequirementAnalysis(**tool_use_block.input)

        return {
            "requirement": request.requirement,
            "analysis": analysis.model_dump()
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )