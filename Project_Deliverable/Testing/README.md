# Quick Start Guide - GramUdyogAI Testing

## 🚀 Quick Setup (5 Minutes)

### 1. Navigate to Testing Directory
```bash
cd "Project_Deliverable/Testing"
```

### 2. Install Dependencies
```bash
pip install -r requirements-test.txt
```

### 3. Run Tests
**Windows:**
```bash
run_tests.bat
```

**Linux/Mac:**
```bash
chmod +x run_tests.sh
./run_tests.sh
```

---

## 📊 What Gets Tested?

✅ **Authentication** - User registration, login, JWT tokens  
✅ **Business Suggestions** - AI-powered recommendations  
✅ **Government Schemes** - Search and filtering  
✅ **Jobs** - Posting, searching, CRUD operations  
✅ **Courses** - Listings and suggestions  
✅ **Events & Projects** - Hackathon platform  
✅ **Multilingual Support** - Translation features  
✅ **User Workflows** - Complete user journeys  

---

## 🎯 Common Commands

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Tests
```bash
# Authentication tests only
pytest tests/test_api_auth.py -v

# Integration tests only
pytest tests/ -m integration -v
```

### Generate Coverage Report
```bash
pytest tests/ --cov=../../GramUdyogAI/backend --cov-report=html
```
Then open `htmlcov/index.html` in your browser.

---

## 📁 Test Files Overview

| File | What It Tests |
|------|---------------|
| `test_api_auth.py` | User authentication & authorization |
| `test_api_business.py` | Business suggestion engine |
| `test_api_schemes.py` | Government schemes database |
| `test_api_jobs.py` | Job listings & applications |
| `test_api_courses.py` | Course recommendations |
| `test_api_features.py` | Translation, audio, profile |
| `test_api_events.py` | Events, projects, notifications |
| `test_integration.py` | Complete user workflows |

---

## 🛠️ Tools Used

- **pytest** - Testing framework
- **FastAPI TestClient** - API testing
- **pytest-cov** - Code coverage
- **httpx** - HTTP requests

---

## 📖 Need More Help?

See the full documentation: [TESTING_GUIDE.md](TESTING_GUIDE.md)

---

## ✅ Expected Results

When you run the tests, you should see:
- ✅ Green checkmarks for passing tests
- 📊 Coverage percentage (target: >80%)
- 📝 HTML coverage report in `htmlcov/` folder
- ⚠️ Any failing tests will be highlighted in red

---

**Happy Testing! 🎉**
