# AI Requirements Analyzer

An AI-powered application that transforms unstructured business requirements into structured product and technical specifications.

## Overview

Business requirements are often incomplete, ambiguous, or written in natural language. This project demonstrates how AI can help Business Analysts, Product Owners, and technology consultants transform those requirements into structured, actionable specifications.

The application accepts a natural-language business requirement and generates:

* Problem statement
* Functional requirements
* Non-functional requirements
* User stories
* Acceptance criteria
* Risks and assumptions
* High-level technical architecture

## Example

### Input

```text
Customers should be able to track their orders online.
```

### Output

The application converts the requirement into a structured analysis containing the underlying problem, functional and non-functional requirements, user stories, acceptance criteria, risks and assumptions, and a suggested architecture.

## Architecture

```text
User
  │
  ▼
FastAPI API
  │
  ▼
Request Validation
(Pydantic)
  │
  ▼
AI Analysis Service
  │
  ▼
OpenAI Responses API
  │
  ▼
Structured Pydantic Output
  │
  ▼
JSON Response
```

## Project Structure

```text
ai-requirements-analyzer/
│
├── src/
│   ├── main.py
│   ├── models.py
│   └── services/
│       └── analyzer.py
│
├── tests/
│   └── test_main.py
│
├── docs/
│
├── .env
├── .gitignore
└── README.md
```

### Responsibilities

**`main.py`**

* FastAPI application
* API routes
* HTTP error handling

**`models.py`**

* Request and response schemas
* Pydantic validation

**`services/analyzer.py`**

* AI analysis logic
* OpenAI API integration
* Structured output generation

**`tests/`**

* API tests
* Validation tests
* AI failure handling tests

## Tech Stack

* Python
* FastAPI
* Pydantic
* OpenAI Responses API
* Uvicorn
* pytest
* Git
* GitHub

## API

### `GET /`

Health/basic application endpoint.

### `POST /analyze`

Analyzes an unstructured business requirement.

Example request:

```json
{
  "requirement": "Customers should be able to track their orders online."
}
```

The endpoint returns a structured analysis containing seven output categories.

## Validation & Error Handling

The application validates incoming requests using Pydantic and handles failures from the AI analysis layer through controlled HTTP responses.

The project also includes automated tests covering:

* Successful API requests
* Requirement analysis flow
* Invalid request validation
* AI service failures

Run the test suite with:

```bash
python -m pytest
```

## Local Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/payal-aibuilds/ai-requirements-analyzer.git
cd ai-requirements-analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it and install dependencies.

Create a `.env` file containing:

```text
OPENAI_API_KEY=your_api_key_here
```

Start the application:

```bash
python -m uvicorn src.main:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Current Status

🟢 Core MVP implemented

* AI-powered requirement analysis
* Structured output validation
* FastAPI API
* Modular service architecture
* Error handling
* Automated tests

## Future Development

Planned extensions include:

* Public cloud deployment
* Web-based user interface
* AI agent capabilities
* External tools and integrations
* Retrieval-Augmented Generation (RAG)
* Model evaluation and observability

## Purpose

This project is part of a portfolio demonstrating the intersection of:

**Business Analysis + Product Thinking + Software Engineering + AI**

The goal is to demonstrate the ability to translate business problems into technical solutions and implement those solutions end-to-end.
