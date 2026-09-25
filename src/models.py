from pydantic import BaseModel
from typing import List


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