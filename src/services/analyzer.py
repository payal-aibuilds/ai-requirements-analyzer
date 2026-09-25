from dotenv import load_dotenv
from anthropic import Anthropic
from src.models import RequirementAnalysis
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def analyze_requirement(requirement: str) -> RequirementAnalysis:
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

{requirement}

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
    return analysis