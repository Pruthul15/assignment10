# app/schemas/user.py
"""
Pydantic schemas for User validation and serialization.
"""
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
import uuid


class UserCreate(BaseModel):
    """Schema for creating a new user during registration."""
    username: str = Field(..., min_length=3, max_length=50, description="Username must be 3-50 characters")
    email: EmailStr = Field(..., description="Valid email address required")
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "password": "SecurePass123"
            }
        }


class UserRead(BaseModel):
    """Schema for returning user data (omits password_hash for security)."""
    id: uuid.UUID
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "username": "johndoe",
                "email": "john@example.com",
                "created_at": "2025-11-08T12:00:00"
            }
        }


class UserLogin(BaseModel):
    """Schema for user login request."""
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User password")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "SecurePass123"
            }
        }


class TokenResponse(BaseModel):
    """Schema for JWT token response."""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")
    user: UserRead = Field(..., description="User information")

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "user": {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "username": "johndoe",
                    "email": "john@example.com",
                    "created_at": "2025-11-08T12:00:00"
                }
            }
        }