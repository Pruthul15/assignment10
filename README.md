# Assignment 10: Secure User Authentication with SQLAlchemy

## 📋 Project Overview

This project implements a **secure user authentication system** using FastAPI, SQLAlchemy, and bcrypt password hashing. It demonstrates fundamental web security practices including password hashing, database modeling with ORM, input validation with Pydantic schemas, and a complete CI/CD pipeline with GitHub Actions and Docker Hub deployment.

**Status:** ✅ COMPLETE - 43 Tests Passing | 93% Code Coverage | Docker Hub Deployed

---

## 🚀 What We Built

### **1. Secure User Model (SQLAlchemy)**
- SQLAlchemy ORM model with UUID primary key
- Unique constraints on `username` and `email`
- `password_hash` field (never stores plain passwords)
- Timestamp tracking with `created_at`
- Methods: `hash_password()` and `verify_password()` using bcrypt

### **2. Data Validation (Pydantic)**
- `UserCreate` schema for registration with validation
- `UserRead` schema for API responses (excludes password_hash)
- Email format validation
- Password strength requirements (8+ chars, uppercase, lowercase, digit)

### **3. Password Security (Bcrypt)**
- One-way password hashing with automatic salt generation
- Unique hash for each password even if passwords are identical
- Cannot reverse-engineer original password from hash
- Industry standard for secure password storage

### **4. Comprehensive Testing**
- 43 total tests passing
- Unit tests (30) - Password hashing, schemas, calculator logic
- Integration tests (10) - Database operations, API endpoints, constraints
- E2E tests (3) - End-to-end browser automation
- 93% code coverage achieved

### **5. CI/CD Pipeline**
- GitHub Actions workflow for automated testing
- Security scanning with Trivy
- Docker image building and pushing to Docker Hub
- Tests must pass before deployment

---

## 📁 Project Structure

```
assignment10/
├── app/
│   ├── models/
│   │   └── user.py                 # SQLAlchemy User model
│   ├── schemas/
│   │   ├── base.py                 # Base Pydantic schemas
│   │   └── user.py                 # UserCreate, UserRead
│   ├── utils/
│   │   └── security.py             # Password hashing functions
│   ├── config.py                   # Configuration
│   ├── database.py                 # Database connection
│   └── main.py                     # FastAPI app
├── tests/
│   ├── unit/
│   │   ├── test_security.py        # (4 tests)
│   │   ├── test_schemas.py         # (5 tests)
│   │   └── test_calculator.py      # (21 tests)
│   ├── integration/
│   │   ├── test_user.py            # (5 tests)
│   │   └── test_fastapi_calculator.py # (5 tests)
│   └── e2e/
│       └── test_e2e.py             # (3 tests)
├── docker-compose.yml              # Local development setup
├── Dockerfile                      # Production container
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🔧 Local Setup & Installation

### **Prerequisites**
- Python 3.10 or higher
- Docker and Docker Compose
- Git

### **Step 1: Clone Repository**
```bash
git clone https://github.com/Pruthul15/assignment10.git
cd assignment10
```

### **Step 2: Create Virtual Environment**
```bash
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Start Docker Services**
```bash
docker-compose up -d
```

### **Step 5: Access Application**
- FastAPI Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- pgAdmin: http://localhost:5050

---

## 🧪 Running Tests Locally

### **Run All Tests**
```bash
pytest -v
```

### **Run Tests by Category**
```bash
# Unit tests only
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# End-to-end tests
pytest tests/e2e/ -v
```

### **Run Tests with Coverage Report**
```bash
pytest --cov=app --cov-report=html

# View the coverage report
open htmlcov/index.html  # macOS/Linux
start htmlcov/index.html # Windows
```

### **Run Specific Test File**
```bash
pytest tests/unit/test_security.py -v
pytest tests/integration/test_user.py -v
```

---

## 📊 Test Results

| Metric | Value |
|--------|-------|
| **Total Tests** | 43 ✅ |
| **Code Coverage** | 93% |
| **Unit Tests** | 30 |
| **Integration Tests** | 10 |
| **E2E Tests** | 3 |
| **Status** | All Passing 🎉 |

### **Test Breakdown**

**Unit Tests:**
- `test_security.py` - Password hashing, salt generation, verification
- `test_schemas.py` - Email validation, password strength, serialization
- `test_calculator.py` - Calculation logic, error handling

**Integration Tests:**
- `test_user.py` - User creation, uniqueness constraints, database operations
- `test_fastapi_calculator.py` - API endpoints, request/response validation

**E2E Tests:**
- `test_e2e.py` - Browser automation, full user workflows

---

## 🔐 Security Features

### **Password Hashing**
- Uses bcrypt algorithm with automatically generated salts
- Each password gets a unique hash even if passwords are identical
- One-way hashing (cannot reverse-engineer original password)
- Database stores only the hash, never plain text

### **Input Validation**
- Email format validation using Pydantic
- Password strength requirements:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit

### **Database Security**
- Password hashes stored instead of plaintext passwords
- Unique constraints prevent duplicate usernames/emails
- SQLAlchemy ORM prevents SQL injection attacks

---

## 📚 Technologies Used

- **FastAPI** - Modern web framework
- **SQLAlchemy** - Python ORM for database operations
- **PostgreSQL** - Relational database
- **Pydantic** - Data validation and serialization
- **Bcrypt** - Password hashing library
- **Pytest** - Testing framework
- **Docker** - Containerization
- **GitHub Actions** - CI/CD automation

---

## 🐳 Docker Hub Repository

**Repository:** https://hub.docker.com/r/pruthul123/assignment10

**Latest Image:** `pruthul123/assignment10:latest`

### **Pull Image**
```bash
docker pull pruthul123/assignment10:latest
```

### **Run Container**
```bash
docker run -p 8000:8000 pruthul123/assignment10:latest
```

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:
1. **Tests** - Runs all 43 tests
2. **Security Scan** - Scans for vulnerabilities with Trivy
3. **Build** - Builds Docker image
4. **Deploy** - Pushes image to Docker Hub

Every push to GitHub triggers this pipeline. The deployment only happens if all tests pass.

---

## 🚨 Common Issues & Solutions

### **Docker Services Won't Start**
```bash
# Check if ports are already in use
lsof -i :5432  # PostgreSQL
lsof -i :8000  # FastAPI

# Stop all containers
docker-compose down

# Start again
docker-compose up -d
```

### **Tests Fail with Database Connection Error**
```bash
# Make sure containers are running
docker-compose ps

# If not running, start them
docker-compose up -d

# Wait for PostgreSQL to be healthy
docker-compose logs postgres_db
```

### **Can't Access FastAPI Docs**
```bash
# Check if FastAPI container is running
docker-compose logs fastapi_calculator

# Check if port 8000 is accessible
curl http://localhost:8000/docs
```

---

## 🔗 Links

- **GitHub Repository:** https://github.com/Pruthul15/assignment10
- **Docker Hub Repository:** https://hub.docker.com/r/pruthul123/assignment10
- **Course:** IS601.855 - Python for Web API Development
- **Institution:** New Jersey Institute of Technology

---

## 👤 Author

**Pruthul Patel**
- GitHub: [@Pruthul15](https://github.com/Pruthul15)
- Docker Hub: [pruthul123](https://hub.docker.com/u/pruthul123)
