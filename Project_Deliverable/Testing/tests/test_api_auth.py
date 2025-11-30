"""
Authentication API Tests for GramUdyogAI
Tests user registration, login, and authentication flows
"""
import pytest
from fastapi import status


class TestAuthenticationAPI:
    """Test suite for authentication endpoints"""
    
    def test_user_registration_success(self, client, sample_user_data):
        """Test successful user registration"""
        response = client.post("/api/auth/register", json=sample_user_data)
        
        # Should return 200 or 201 for successful registration
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
        
        data = response.json()
        assert "id" in data or "user_id" in data or "message" in data
    
    
    def test_user_registration_duplicate_email(self, client, sample_user_data):
        """Test registration with duplicate email"""
        # Register first time
        client.post("/api/auth/register", json=sample_user_data)
        
        # Try to register again with same email
        response = client.post("/api/auth/register", json=sample_user_data)
        
        # Should return error for duplicate
        assert response.status_code in [status.HTTP_400_BAD_REQUEST, status.HTTP_409_CONFLICT]
    
    
    def test_user_registration_invalid_email(self, client, sample_user_data):
        """Test registration with invalid email format"""
        sample_user_data["email"] = "invalid-email"
        response = client.post("/api/auth/register", json=sample_user_data)
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    
    def test_user_registration_weak_password(self, client, sample_user_data):
        """Test registration with weak password"""
        sample_user_data["password"] = "123"
        response = client.post("/api/auth/register", json=sample_user_data)
        
        # Should reject weak password
        assert response.status_code in [status.HTTP_400_BAD_REQUEST, status.HTTP_422_UNPROCESSABLE_ENTITY]
    
    
    def test_user_login_success(self, client, sample_user_data):
        """Test successful user login"""
        # Register user first
        client.post("/api/auth/register", json=sample_user_data)
        
        # Login
        login_data = {
            "username": sample_user_data["email"],
            "password": sample_user_data["password"]
        }
        response = client.post("/api/auth/login", data=login_data)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    
    def test_user_login_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        login_data = {
            "username": "nonexistent@example.com",
            "password": "WrongPassword123!"
        }
        response = client.post("/api/auth/login", data=login_data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    
    def test_user_login_missing_fields(self, client):
        """Test login with missing required fields"""
        response = client.post("/api/auth/login", data={})
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    
    def test_protected_endpoint_without_token(self, client):
        """Test accessing protected endpoint without authentication"""
        response = client.get("/api/profile")
        
        # Should return 401 Unauthorized
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    
    def test_protected_endpoint_with_token(self, client, auth_headers):
        """Test accessing protected endpoint with valid token"""
        if not auth_headers:
            pytest.skip("Authentication headers not available")
        
        response = client.get("/api/profile", headers=auth_headers)
        
        # Should return success or redirect
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_307_TEMPORARY_REDIRECT]
    
    
    def test_protected_endpoint_with_invalid_token(self, client):
        """Test accessing protected endpoint with invalid token"""
        headers = {"Authorization": "Bearer invalid_token_12345"}
        response = client.get("/api/profile", headers=headers)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.integration
class TestAuthenticationFlow:
    """Integration tests for complete authentication flows"""
    
    def test_complete_registration_login_flow(self, client, sample_user_data):
        """Test complete flow: register -> login -> access protected resource"""
        # Step 1: Register
        register_response = client.post("/api/auth/register", json=sample_user_data)
        assert register_response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
        
        # Step 2: Login
        login_data = {
            "username": sample_user_data["email"],
            "password": sample_user_data["password"]
        }
        login_response = client.post("/api/auth/login", data=login_data)
        assert login_response.status_code == status.HTTP_200_OK
        
        token = login_response.json()["access_token"]
        
        # Step 3: Access protected resource
        headers = {"Authorization": f"Bearer {token}"}
        profile_response = client.get("/api/profile", headers=headers)
        assert profile_response.status_code in [status.HTTP_200_OK, status.HTTP_307_TEMPORARY_REDIRECT]
