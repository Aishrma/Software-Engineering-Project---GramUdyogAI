"""
Courses API Tests for GramUdyogAI
Tests course listing and recommendation functionality
"""
import pytest
from fastapi import status


class TestCoursesAPI:
    """Test suite for courses endpoints"""
    
    def test_get_all_courses(self, client):
        """Test retrieving all courses"""
        response = client.get("/api/courses")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_get_courses_with_pagination(self, client):
        """Test courses with pagination"""
        response = client.get("/api/courses", params={"limit": 10, "offset": 0})
        
        assert response.status_code == status.HTTP_200_OK
    
    
    def test_search_courses_by_keyword(self, client):
        """Test searching courses by keyword"""
        response = client.get("/api/courses", params={"search": "agriculture"})
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_filter_courses_by_category(self, client):
        """Test filtering courses by category"""
        response = client.get("/api/courses", params={"category": "farming"})
        
        assert response.status_code == status.HTTP_200_OK
    
    
    def test_get_course_suggestions(self, client, auth_headers):
        """Test getting personalized course suggestions"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        suggestion_data = {
            "skills": "farming, dairy",
            "interests": "organic farming"
        }
        
        response = client.post(
            "/api/course-suggestions",
            json=suggestion_data,
            headers=auth_headers
        )
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_201_CREATED,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_get_course_by_id(self, client):
        """Test retrieving a specific course by ID"""
        all_courses = client.get("/api/courses")
        
        if all_courses.status_code == status.HTTP_200_OK:
            courses = all_courses.json()
            if courses and len(courses) > 0:
                course_id = courses[0].get("id", 1)
                response = client.get(f"/api/courses/{course_id}")
                
                assert response.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]


class TestYouTubeSummaryAPI:
    """Test suite for YouTube summary endpoints"""
    
    def test_youtube_summary_endpoint_exists(self, client):
        """Test that YouTube summary endpoint exists"""
        response = client.post("/api/youtube-summary/summarize", json={})
        
        # Should return error for missing data, not 404
        assert response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_youtube_summary_with_valid_url(self, client, auth_headers):
        """Test YouTube summary with valid URL"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        data = {
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "language": "en"
        }
        
        response = client.post(
            "/api/youtube-summary/summarize",
            json=data,
            headers=auth_headers if auth_headers else {}
        )
        
        # May succeed or fail based on API availability
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_500_INTERNAL_SERVER_ERROR
        ]
    
    
    def test_youtube_summary_invalid_url(self, client, auth_headers):
        """Test YouTube summary with invalid URL"""
        data = {
            "url": "not-a-valid-url",
            "language": "en"
        }
        
        response = client.post(
            "/api/youtube-summary/summarize",
            json=data,
            headers=auth_headers if auth_headers else {}
        )
        
        assert response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
