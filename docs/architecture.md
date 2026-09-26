# Architecture

## High-Level Architecture

```text
┌─────────────────────────────┐
│            User             │
│  Business Requirement Input │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│         FastAPI API         │
│        POST /analyze        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Pydantic Validation     │
│     RequirementRequest      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     AI Analysis Service     │
│     services/analyzer.py    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    OpenAI Responses API     │
│       Structured Output     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Pydantic Validation     │
│    RequirementAnalysis      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        JSON Response        │
│                             │
│ • Problem Statement         │
│ • Functional Requirements   │
│ • Non-functional Reqs.      │
│ • User Stories              │
│ • Acceptance Criteria       │
│ • Risks & Assumptions       │
│ • Architecture              │
└─────────────────────────────┘