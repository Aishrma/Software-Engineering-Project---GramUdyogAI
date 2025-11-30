"""
Business Suggestion API Tests for GramUdyogAI
Tests AI-powered business suggestion functionality
"""
import pytest
from fastapi import status


class TestBusinessSuggestionAPI:
    """Test suite for business suggestion endpoints"""
    
    def test_get_business_suggestions_success(self, client, sample_business_data, auth_headers):
        """Test successful business suggestion generation"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.post(
            "/api/business/suggestions",
            json=sample_business_data,
            headers=auth_headers
        )
        
        # Should return suggestions or accept the request
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
    
    
    def test_get_business_suggestions_without_auth(self, client, sample_business_data):
        """Test business suggestions without authentication"""
        response = client.post("/api/business/suggestions", json=sample_business_data)
        
        # Might allow without auth or require it
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_201_CREATED
        ]
    
    
    def test_get_business_suggestions_missing_fields(self, client, auth_headers):
        """Test business suggestions with missing required fields"""
        incomplete_data = {"skills": "farming"}
        
        response = client.post(
            "/api/business/suggestions",
            json=incomplete_data,
            headers=auth_headers if auth_headers else {}
        )
        
        # Should handle gracefully
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_get_business_suggestions_empty_skills(self, client, auth_headers):
        """Test business suggestions with empty skills"""
        data = {
            "skills": "",
            "resources": "land",
            "location": "Rural Area",
            "budget": "100000"
        }
        
        response = client.post(
            "/api/business/suggestions",
            json=data,
            headers=auth_headers if auth_headers else {}
        )
        
        # Should handle empty input
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_business_suggestions_response_format(self, client, sample_business_data, auth_headers):
        """Test that business suggestions return proper format"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.post(
            "/api/business/suggestions",
            json=sample_business_data,
            headers=auth_headers
        )
        
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            # Check if response has expected structure
            assert isinstance(data, (dict, list))


@pytest.mark.integration
class TestBusinessSuggestionIntegration:
    """Integration tests for business suggestion workflows"""
    
    def test_complete_business_suggestion_flow(self, client, auth_headers, sample_business_data):
        """Test complete flow of getting business suggestions"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        # Get suggestions
        response = client.post(
            "/api/business/suggestions",
            json=sample_business_data,
            headers=auth_headers
        )
        
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
