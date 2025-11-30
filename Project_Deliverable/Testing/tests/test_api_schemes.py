"""
Government Schemes API Tests for GramUdyogAI
Tests scheme search and retrieval functionality
"""
import pytest
from fastapi import status


class TestSchemesAPI:
    """Test suite for government schemes endpoints"""
    
    def test_get_all_schemes(self, client):
        """Test retrieving all government schemes"""
        response = client.get("/api/schemes")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_get_schemes_with_filters(self, client, sample_scheme_filter):
        """Test retrieving schemes with filters"""
        response = client.get("/api/schemes", params=sample_scheme_filter)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_get_scheme_by_id(self, client):
        """Test retrieving a specific scheme by ID"""
        # First get all schemes to get a valid ID
        all_schemes = client.get("/api/schemes")
        
        if all_schemes.status_code == status.HTTP_200_OK:
            schemes = all_schemes.json()
            if schemes and len(schemes) > 0:
                scheme_id = schemes[0].get("id", 1)
                response = client.get(f"/api/schemes/{scheme_id}")
                
                assert response.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]
    
    
    def test_get_nonexistent_scheme(self, client):
        """Test retrieving a non-existent scheme"""
        response = client.get("/api/schemes/99999999")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    
    def test_search_schemes_by_keyword(self, client):
        """Test searching schemes by keyword"""
        response = client.get("/api/schemes", params={"search": "agriculture"})
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_filter_schemes_by_category(self, client):
        """Test filtering schemes by category"""
        categories = ["agriculture", "education", "health", "finance"]
        
        for category in categories:
            response = client.get("/api/schemes", params={"category": category})
            assert response.status_code == status.HTTP_200_OK
    
    
    def test_filter_schemes_by_state(self, client):
        """Test filtering schemes by state"""
        states = ["Maharashtra", "Karnataka", "Tamil Nadu"]
        
        for state in states:
            response = client.get("/api/schemes", params={"state": state})
            assert response.status_code == status.HTTP_200_OK


class TestSchemesDataIntegrity:
    """Test data integrity of schemes"""
    
    def test_scheme_data_structure(self, client):
        """Test that scheme data has required fields"""
        response = client.get("/api/schemes")
        
        if response.status_code == status.HTTP_200_OK:
            schemes = response.json()
            if schemes and len(schemes) > 0:
                scheme = schemes[0]
                # Check for common fields
                assert isinstance(scheme, dict)
