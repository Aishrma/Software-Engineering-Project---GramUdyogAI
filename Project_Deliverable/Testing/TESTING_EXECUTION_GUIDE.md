# 🧪 GramUdyogAI Testing Execution Guide

## 📋 Complete Step-by-Step Testing Instructions

This guide will walk you through executing all tests and capturing screenshots for your Project Deliverable 3.

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Open New Terminal for Testing

1. Open a **NEW** PowerShell/Command Prompt window
2. Navigate to the testing directory:
```bash
cd "C:\Users\Aishwarya Sharma\Desktop\College Work\Semester 5\CSE Core\SE Lab\Project\Final Implementation\Project_Deliverable\Testing"
```

### Step 2: Install Testing Dependencies

```bash
pip install -r requirements-test.txt
```

**⏱️ This will take 2-3 minutes**

**📸 SCREENSHOT 1**: Take screenshot after installation completes showing "Successfully installed..." message

---

## 🧪 Running Tests

### Method 1: Run All Tests (Recommended)

```bash
pytest tests/ -v
```

**📸 SCREENSHOT 2**: Capture the complete test execution output showing:
- Number of tests passed/failed
- Test names and their status
- Total execution time

### Method 2: Run Tests with Coverage Report

```bash
pytest tests/ --cov=../../GramUdyogAI/backend --cov-report=html --cov-report=term-missing -v
```

**📸 SCREENSHOT 3**: Capture the coverage summary showing:
- Coverage percentage
- Lines covered/missing
- Module-wise coverage

---

## 📊 Viewing Coverage Report

After running tests with coverage:

1. Open the HTML coverage report:
```bash
start htmlcov/index.html
```

2. This will open in your browser

**📸 SCREENSHOT 4**: Capture the HTML coverage report homepage showing:
- Overall coverage percentage
- List of modules with coverage stats
- Color-coded coverage indicators

**📸 SCREENSHOT 5**: Click on any module (e.g., `routes_auth.py`) and capture:
- Line-by-line coverage view
- Green (covered) and red (not covered) lines

---

## 🎯 Running Specific Test Categories

### Run Authentication Tests Only
```bash
pytest tests/test_api_auth.py -v
```

**📸 SCREENSHOT 6**: Capture authentication test results

### Run Integration Tests Only
```bash
pytest tests/ -m integration -v
```

**📸 SCREENSHOT 7**: Capture integration test results

### Run API Tests Only
```bash
pytest tests/ -m api -v
```

---

## 📝 Test Execution Summary

### Expected Results:

| Test Category | File | Expected Tests | Status |
|---------------|------|----------------|--------|
| Authentication | `test_api_auth.py` | 10+ tests | ✅ Should Pass |
| Business | `test_api_business.py` | 5+ tests | ✅ Should Pass |
| Schemes | `test_api_schemes.py` | 8+ tests | ✅ Should Pass |
| Jobs | `test_api_jobs.py` | 9+ tests | ✅ Should Pass |
| Courses | `test_api_courses.py` | 6+ tests | ✅ Should Pass |
| Features | `test_api_features.py` | 12+ tests | ⚠️ Some may skip |
| Events | `test_api_events.py` | 11+ tests | ✅ Should Pass |
| Integration | `test_integration.py` | 6+ tests | ✅ Should Pass |

**Total Expected**: 50+ test cases

---

## 📸 Screenshot Checklist

Here's what you need to capture for your deliverable:

### Required Screenshots:

- [ ] **Screenshot 1**: Test dependencies installation
- [ ] **Screenshot 2**: All tests execution (pytest tests/ -v)
- [ ] **Screenshot 3**: Coverage report in terminal
- [ ] **Screenshot 4**: HTML coverage report homepage
- [ ] **Screenshot 5**: Detailed module coverage view
- [ ] **Screenshot 6**: Authentication tests results
- [ ] **Screenshot 7**: Integration tests results

### Optional (Bonus):

- [ ] **Screenshot 8**: Specific test file execution
- [ ] **Screenshot 9**: Test failure example (if any)
- [ ] **Screenshot 10**: Performance test results

---

## 🛠️ Troubleshooting

### Issue: Tests Fail with Import Errors

**Solution**:
```bash
# Make sure you're in the Testing directory
cd "Project_Deliverable/Testing"

# Reinstall dependencies
pip install -r requirements-test.txt
```

### Issue: Backend Not Running

**Error**: `Connection refused` or `Failed to connect`

**Solution**: Make sure your backend is running:
```bash
# In another terminal
cd "../../GramUdyogAI/backend"
uvicorn main:app --reload
```

### Issue: Some Tests Skip

**This is normal!** Some tests skip when:
- Authentication is not available
- External APIs are not configured
- Optional features are not enabled

**Skipped tests are OK** - they won't affect your grade.

---

## 📊 Understanding Test Results

### Test Status Indicators:

- ✅ **PASSED** (Green): Test succeeded
- ❌ **FAILED** (Red): Test failed - needs investigation
- ⚠️ **SKIPPED** (Yellow): Test skipped - optional feature
- 🔄 **XFAIL** (Blue): Expected failure - known issue

### Coverage Metrics:

- **90-100%**: Excellent coverage ⭐⭐⭐
- **80-89%**: Good coverage ⭐⭐
- **70-79%**: Acceptable coverage ⭐
- **<70%**: Needs improvement

**Target**: Aim for >80% coverage

---

## 📁 Where to Save Screenshots

Create a folder for screenshots:

```bash
mkdir screenshots
```

Save all screenshots in this folder with descriptive names:
- `01_dependencies_installation.png`
- `02_all_tests_execution.png`
- `03_coverage_terminal.png`
- `04_coverage_html_homepage.png`
- `05_coverage_module_detail.png`
- `06_auth_tests.png`
- `07_integration_tests.png`

---

## 📄 Creating Test Report Document

After running all tests, create a summary document:

### Test Execution Report Template:

```markdown
# GramUdyogAI Test Execution Report

## Test Summary
- **Total Tests**: [Number]
- **Passed**: [Number]
- **Failed**: [Number]
- **Skipped**: [Number]
- **Coverage**: [Percentage]%

## Test Results by Category

### 1. Authentication Tests
- Status: ✅ PASSED
- Tests Run: 10
- Coverage: 85%

### 2. Business Suggestion Tests
- Status: ✅ PASSED
- Tests Run: 5
- Coverage: 78%

[Continue for all categories...]

## Screenshots
[Insert screenshots here]

## Conclusion
All critical tests passed successfully with >80% code coverage.
```

---

## 🎓 For Your Deliverable

### What to Submit:

1. **Test Scripts** (Already created ✅)
   - All files in `Project_Deliverable/Testing/` folder

2. **Test Execution Screenshots** (7-10 screenshots)
   - Follow the screenshot checklist above

3. **Test Report** (1-2 pages)
   - Summary of test results
   - Coverage statistics
   - Any issues encountered and resolved

4. **GitHub Repository Link**
   - File: `GITHUB_REPO_LINK.txt` (Already created ✅)

---

## ⚡ Quick Commands Reference

```bash
# Install dependencies
pip install -r requirements-test.txt

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=../../GramUdyogAI/backend --cov-report=html -v

# Run specific test file
pytest tests/test_api_auth.py -v

# Run by marker
pytest tests/ -m integration -v

# Open coverage report
start htmlcov/index.html
```

---

## ✅ Final Checklist

Before submitting:

- [ ] All test dependencies installed
- [ ] All tests executed successfully
- [ ] Coverage report generated (>80%)
- [ ] All required screenshots captured
- [ ] Screenshots saved with descriptive names
- [ ] Test execution report created
- [ ] GitHub repository link verified
- [ ] All documentation reviewed

---

## 🆘 Need Help?

If you encounter any issues:

1. Check the main testing guide: `TESTING_GUIDE.md`
2. Review test file comments for specific test details
3. Ensure backend is running on `http://localhost:8000`
4. Check that database has been initialized

---

**Good Luck with Your Testing! 🚀**

**Estimated Time**: 15-20 minutes for complete testing and screenshot capture
