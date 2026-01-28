# 🚀 Deployment Guide: UniManager v0.1

Success! The codebase is ready for deployment. Follow these steps to take it live.

## 1. Prerequisites (You have these keys)
- **Neon (PostgreSQL)**: You need the connection string (`postgresql+asyncpg://...`).
- **Clerk (Auth)**: You need `Publishable Key` and `Secret Key`.
- **Render (Backend)**: Account ready.
- **Vercel (Frontend)**: Account ready.

## 2. Backend Deployment (Render)

1.  **Push Code**: Push this entire repository to your GitHub.
2.  **New Web Service**: In Render dashboard, create new "Web Service".
3.  **Root Directory**: Set to `./backend`.
4.  **Environment**: `Python 3` (Render will detect `requirements.txt`).
5.  **Build Command**: `pip install -r requirements.txt` (Default is fine).
6.  **Start Command**: `gunicorn app.main:app -k uvicorn.workers.UvicornWorker`.
7.  **Environment Variables**:
    - `python_version`: `3.11.0`
    - `DATABASE_URL`: Your Neon Connection String (ensure it starts with `postgresql+asyncpg://`).
    - `CLERK_WEBHOOK_SECRET`: Your webhook secret.

### Database Migration
Once deployed, the app might crash because tables don't exist. You need to run migration.
- In Render Dashboard -> Shell / Terminal:
  ```bash
  alembic upgrade head
  ```

## 3. Frontend Deployment (Vercel)

1.  **New Project**: In Vercel, import your repository.
2.  **Root Directory**: Edit settings to point to `frontend`.
3.  **Framework Preset**: Select **Vite**.
4.  **Environment Variables**:
    - `VITE_CLERK_PUBLISHABLE_KEY`: Your Clerk Publishable Key (starts with `pk_...`).
5.  **Deploy**: Click Deploy.

## 4. Verification
1.  Open your Vercel URL.
2.  Sign Up with Clerk.
3.  Check Neon Console: You should see a new row in the `users` table!
