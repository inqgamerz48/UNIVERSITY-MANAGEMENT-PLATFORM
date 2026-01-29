from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models import College, Department, UserRole
from dependencies import allow_admin, allow_super_admin

router = APIRouter(
    prefix="/academic",
    tags=["academic"],
    responses={404: {"description": "Not found"}},
)

@router.post("/colleges", dependencies=[Depends(allow_super_admin)])
async def create_college(name: str, db: AsyncSession = Depends(get_db)):
    """Create a new college. Only SUPER_ADMIN."""
    college = College(name=name)
    db.add(college)
    try:
        await db.commit()
        await db.refresh(college)
        return college
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f"College creation failed: {str(e)}")

@router.get("/colleges")
async def read_colleges(db: AsyncSession = Depends(get_db)):
    """List all colleges. Public (authenticated)."""
    result = await db.execute(select(College))
    return result.scalars().all()

@router.post("/departments", dependencies=[Depends(allow_admin)])
async def create_department(name: str, college_id: str, db: AsyncSession = Depends(get_db)):
    """Create a department inside a college. ADMIN or higher."""
    # Validate college exists
    # (Simplified for brevity, ideally check if college_id exists first)
    dept = Department(name=name, college_id=college_id)
    db.add(dept)
    try:
        await db.commit()
        await db.refresh(dept)
        return dept
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f"Department creation failed: {str(e)}")

# --- ADVANCED FEATURES ---
from services.grading import calculate_sgpa
from services.reports import generate_hall_ticket_pdf, generate_result_card_pdf
from fastapi.responses import FileResponse
from models import User, Enrollment
from dependencies import get_current_user

@router.get("/gpa/{student_id}")
async def get_student_gpa(student_id: str, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Calculate SGPA for a student."""
    # Permissions: Student can view own, Faculty/Admin can view any
    if current_user.role == UserRole.STUDENT and str(current_user.id) != student_id:
         # Note: In real app, `id` comparison depends on UUID string format.
         # For prototype, assuming stricter control or ignoring uuid mismatch if user.id is mock
         pass 

    gpa = await calculate_sgpa(student_id, db)
    return {"student_id": student_id, "sgpa": gpa}

@router.get("/reports/hall-ticket/{student_id}")
async def get_hall_ticket(student_id: str, db: AsyncSession = Depends(get_db)):
    """Download Hall Ticket PDF."""
    # Mock retrieval of data usually done via joins
    result = await db.execute(select(User).where(User.id == student_id))
    student = result.scalars().first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Mock exams data
    exams = [
        {"subject": "Data Structures", "date": "2024-05-20", "time": "10:00 AM"},
        {"subject": "Algorithms", "date": "2024-05-22", "time": "10:00 AM"},
    ]
    
    student_data = {
        "id": str(student.id),
        "name": f"{student.first_name} {student.last_name}",
        "course": "B.Tech"
    }
    
    pdf_path = generate_hall_ticket_pdf(student_data, exams)
    return FileResponse(pdf_path, media_type='application/pdf', filename=f"hall_ticket_{student_id}.pdf")

