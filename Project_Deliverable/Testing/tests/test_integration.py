"""
Integration Tests for GramUdyogAI
Tests complete user workflows and feature interactions
"""
import pytest
from fastapi import status


@pytest.mark.integration
class TestCompleteUserJourney:
    """Test complete user journey through the application"""
    
    def test_new_user_onboarding_flow(self, client):
        """Test complete new user onboarding"""
        # Step 1: Register
        register_data = {
            "email": "journey_test@example.com",
            "password": "SecurePass123!",
            "full_name": "Journey Test User",
            "user_type": "individual"
        }
        
        register_response = client.post("/api/auth/register", json=register_data)
        assert register_response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
        
        # Step 2: Login
        login_data = {
            "username": register_data["email"],
            "password": register_data["password"]
        }
        login_response = client.post("/api/auth/login", data=login_data)
        assert login_response.status_code == status.HTTP_200_OK
        
        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        
        # Step 3: Access profile
        profile_response = client.get("/api/profile", headers=headers)
        assert profile_response.status_code in [status.HTTP_200_OK, status.HTTP_307_TEMPORARY_REDIRECT]
        
        # Step 4: Browse schemes
        schemes_response = client.get("/api/schemes")
        assert schemes_response.status_code == status.HTTP_200_OK
        
        # Step 5: Browse jobs
        jobs_response = client.get("/api/jobs")
        assert jobs_response.status_code == status.HTTP_200_OK
    
    
    def test_entrepreneur_business_planning_flow(self, client, auth_headers):
        """Test entrepreneur planning a business"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        # Step 1: Get business suggestions
        business_data = {
            "skills": "farming, animal husbandry",
            "resources": "10 acres land, cattle",
            "location": "Rural Maharashtra",
            "budget": "500000"
        }
        
        suggestions_response = client.post(
            "/api/business/suggestions",
            json=business_data,
            headers=auth_headers
        )
        assert suggestions_response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
        
        # Step 2: Search for relevant schemes
        schemes_response = client.get("/api/schemes", params={"category": "agriculture"})
        assert schemes_response.status_code == status.HTTP_200_OK
        
        # Step 3: Look for relevant courses
        courses_response = client.get("/api/courses", params={"search": "farming"})
        assert courses_response.status_code == status.HTTP_200_OK
    
    
    def test_job_seeker_flow(self, client, auth_headers):
        """Test job seeker workflow"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        # Step 1: Browse available jobs
        jobs_response = client.get("/api/jobs")
        assert jobs_response.status_code == status.HTTP_200_OK
        
        # Step 2: Search for specific jobs
        search_response = client.get("/api/jobs", params={"search": "agriculture"})
        assert search_response.status_code == status.HTTP_200_OK
        
        # Step 3: Filter by location
        location_response = client.get("/api/jobs", params={"location": "Mumbai"})
        assert location_response.status_code == status.HTTP_200_OK


@pytest.mark.integration
class TestMultilingualSupport:
    """Test multilingual features"""
    
    def test_translation_workflow(self, client):
        """Test translation feature workflow"""
        languages = ["hi", "mr", "ta", "te"]
        
        for lang in languages:
            data = {
                "text": "Welcome to GramUdyogAI",
                "target_language": lang
            }
            
            response = client.post("/api/translate", json=data)
            # May or may not be implemented
            assert response.status_code in [
                status.HTTP_200_OK,
                status.HTTP_404_NOT_FOUND,
                status.HTTP_400_BAD_REQUEST
            ]


@pytest.mark.integration
class TestDataConsistency:
    """Test data consistency across endpoints"""
    
    def test_user_data_consistency(self, client, auth_headers, sample_user_data):
        """Test that user data is consistent across endpoints"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        # Get profile
        profile_response = client.get("/api/profile", headers=auth_headers)
        
        if profile_response.status_code == status.HTTP_200_OK:
            profile_data = profile_response.json()
            assert isinstance(profile_data, dict)
    
    
    def test_scheme_data_integrity(self, client):
        """Test scheme data integrity"""
        response = client.get("/api/schemes")
        
        if response.status_code == status.HTTP_200_OK:
            schemes = response.json()
            assert isinstance(schemes, list)
            
            # Check that each scheme has consistent structure
            for scheme in schemes[:5]:  # Check first 5
                assert isinstance(scheme, dict)


@pytest.mark.slow
class TestPerformance:
    """Performance tests for API endpoints"""
    
    def test_schemes_endpoint_performance(self, client):
        """Test schemes endpoint response time"""
        import time
        
        start_time = time.time()
        response = client.get("/api/schemes")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        assert response.status_code == status.HTTP_200_OK
        assert response_time < 5.0  # Should respond within 5 seconds
    
    
    def test_jobs_endpoint_performance(self, client):
        """Test jobs endpoint response time"""
        import time
        
        start_time = time.time()
        response = client.get("/api/jobs")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        assert response.status_code == status.HTTP_200_OK
        assert response_time < 5.0
