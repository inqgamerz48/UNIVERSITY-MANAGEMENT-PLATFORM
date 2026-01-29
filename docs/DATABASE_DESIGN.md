# Database Design - UNIManager

Based on the blueprints from `unimanager-export-1769619449603.json`.

## Overview
- **Database**: PostgreSQL 15+
- **ORM**: SQLAlchemy 2.0 (Async)
- **Migration**: Alembic

## ERD / Schema Definitions

### 1. User Management (Synced with Clerk)
| Table | Column | Type | Notes |
| :--- | :--- | :--- | :--- |
| `users` | `id` | UUID (PK) | Clerk User ID |
| | `email` | String | Unique, Indexed |
| | `first_name` | String | |
| | `last_name` | String | |
| | `role` | Enum | `SUPER_ADMIN`, `ADMIN`, `FACULTY`, `STUDENT` |
| | `is_active` | Boolean | Default True |
| | `created_at` | DateTime | |

### 2. Academic Structure
| Table | Column | Type | Notes |
| :--- | :--- | :--- | :--- |
| `colleges` | `id` | UUID (PK) | |
| | `name` | String | e.g., "College of Engineering" |
| | `created_at` | DateTime | |
| `departments` | `id` | UUID (PK) | |
| | `name` | String | e.g., "Computer Science" |
| | `college_id` | UUID (FK) | Ref `colleges.id` |
| | `head_of_dept_id`| UUID (FK) | Ref `users.id` (Optional) |

### 3. Curriculum
| Table | Column | Type | Notes |
| :--- | :--- | :--- | :--- |
| `courses` | `id` | UUID (PK) | e.g., "B.Tech CSE" |
| | `name` | String | |
| | `department_id` | UUID (FK) | Ref `departments.id` |
| `semesters` | `id` | UUID (PK) | |
| | `name` | String | e.g., "Fall 2025" or "Semester 1" |
| | `course_id` | UUID (FK) | Ref `courses.id` |
| `subjects` | `id` | UUID (PK) | |
| | `name` | String | e.g., "Data Structures" |
| | `code` | String | e.g., "CS101" |
| | `semester_id` | UUID (FK) | Ref `semesters.id` |
| | `credits` | Integer | |

### 4. Enrollments & Assignments
| Table | Column | Type | Notes |
| :--- | :--- | :--- | :--- |
| `student_profiles`| `id` | UUID (PK) | Ref `users.id` (1:1) |
| | `enrollment_no`| String | Unique |
| | `course_id` | UUID (FK) | Ref `courses.id` |
| | `current_sem_id`| UUID (FK) | Ref `semesters.id` |
| `faculty_profiles`| `id` | UUID (PK) | Ref `users.id` (1:1) |
| | `department_id` | UUID (FK) | Ref `departments.id` |
| `subject_assignments` | `id` | UUID (PK) | Faculty -> Subject mapping |
| | `faculty_id` | UUID (FK) | Ref `users.id` |
| | `subject_id` | UUID (FK) | Ref `subjects.id` |
| | `academic_year` | String | e.g., "2025-2026" |

### 5. Academic Records
| Table | Column | Type | Notes |
| :--- | :--- | :--- | :--- |
| `attendance` | `id` | UUID (PK) | |
| | `student_id` | UUID (FK) | Ref `users.id` |
| | `subject_id` | UUID (FK) | Ref `subjects.id` |
| | `date` | Date | Indexed |
| | `status` | Enum | `PRESENT`, `ABSENT`, `EXCUSED` |
| `marks` | `id` | UUID (PK) | |
| | `student_id` | UUID (FK) | Ref `users.id` |
| | `subject_id` | UUID (FK) | Ref `subjects.id` |
| | `exam_type` | Enum | `INTERNAL_1`, `INTERNAL_2`, `FINAL` |
| | `marks_obtained`| Float | |
| | `max_marks` | Float | |

## Indexes
- `users(email)`
- `attendance(student_id, subject_id, date)` - Composite for uniqueness/query
- `marks(student_id, subject_id, exam_type)` - Composite Unique
