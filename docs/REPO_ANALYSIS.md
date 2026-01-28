# Repository Analysis: UNI-MANAGER-

## 1. Project Overview
**Name:** UNI-MANAGER (UniManager V6 Candidate)
**Purpose:** Comprehensive University Management System
**Current Status:** ~35% Complete (MVP Phase)
**Documentation Quality:** Excellent (Contains `BRUTAL_HONEST_DOCUMENTATION.md`)

## 2. Technology Stack

### Backend
- **Framework:** FastAPI 0.110.1 (Python 3.11+)
- **Database:** MongoDB (via Motor Async Driver)
- **Auth:** Google OAuth (Emergent), JWT (Python-Jose)
- **Validation:** Pydantic
- **Deployment:** Uvicorn, Nginx, Supervisor

### Frontend
- **Framework:** React 19.0.0
- **Routing:** React Router v7
- **Styling:** Tailwind CSS 3.4
- **UI Lib:** Shadcn UI + Lucide React
- **State/API:** Axios, Custom Hooks (No global state manager seen yet)

## 3. Current Implementation Status

### ✅ Functioning Features
- **Authentication:** Google OAuth, Session Management (Cookies/JWT).
- **User Management:** create, read, update roles.
- **Role-Based Access Control:** 9 distinct roles supported.
- **Basic CRUD:** Notices, Complaints, Courses, Subjects, Exams, Hostel Rooms, Library Books.

### ⚠️ Functional Issues (Tech Debt)
- **Student Profile:** Created but not linked to User Accounts (Data silo).
- **Faculty Profile:** Created but not linked to Subjects/Classes.
- **Mock Data:** Student Dashboard, Attendance, Marks, Fees rely on hardcoded/fake data.
- **Missing Linkages:** No `enrollment` table linking Students <-> Classes <-> Subjects.

### ❌ Critical Missing Features
1. **Class/Section Management:** No entity to group students.
2. **Student-User Bridge:** Critical architecture flaw preventing students from seeing their own real data.
3. **Email/Password Auth:** Only Google OAuth is implemented.
4. **File Uploads:** Firebase Configured but logic missing.
5. **Real Data Flow:** Attendance and Marks modules are UI shells without backend logic.

## 4. Architecture observations
- **Monorepo:** `backend/` and `frontend/` in root.
- **API Design:** RESTful, but some endpoints return mock data.
- **Database Schema:** NoSQL (MongoDB). Collections defined but critical relational mapping (linking collections) is weak/missing.

## 5. Security & Code Quality
- **Auth:** Relying on 'Emergent' managed OAuth. JWT handling seems standard.
- **Secrets:** Uses `.env`.
- **Validation:** Pydantic used in backend (Good).
- **Testing:** `tests/` folder exists but low coverage indicated.

## 6. Recommendations
If integrating this into the current project:
1. **Fix Data Modeling:** Prioritize creating the `Enrollments` and `ClassSchedule` collections.
2. **Bridge Identity:** Implement the link between `User` (Auth) and `Student` (Profile) collections.
3. **Implement Logic:** Replace the mock endpoints in `server.py` with real DB queries.
4. **Frontend Cleanup:** Remove hardcoded values in `StudentDashboard.jsx`.
