@echo off
REM Test Runner Script for GramUdyogAI - Windows
REM This script runs all tests and generates coverage reports

echo ========================================
echo GramUdyogAI Testing Suite
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    exit /b 1
)

echo [1/4] Installing test dependencies...
pip install -r requirements-test.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    exit /b 1
)

echo.
echo [2/4] Running all tests...
pytest tests/ -v --tb=short
if errorlevel 1 (
    echo WARNING: Some tests failed
)

echo.
echo [3/4] Generating coverage report...
pytest tests/ --cov=../../GramUdyogAI/backend --cov-report=html --cov-report=term-missing
if errorlevel 1 (
    echo WARNING: Coverage report generation had issues
)

echo.
echo [4/4] Running specific test categories...
echo.
echo Running Unit Tests...
pytest tests/ -m unit -v
echo.
echo Running Integration Tests...
pytest tests/ -m integration -v
echo.
echo Running API Tests...
pytest tests/ -m api -v

echo.
echo ========================================
echo Testing Complete!
echo ========================================
echo Coverage report available at: htmlcov/index.html
echo.

pause
