"""
Pytest Configuration and Fixtures for GramUdyogAI Testing
"""
import os
import sys
import pytest
from fastapi.testclient import TestClient
from typing import Generator

# Add backend directory to path
backend_path = os.path.join(os.path.dirname(__file__), '..', '..', 'GramUdyogAI', 'backend')
sys.path.insert(0, backend_path)

# Set test environment variables
os.environ['TESTING'] = 'true'
os.environ['DATABASE_URL'] = 'sqlite:///./test_database.db'


@pytest.fixture(scope="session")
def test_app():
    """Create a test FastAPI application instance"""
    from main import app
    return app


@pytest.fixture(scope="function")
def client(test_app) -> Generator:
    """Create a test client for API testing"""
    with TestClient(test_app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def auth_headers(client):
    """Create authentication headers for protected endpoints"""
    # Register a test user
    register_data = {
        "email": "test@example.com",
        "password": "TestPassword123!",
        "full_name": "Test User",
        "user_type": "individual"
    }
    
    # Try to register (might fail if user exists)
    client.post("/api/auth/register", json=register_data)
    
    # Login to get token
    login_data = {
        "username": "test@example.com",
        "password": "TestPassword123!"
    }
    response = client.post("/api/auth/login", data=login_data)
    
    if response.status_code == 200:
        token = response.json().get("access_token")
        return {"Authorization": f"Bearer {token}"}
    
    return {}


@pytest.fixture(scope="function")
def sample_user_data():
    """Sample user data for testing"""
    return {
        "email": "newuser@example.com",
        "password": "SecurePass123!",
        "full_name": "New Test User",
        "user_type": "individual",
        "phone": "+919876543210",
        "location": "Mumbai, Maharashtra"
    }


@pytest.fixture(scope="function")
def sample_business_data():
    """Sample business suggestion request data"""
    return {
        "skills": "farming, dairy, organic products",
        "resources": "5 acres land, water source, cattle",
        "location": "Rural Maharashtra",
        "budget": "500000"
    }


@pytest.fixture(scope="function")
def sample_scheme_filter():
    """Sample scheme filter parameters"""
    return {
        "category": "agriculture",
        "state": "Maharashtra",
        "beneficiary_type": "farmer"
    }


@pytest.fixture(autouse=True)
def cleanup_test_files():
    """Cleanup test files after each test"""
    yield
    # Cleanup logic here if needed
    test_db = "test_database.db"
    if os.path.exists(test_db):
        try:
            os.remove(test_db)
        except:
            pass


@pytest.fixture
def mock_ai_response():
    """Mock AI response for testing"""
    return {
        "suggestions": [
            {
                "business_name": "Organic Dairy Farm",
                "description": "Start an organic dairy farm with your cattle and land",
                "investment": "300000-500000",
                "roi": "20-25% annually",
                "feasibility": "high"
            }
        ]
    }
