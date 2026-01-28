# Implementation Plan: Clerk RBAC "Identity Bridge"

## Goal
Implement a robust Role-Based Access Control (RBAC) system using Clerk for authentication and a local PostgreSQL database for authorization and user data, solving the "Data Silo" problem.

## Architecture: "The Identity Bridge"
We will separate **Authentication** (Clerk) from **Authorization & Data** (Local DB).
1.  **Identity Provider (IDP):** Clerk handles cleanup, login, MFA, and session tokens.
2.  **Service Provider (SP):** Our Backend Database holds the user's Role (`student`, `faculty`) and links them to their specific profile data.
3.  **The Bridge:** A `users` table in Postgres that stores the `clerk_id` and maps it to a `role`.

## Proposed Changes

### 1. Database Schema (Database Architect)
#### [NEW] `backend/app/models/user.py`
Create a `User` model:
- `id`: UUID (Primary Key)
- `clerk_id`: String (Indexed, Unique) - The bridge to Clerk
- `email`: String
- `role`: Enum (student, faculty, admin, etc.)
- `is_active`: Boolean
- `created_at`: DateTime

### 2. Backend Logic (Backend Specialist)
#### [NEW] `backend/app/api/v1/endpoints/webhooks.py`
- Endpoint to receive Clerk `user.created` events.
- **Logic:** When a user signs up in Clerk -> Create entry in our `users` table.

#### [NEW] `backend/app/core/auth_dependencies.py`
- `get_current_user` dependency.
- **Logic:**
    1. Verify Clerk JWT.
    2. Extract `clerk_id`.
    3. Query local DB for `User` using `clerk_id`.
    4. Return merged object (User Data + Role).

### 3. Verification (Test Engineer)
- **Script:** `tests/test_clerk_webhook.py` - Simulate a Clerk webhook payload to verify DB insertion.
- **Script:** `tests/test_rbac_protection.py` - Mock a request with a specific role to test endpoint protection.

## Orchestration Steps (Phase 2)
1.  **`database-architect`**: Define SQLAlchemy models and generate Alembic migrations.
2.  **`backend-specialist`**: Implement Webhook logic and Auth Dependency.
3.  **`security-auditor`**: Review the security of the webhook (Signature verification).
4.  **`test-engineer`**: Write and run verification scripts.

## Verification Plan
- [ ] `alembic upgrade head` runs successfully.
- [ ] Mock Webhook creates a user in local DB.
- [ ] Protected endpoint denies access to user without correct role.
