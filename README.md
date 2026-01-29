# UNIManager v2

University Management System Monorepo.

## Structure
- `apps/api`: FastAPI Backend (Python)
- `apps/web`: Next.js Frontend (TypeScript)

## Getting Started

### Backend (apps/api)
```bash
cd apps/api
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (apps/web)
```bash
cd apps/web
npm install
npm run dev
```

## Documentation
- [Implementation Plan](docs/PLAN.md)
- [Database Design](docs/DATABASE_DESIGN.md)
