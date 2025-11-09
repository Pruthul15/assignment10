# Assignment 10: Secure User Authentication with SQLAlchemy & JWT

📋 **Project Overview**

This project implements a secure user authentication system using FastAPI, SQLAlchemy, and bcrypt password hashing with JWT token generation. It demonstrates core web security practices including password hashing, database modeling with ORM, input validation with Pydantic schemas, and a complete CI/CD pipeline with GitHub Actions and Docker Hub deployment.

**Status:** ✅ **COMPLETE** - 43 Tests Passing | 75% Code Coverage | Docker Deployed

---

## 🚀 What We Built

### 1. Secure User Model (SQLAlchemy)
- SQLAlchemy ORM model with UUID primary key
- Unique constraints on username and email
- `password_hash` field (never stores plain passwords)
- Timestamp tracking with `created_at`
- Methods: `set_password()` and `verify_password()` using bcrypt

### 2. JWT Authentication System
- `/api/auth/register` endpoint for user registration
- `/api/auth/login` endpoint with JWT token response
- JWT tokens with 30-minute expiration
- Secure token validation and decoding

### 3. Data Validation (Pydantic)
- `UserCreate` schema for registration with validation
- `UserRead` schema for API responses (excludes password_hash)
- `UserLogin` schema for login credentials
- `TokenResponse` schema for JWT responses
- Email format validation
- Password strength requirements (8+ chars minimum)

### 4. Password Security (Bcrypt)
- One-way password hashing with automatic salt generation
- Unique hash for each password (even if passwords are identical)
- Cannot reverse-engineer original password from hash
- Industry standard for secure password storage

### 5. Comprehensive Testing
- **43 total tests passing** ✅
- **Unit tests (30)** - Password hashing, schemas, calculator logic
- **Integration tests (10)** - Database operations, API endpoints, constraints
- **E2E tests (3)** - End-to-end browser automation
- **75% code coverage** achieved

### 6. CI/CD Pipeline
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
│   │   ├── __init__.py             # Export User model
│   │   └── user.py                 # SQLAlchemy User model with password hashing
│   ├── routers/
│   │   ├── __init__.py
│   │   └── auth.py                 # /register and /login endpoints
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── base.py                 # Base Pydantic schemas
│   │   └── user.py                 # UserCreate, UserRead, UserLogin, TokenResponse
│   ├── utils/
│   │   ├── __init__.py
│   │   └── security.py             # Password hashing & JWT functions
│   ├── operations/
│   │   └── __init__.py             # Calculator operations
│   ├── __init__.py
│   ├── config.py                   # Configuration & database URL
│   └── database.py                 # Database connection & session management
├── tests/
│   ├── conftest.py                 # Pytest fixtures
│   ├── unit/
│   │   ├── test_security.py        # (4 tests) Password hashing
│   │   ├── test_schemas.py         # (5 tests) Schema validation
│   │   └── test_calculator.py      # (21 tests) Calculator logic
│   ├── integration/
│   │   ├── test_user.py            # (5 tests) User CRUD operations
│   │   └── test_fastapi_calculator.py # (5 tests) API endpoints
│   └── e2e/
│       └── test_e2e.py             # (3 tests) Browser automation
├── templates/
│   └── index.html                  # Frontend calculator UI
├── main.py                         # FastAPI application entry point
├── docker-compose.yml              # Local development setup
├── Dockerfile                      # Production container
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configuration
└── README.md                       # This file
```

---

## 🔧 Local Setup & Installation

### Prerequisites
- Python 3.10 or higher
- Docker and Docker Compose
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/Pruthul15/assignment10.git
cd assignment10
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Start Docker Services
```bash
docker-compose up -d
```

### Step 5: Access Application
- **FastAPI Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **pgAdmin:** http://localhost:5050
- **Calculator:** http://localhost:8000/

---

## 🧪 Running Tests Locally

### Run All Tests
```bash
pytest -v
```

### Run Tests by Category
```bash
# Unit tests only
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# End-to-end tests
pytest tests/e2e/ -v
```

### Run Tests with Coverage Report
```bash
pytest --cov=app --cov-report=html

# View the coverage report
open htmlcov/index.html  # macOS/Linux
start htmlcov/index.html # Windows
```

### Run Specific Test File
```bash
pytest tests/unit/test_security.py -v
pytest tests/integration/test_user.py -v
```

---

## 📊 Test Results

| Metric | Value |
|--------|-------|
| **Total Tests** | 43 ✅ |
| **Code Coverage** | 75% |
| **Unit Tests** | 30 |
| **Integration Tests** | 10 |
| **E2E Tests** | 3 |
| **Status** | All Passing 🎉 |

### Test Breakdown
- **test_security.py** - Password hashing, salt generation, verification (4 tests)
- **test_schemas.py** - Email validation, serialization (5 tests)
- **test_calculator.py** - Calculation logic, error handling (21 tests)
- **test_user.py** - User creation, uniqueness constraints (5 tests)
- **test_fastapi_calculator.py** - API endpoints, validation (5 tests)
- **test_e2e.py** - Browser automation, workflows (3 tests)

---

## 🔐 Security Features

### Password Hashing
- Uses bcrypt algorithm with automatically generated salts
- Each password gets a unique hash even if passwords are identical
- One-way hashing (cannot reverse-engineer original password)
- Database stores only the hash, never plain text

### Input Validation
- Email format validation using Pydantic
- Password strength requirements (minimum 8 characters)
- Username and email uniqueness constraints
- SQL injection prevention via SQLAlchemy ORM

### JWT Token Authentication
- Secure token generation with HS256 algorithm
- 30-minute token expiration
- User ID stored in token subject claim
- Token validation on protected endpoints

### Database Security
- Password hashes stored instead of plaintext passwords
- Unique constraints prevent duplicate usernames/emails
- SQLAlchemy ORM prevents SQL injection attacks
- UUID primary keys instead of sequential IDs

---

## 🌐 API Endpoints

### Authentication Endpoints

**Register New User**
```bash
POST /api/auth/register
Content-Type: application/json

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "SecurePass123"
}

Response (201):
{
  "id": "d57ed209-05df-4f91-b584-2d9454ce3b2f",
  "username": "testuser",
  "email": "test@example.com",
  "created_at": "2025-11-09T02:43:31.226926"
}
```

**Login User**
```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "SecurePass123"
}

Response (200):
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "d57ed209-05df-4f91-b584-2d9454ce3b2f",
    "username": "testuser",
    "email": "test@example.com",
    "created_at": "2025-11-09T02:43:31.226926"
  }
}
```

### Calculator Endpoints

**Add**
```bash
POST /add
Content-Type: application/json

{
  "a": 10,
  "b": 5
}

Response:
{
  "result": 15.0
}
```

**Subtract, Multiply, Divide** - Same pattern as Add

---

## 📚 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Modern web framework with async support |
| **SQLAlchemy** | Python ORM for database operations |
| **PostgreSQL** | Relational database |
| **Pydantic** | Data validation and serialization |
| **Bcrypt** | Password hashing library |
| **PyJWT** | JWT token generation and validation |
| **Pytest** | Testing framework with coverage |
| **Docker** | Containerization |
| **GitHub Actions** | CI/CD automation |
| **Trivy** | Container security scanning |

---

## 🐳 Docker Hub Repository

**Repository:** https://hub.docker.com/r/pruthul123/assignment10

**Latest Image:** `pruthul123/assignment10:latest`

### Pull Image
```bash
docker pull pruthul123/assignment10:latest
```

### Run Container
```bash
docker run -p 8000:8000 pruthul123/assignment10:latest
```

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Tests** - Runs all 43 tests with pytest
2. **Security Scan** - Scans Docker image for vulnerabilities with Trivy
3. **Build** - Builds Docker image from Dockerfile
4. **Deploy** - Pushes image to Docker Hub

Every push to GitHub triggers this pipeline. Deployment only happens if all tests pass.

---

## 🚨 Common Issues & Solutions

### Docker Services Won't Start
```bash
# Check if ports are already in use
lsof -i :5432  # PostgreSQL
lsof -i :8000  # FastAPI

# Stop all containers
docker-compose down

# Start again
docker-compose up -d
```

### Tests Fail with Database Connection Error
```bash
# Make sure containers are running
docker-compose ps

# If not running, start them
docker-compose up -d

# Wait for PostgreSQL to be healthy
docker-compose logs postgres_db
```

### Can't Access FastAPI Docs
```bash
# Check if FastAPI container is running
docker-compose logs fastapi_calculator

# Check if port 8000 is accessible
curl http://localhost:8000/docs
```

### Password Authentication Failed
Ensure `app/config.py` DATABASE_URL matches docker-compose PostgreSQL credentials:
```python
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
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

- **GitHub:** [@Pruthul15](https://github.com/Pruthul15)
- **Docker Hub:** [pruthul123](https://hub.docker.com/u/pruthul123)
- **Email:** pp8787140@gmail.com

---


