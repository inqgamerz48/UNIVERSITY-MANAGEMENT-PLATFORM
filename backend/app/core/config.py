from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "UNI Manager API"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/unimanager"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    # Clerk
    CLERK_JWKS_URL: str = "https://clerk.clerk.com/.well-known/jwks.json"
    CLERK_WEBHOOK_SECRET: str = "whsec_..." # Update with your Clerk Webhook Secret


    class Config:
        case_sensitive = True

settings = Settings()
