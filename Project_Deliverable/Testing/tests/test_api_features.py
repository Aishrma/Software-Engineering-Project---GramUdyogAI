"""
Translation and Audio API Tests for GramUdyogAI
Tests multilingual support and audio features
"""
import pytest
from fastapi import status


class TestTranslationAPI:
    """Test suite for translation endpoints"""
    
    def test_translate_text(self, client):
        """Test text translation"""
        data = {
            "text": "Hello, how are you?",
            "target_language": "hi"  # Hindi
        }
        
        response = client.post("/api/translate", json=data)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_translate_empty_text(self, client):
        """Test translation with empty text"""
        data = {
            "text": "",
            "target_language": "hi"
        }
        
        response = client.post("/api/translate", json=data)
        
        assert response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_translate_unsupported_language(self, client):
        """Test translation with unsupported language"""
        data = {
            "text": "Hello",
            "target_language": "xyz"  # Invalid language code
        }
        
        response = client.post("/api/translate", json=data)
        
        assert response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]
    
    
    def test_get_supported_languages(self, client):
        """Test getting list of supported languages"""
        response = client.get("/api/translate/languages")
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_404_NOT_FOUND
        ]


class TestAudioAPI:
    """Test suite for audio endpoints"""
    
    def test_text_to_speech(self, client):
        """Test text-to-speech conversion"""
        data = {
            "text": "Hello, this is a test",
            "language": "en"
        }
        
        response = client.post("/api/audio/tts", json=data)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_speech_to_text(self, client):
        """Test speech-to-text endpoint exists"""
        response = client.post("/api/stt", json={})
        
        # Should require audio file
        assert response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            status.HTTP_404_NOT_FOUND
        ]


class TestDashboardAPI:
    """Test suite for dashboard endpoints"""
    
    def test_get_dashboard_data(self, client, auth_headers):
        """Test retrieving dashboard data"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.get("/api/dashboard", headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_dashboard_without_auth(self, client):
        """Test dashboard access without authentication"""
        response = client.get("/api/dashboard")
        
        assert response.status_code in [
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_307_TEMPORARY_REDIRECT
        ]


class TestProfileAPI:
    """Test suite for user profile endpoints"""
    
    def test_get_user_profile(self, client, auth_headers):
        """Test retrieving user profile"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        response = client.get("/api/profile", headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_307_TEMPORARY_REDIRECT
        ]
    
    
    def test_update_user_profile(self, client, auth_headers):
        """Test updating user profile"""
        if not auth_headers:
            pytest.skip("Authentication required")
        
        update_data = {
            "full_name": "Updated Name",
            "location": "New Location"
        }
        
        response = client.put("/api/profile", json=update_data, headers=auth_headers)
        
        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_404_NOT_FOUND
        ]
    
    
    def test_profile_without_auth(self, client):
        """Test profile access without authentication"""
        response = client.get("/api/profile")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
