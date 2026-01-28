# Implementation Plan: V0.1 Deployment Candidate

## Goal
Build a deployable "Skeleton v0.1" hosted on Vercel (Frontend), Render (Backend), and Neon (Postgres), authenticated via Clerk.

## Scope
1.  **Database (Neon)**: Initialize Alembic, generate migrations for `User` table.
2.  **Backend (Render)**: Add `Dockerfile` and `render.yaml`. Ensure production server (`gunicorn`) is ready.
3.  **Frontend (Vercel)**: Ensure `package.json` build scripts are correct.
4.  **Verification**: Local "dry run" of the build process.

## Architecture & Steps

### 1. Database & Schema (Database Architect)
- **Action**: Run `alembic init alembic`.
- **Config**: Update `alembic.ini` and `env.py` to use `DATABASE_URL` from environment.
- **Migration**: Generate `001_initial_schema` for `User` model.

### 2. Backend Deployment Config (DevOps Engineer)
- **Action**: Create `backend/Dockerfile` using Python 3.11.
- **Action**: Create `render.yaml` for Blueprint deployment (optional, or just Dockerfile).
- **Dependency**: Add `gunicorn` to `requirements.txt`.
- **Entrypoint**: Create `start.sh` or generic command `gunicorn app.main:app -k uvicorn.workers.UvicornWorker`.

### 3. Frontend Deployment Config (Frontend Specialist)
- **Check**: Verify `vite build` output includes `dist`.
- **Config**: Create `vercel.json` (optional, usually Vercel auto-detects Vite).

## Execution Agents
- `database-architect`: Migrations.
- `devops-engineer`: Docker/Render config.
- `backend-specialist`: Gunicorn setup.

## Verification
- [ ] `docker build` succeeds for backend.
- [ ] `npm run build` succeeds for frontend.
- [ ] Alembic can generate a migration file locally.
