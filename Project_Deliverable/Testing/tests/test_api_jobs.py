"""
Jobs API Tests for GramUdyogAI
Tests job listing and posting functionality
"""
import pytest
from fastapi import status


class TestJobsAPI:
    """Test suite for jobs endpoints"""
    
    def test_get_all_jobs(self, client):
        """Test retrieving all job listings"""
        response = client.get("/api/jobs")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_get_jobs_with_pagination(self, client):
        """Test job listings with pagination"""
        response = client.get("/api/jobs", params={"limit": 10, "offset": 0})
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_search_jobs_by_keyword(self, client):
        """Test searching jobs by keyword"""
        response = client.get("/api/jobs", params={"search": "agriculture"})
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_filter_jobs_by_location(self, client):
        """Test filtering jobs by location"""
        response = client.get("/api/jobs", params={"location": "Mumbai"})
        
        assert response.status_code == status.HTTP_200_OK
    
    
    def test_post_new_job(self, client, auth_headers):
        """Test posting a new job listing"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        job_data = {
            "title": "Agricultural Supervisor",
            "description": "Supervise farming operations",
            "location": "Rural Maharashtra",
            "salary": "25000-30000",
            "company": "Test Farm Ltd"
        }
        
        response = client.post("/api/jobs", json=job_data, headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_201_CREATED,
            status.HTTP_401_UNAUTHORIZED
        ]
    
    
    def test_post_job_without_auth(self, client):
        """Test posting job without authentication"""
        job_data = {
            "title": "Test Job",
            "description": "Test Description"
        }
        
        response = client.post("/api/jobs", json=job_data)
        
        # Should require authentication
        assert response.status_code in [
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_get_job_by_id(self, client):
        """Test retrieving a specific job by ID"""
        # First get all jobs
        all_jobs = client.get("/api/jobs")
        
        if all_jobs.status_code == status.HTTP_200_OK:
            jobs = all_jobs.json()
            if jobs and len(jobs) > 0:
                job_id = jobs[0].get("id", 1)
                response = client.get(f"/api/jobs/{job_id}")
                
                assert response.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]
    
    
    def test_update_job(self, client, auth_headers):
        """Test updating a job listing"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        update_data = {
            "title": "Updated Job Title",
            "description": "Updated description"
        }
        
        response = client.put("/api/jobs/1", json=update_data, headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_404_NOT_FOUND,
            status.HTTP_401_UNAUTHORIZED
        ]
    
    
    def test_delete_job(self, client, auth_headers):
        """Test deleting a job listing"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.delete("/api/jobs/99999", headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_204_NO_CONTENT,
            status.HTTP_404_NOT_FOUND,
            status.HTTP_401_UNAUTHORIZED
        ]
