#!/bin/bash
# Test Runner Script for GramUdyogAI - Linux/Mac
# This script runs all tests and generates coverage reports

echo "========================================"
echo "GramUdyogAI Testing Suite"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

echo "[1/4] Installing test dependencies..."
pip install -r requirements-test.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "[2/4] Running all tests..."
pytest tests/ -v --tb=short

echo ""
echo "[3/4] Generating coverage report..."
pytest tests/ --cov=../../GramUdyogAI/backend --cov-report=html --cov-report=term-missing

echo ""
echo "[4/4] Running specific test categories..."
echo ""
echo "Running Unit Tests..."
pytest tests/ -m unit -v
echo ""
echo "Running Integration Tests..."
pytest tests/ -m integration -v
echo ""
echo "Running API Tests..."
pytest tests/ -m api -v

echo ""
echo "========================================"
echo "Testing Complete!"
echo "========================================"
echo "Coverage report available at: htmlcov/index.html"
echo ""
