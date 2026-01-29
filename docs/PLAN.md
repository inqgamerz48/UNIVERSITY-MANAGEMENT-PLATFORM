# UNIManager Rebuild Plan

## 1. Overview
Rebuild of the "UNIManager" University Management System based on the `v3` blueprint provided in `unimanager-export-1769619449603.json`.
The system is a production-grade web application for managing students, faculty, attendance, and marks with strict RBAC.

## 2. Project Type
**WEB** (Full Stack)

## 3. Success Criteria
- [x] Monorepo structure established (`apps/web`, `apps/api`).
- [ ] Backend: FastAPI running with Async SQLAlchemy and Postgres.
- [ ] Frontend: Next.js running with Clerk Authentication & RBAC.
- [ ] Database: Schema migrated via Alembic matching the JSON blueprint.
- [ ] Key User Flows: Admin Dashboard, Faculty Attendance Upload, Student Report View.

## 4. Tech Stack
-   **Backend**: Python 3.10+, FastAPI (Async), SQLAlchemy 2.0 (Async), Alembic, Pydantic.
-   **Frontend**: Next.js 14+ (App Router), React, TailwindCSS, Clerk (Auth).
-   **Database**: PostgreSQL 15+.
-   **Infrastructure**: Docker (optional/future), Monorepo structure.

## 5. File Structure
```
.
├── apps
│   ├── api          # FastAPI Backend
│   └── web          # Next.js Frontend
├── packages         # Shared config (optional)
├── docker-compose.yml
└── README.md
```

## 6. Task Breakdown

### Phase 1: Foundation (Database & Repo)
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **F-01** | Initialize Monorepo | `devops-engineer` | `bash-linux` | P0 (Done) |
| **F-02** | Database Schema Design (ERD) | `database-architect` | `database-design` | P0 (Done) |
| **F-03** | FastAPI Setup + Alembic Init | `backend-specialist` | `python-patterns` | P0 (Done) |
| **F-04** | Next.js Setup + Tailwind | `frontend-specialist` | `nextjs-react-expert` | P1 (Done) |

### Phase 2: Core Backend (Auth & Users)
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **B-01** | Implement RBAC Middleware | `backend-specialist` | `api-patterns` | P0 |
| **B-02** | User Management API (Sync with Clerk) | `backend-specialist` | `api-patterns` | P1 (Done) |
| **B-03** | Academic Models (College/Dept/Course) | `backend-specialist` | `database-design` | P1 (Done) |

### Phase 3: Core Frontend (UI & Dashboards)
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **W-01** | Clerk Integration + Protected Routes | `frontend-specialist` | `nextjs-react-expert` | P0 |
| **W-02** | App Layout (Sidebar, Navbar) | `frontend-specialist` | `frontend-design` | P1 (Partial) |
| **W-03** | Admin Dashboard Components | `frontend-specialist` | `frontend-design` | P2 (Done) |
| **W-04** | API Client Integration | `frontend-specialist` | `nextjs-react-expert` | P1 |
| **W-05** | Faculty Dashboard (Attendance) | `frontend-specialist` | `frontend-design` | P1 |
| **W-06** | Student Dashboard (Marks/Reports) | `frontend-specialist` | `frontend-design` | P1 |

### Phase 4: Advanced Backend
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **A-01** | GPA Calculation Logic | `backend-specialist` | `python-patterns` | P1 |
| **A-02** | PDF Report Generation (Hall Tickets/Results) | `backend-specialist` | `python-patterns` | P1 |

### Phase 5: Verification
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **V-01** | API Integration Tests | `test-engineer` | `testing-patterns` | P1 |
### Phase 6: Production Hardening (Option B)
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **H-01** | Real Clerk Authentication (JWT Validation) | `backend-specialist` | `api-patterns` | P0 |
### Phase 7: Deployment (Dockerization)
| Task ID | Name | Agent | Skills | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **D-01** | Create Backend Dockerfile | `devops-engineer` | `server-management` | P0 |
| **D-02** | Create Frontend Dockerfile | `devops-engineer` | `server-management` | P0 |
| **D-03** | Create Production Compose File | `devops-engineer` | `deployment-procedures` | P0 |

## 7. Phase X: Verification Checklist
- [ ] **Lint**: `npm run lint` & `flake8` pass.
- [ ] **Security**: `security_scan.py` passes (no high vulnerabilities).
- [ ] **Build**: `npm run build` succeeds (web).
- [ ] **Runtime**: `docker-compose up` starts all services without errors.
