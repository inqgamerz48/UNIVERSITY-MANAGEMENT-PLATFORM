# UNIVERSITY-MANAGEMENT-PLATFORM (v0.1 Skeleton)

A comprehensive University Management System built with a modern stack, designed to bridge the gap between Authentication and Authorization using an "Identity Bridge" architecture.

## 🚀 Status: v0.1 Deployment Candidate

This repository contains the **Foundation Skeleton** required to deploy the application on a production stack.

- **Frontend**: React + Vite + Clerk (Ready for Vercel)
- **Backend**: FastAPI + SQLAlchemy (Async) + Clerk Webhooks (Ready for Render)
- **Database**: PostgreSQL (Ready for Neon)

## 🛠️ Tech Stack

- **Frontend**: React 18, TailwindCSS, Shadcn UI, Clerk Auth, Axios.
- **Backend**: Python 3.11, FastAPI, AsyncPG, Alembic, Pydantic.
- **Infrastructure**: Docker, Gunicorn, Uvicorn.

## 📂 Project Structure

```
/
├── backend/            # FastAPI Application
│   ├── app/
│   │   ├── models/     # SQLAlchemy Models (User)
│   │   ├── api/        # Endpoints (Webhooks)
│   │   └── core/       # Config & Auth Dependencies
│   ├── alembic/        # Database Migrations
│   └── Dockerfile      # Render Deployment Config
│
├── frontend/           # React Application
│   ├── src/
│   │   ├── components/ # ProtectedRoute (RBAC)
│   │   └── App.jsx     # Routing Logic
│   └── vercel.json     # (Optional) Vercel Config
│
└── docs/               # Project Documentation
    ├── DEPLOYMENT_GUIDE.md
    └── ORCHESTRATION_REPORT.md
```

## ⚡ Quick Start (Local)

### Prerequisites
1.  **Clerk Account**: Get `PUBLISHABLE_KEY` and `SECRET_KEY`.
2.  **PostgreSQL**: Local URL or Neon URL.

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Set ENV Variables: DATABASE_URL, CLERK_WEBHOOK_SECRET
alembic upgrade head
uvicorn app.main:app --reload
```

### 2. Frontend Setup
```bash
cd frontend
npm install
# Set ENV Variable: VITE_CLERK_PUBLISHABLE_KEY
npm run dev
```

## 🚢 Deployment

Detailed instructions are available in [`docs/DEPLOYMENT_GUIDE.md`](./docs/DEPLOYMENT_GUIDE.md).

### Summary:
1.  **Database**: Create Neon Project -> Get Connection String.
2.  **Backend**: create Web Service on Render -> Link Repo -> Set Envs.
3.  **Frontend**: Import Repo on Vercel -> Set Envs -> Deploy.

## 🤝 Contribution

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
