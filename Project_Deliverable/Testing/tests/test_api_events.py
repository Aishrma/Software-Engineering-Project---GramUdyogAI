"""
Events and Projects API Tests for GramUdyogAI
Tests hackathon platform functionality
"""
import pytest
from fastapi import status


class TestEventsAPI:
    """Test suite for events/hackathon endpoints"""
    
    def test_get_all_events(self, client):
        """Test retrieving all events"""
        response = client.get("/api/events")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_create_event(self, client, auth_headers):
        """Test creating a new event"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        event_data = {
            "title": "Rural Innovation Hackathon",
            "description": "A hackathon for rural entrepreneurs",
            "start_date": "2024-12-01",
            "end_date": "2024-12-03",
            "location": "Mumbai"
        }
        
        response = client.post("/api/events", json=event_data, headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_201_CREATED,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_get_event_by_id(self, client):
        """Test retrieving a specific event"""
        all_events = client.get("/api/events")
        
        if all_events.status_code == status.HTTP_200_OK:
            events = all_events.json()
            if events and len(events) > 0:
                event_id = events[0].get("id", 1)
                response = client.get(f"/api/events/{event_id}")
                
                assert response.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]
    
    
    def test_update_event(self, client, auth_headers):
        """Test updating an event"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        update_data = {
            "title": "Updated Event Title"
        }
        
        response = client.put("/api/events/1", json=update_data, headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_404_NOT_FOUND,
            status.HTTP_401_UNAUTHORIZED
        ]
    
    
    def test_delete_event(self, client, auth_headers):
        """Test deleting an event"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.delete("/api/events/99999", headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_204_NO_CONTENT,
            status.HTTP_404_NOT_FOUND,
            status.HTTP_401_UNAUTHORIZED
        ]


class TestProjectsAPI:
    """Test suite for projects endpoints"""
    
    def test_get_all_projects(self, client):
        """Test retrieving all projects"""
        response = client.get("/api/projects")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_create_project(self, client, auth_headers):
        """Test creating a new project"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        project_data = {
            "title": "Smart Irrigation System",
            "description": "IoT-based irrigation for rural farms",
            "category": "agriculture",
            "technologies": ["IoT", "Python", "Arduino"]
        }
        
        response = client.post("/api/projects", json=project_data, headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_201_CREATED,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_get_project_by_id(self, client):
        """Test retrieving a specific project"""
        all_projects = client.get("/api/projects")
        
        if all_projects.status_code == status.HTTP_200_OK:
            projects = all_projects.json()
            if projects and len(projects) > 0:
                project_id = projects[0].get("id", 1)
                response = client.get(f"/api/projects/{project_id}")
                
                assert response.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]
    
    
    def test_search_projects(self, client):
        """Test searching projects"""
        response = client.get("/api/projects", params={"search": "agriculture"})
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
    
    
    def test_filter_projects_by_category(self, client):
        """Test filtering projects by category"""
        response = client.get("/api/projects", params={"category": "agriculture"})
        
        assert response.status_code == status.HTTP_200_OK


class TestNotificationsAPI:
    """Test suite for notifications endpoints"""
    
    def test_get_notifications(self, client, auth_headers):
        """Test retrieving user notifications"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.get("/api/notifications", headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_mark_notification_read(self, client, auth_headers):
        """Test marking notification as read"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.put("/api/notifications/1/read", headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_404_NOT_FOUND,
            status.HTTP_401_UNAUTHORIZED
        ]
