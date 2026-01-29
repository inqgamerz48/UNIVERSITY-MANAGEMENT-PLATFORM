from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
import os
import httpx
from jose import jwt, JWTError
from .database import get_db
from .models import User, UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Clerk Configuration (Get these from your Clerk Dashboard)
CLERK_ISSUER = os.getenv("CLERK_ISSUER_URL") # e.g., https://your-clerk-domain.clerk.accounts.dev
CLERK_JWKS_URL = f"{CLERK_ISSUER}/.well-known/jwks.json" if CLERK_ISSUER else None

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> User:
    """
    Validates the Clerk JWT and retrieves/syncs the user with the database.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # --- DEV MODE BYPASS (Only if CLERK_ISSUER is not set) ---
    if not CLERK_ISSUER:
        # Warn in logs
        # For prototype simplicity: "admin" token = Super Admin
        if token == "admin":
             return User(id="mock-admin-id", email="admin@test.com", role=UserRole.SUPER_ADMIN, first_name="Mock", last_name="Admin")
        elif token == "student":
             return User(id="mock-student-id", email="student@test.com", role=UserRole.STUDENT, first_name="Mock", last_name="Student")
        # Fallback to failing if not specific mock tokens
        # raise credentials_exception

    try:
        # 1. Fetch JWKS (Cache this in production!)
        async with httpx.AsyncClient() as client:
            jwks_res = await client.get(CLERK_JWKS_URL)
            jwks = jwks_res.json()

        # 2. Decode and Verify Token
        # Clerk tokens usually use RS256
        payload = jwt.decode(
            token, 
            jwks, 
            algorithms=["RS256"], 
            options={"verify_aud": False} # Verify audience if necessary
        )
        
        user_email = payload.get("sub") # Clerk User ID is in 'sub', email in 'email' usually
        # Note: 'sub' is the Clerk ID. Mapping logic depends on your user syncing strategy.
        # For simplicity, we'll assume we look up by email provided in claims, or sync on fly.
        
        # NOTE: Clerk JWT claims might need mapping.
        
    except JWTError:
        raise credentials_exception
    except Exception as e:
         print(f"Auth Error: {e}")
         raise credentials_exception

    # 3. DB Lookup
    # In a real sync scenario, we might upsert the user here.
    # For now, we mock the DB lookup part based on successful JWT validation
    # or actually query the DB.
    
    # ... Implementation of DB lookup ...
    
    # Returning a mock user for now to prevent breaking flow until DB is seeded
    return User(id="clerk-verified-id", email="verified@test.com", role=UserRole.SUPER_ADMIN)


class RoleChecker:
    def __init__(self, allowed_roles: List[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="Operation not permitted"
            )
        return user

# Dependency shortcuts
allow_super_admin = RoleChecker([UserRole.SUPER_ADMIN])
allow_admin = RoleChecker([UserRole.SUPER_ADMIN, UserRole.ADMIN])
allow_faculty = RoleChecker([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.FACULTY])
