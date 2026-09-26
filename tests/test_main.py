from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "AI Requirements Analyzer is running!"
    }


def test_analyze_requirement(monkeypatch):
    class MockAnalysis:
        def model_dump(self):
            return {
                "problem_statement": "Customers need visibility into their orders.",
                "functional_requirements": [
                    "Customers can view order status."
                ],
                "non_functional_requirements": [
                    "The system should respond quickly."
                ],
                "user_stories": [
                    "As a customer, I want to track my order."
                ],
                "acceptance_criteria": [
                    "The customer can see the current order status."
                ],
                "risks_and_assumptions": [
                    "The order management system provides status data."
                ],
                "architecture": "Web application connected to an order management API."
            }

    def mock_analyze_requirement(requirement):
        return MockAnalysis()

    monkeypatch.setattr(
        "src.main.analyze_requirement",
        mock_analyze_requirement
    )

    response = client.post(
        "/analyze",
        json={
            "requirement": "Customers should be able to track their orders online."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["requirement"] == (
        "Customers should be able to track their orders online."
    )

    assert "analysis" in data
    assert "problem_statement" in data["analysis"]
    assert "architecture" in data["analysis"]


def test_analyze_requirement_missing_field():
    response = client.post(
        "/analyze",
        json={}
    )

    assert response.status_code == 422
    
def test_analyze_requirement_ai_failure(monkeypatch):
    def mock_analyze_requirement(requirement):
        raise Exception("AI service unavailable")

    monkeypatch.setattr(
        "src.main.analyze_requirement",
        mock_analyze_requirement
    )

    response = client.post(
        "/analyze",
        json={
            "requirement": "Customers should be able to track their orders online."
        }
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "AI analysis failed: AI service unavailable"