from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from database import get_db
from models import Enrollment, Attendance, Mark, AttendanceStatus, User, Subject
from dependencies import allow_faculty, allow_admin, get_current_user

router = APIRouter(
    prefix="/operations",
    tags=["operations"],
    responses={404: {"description": "Not found"}},
)

@router.post("/enroll", dependencies=[Depends(allow_admin)])
async def enroll_student(student_id: str, subject_id: str, academic_year: str, db: AsyncSession = Depends(get_db)):
    """Enroll a student in a subject."""
    # Check if exists
    existing = await db.execute(select(Enrollment).where(
        Enrollment.student_id == student_id,
        Enrollment.subject_id == subject_id
    ))
    if existing.scalars().first():
        raise HTTPException(status_code=400, detail="Already enrolled")

    enrollment = Enrollment(student_id=student_id, subject_id=subject_id, academic_year=academic_year)
    db.add(enrollment)
    await db.commit()
    await db.refresh(enrollment)
    return enrollment

@router.post("/attendance/bulk", dependencies=[Depends(allow_faculty)])
async def mark_bulk_attendance(
    subject_id: str, 
    date: str, 
    records: List[dict] = Body(...), # List of {student_id: str, status: AttendanceStatus}
    db: AsyncSession = Depends(get_db)
):
    """Mark attendance for multiple students in a subject."""
    # Ideally verify that the current faculty teaches this subject
    # For now, just iterate and create records
    
    created_records = []
    
    for rec in records:
        # Find enrollment
        result = await db.execute(select(Enrollment).where(
            Enrollment.student_id == rec['student_id'],
            Enrollment.subject_id == subject_id
        ))
        enrollment = result.scalars().first()
        
        if not enrollment:
            continue # Skip invalid enrollments
            
        att = Attendance(
            enrollment_id=enrollment.id,
            date=date,
            status=rec['status']
        )
        db.add(att)
        created_records.append(att)
        
    await db.commit()
    return {"message": "Attendance marked", "count": len(created_records)}

@router.post("/marks", dependencies=[Depends(allow_faculty)])
async def upload_marks(
    student_id: str,
    subject_id: str,
    exam_type: str,
    score: int,
    max_score: int,
    db: AsyncSession = Depends(get_db)
):
    """Upload marks for a student."""
    # Find enrollment
    result = await db.execute(select(Enrollment).where(
        Enrollment.student_id == student_id,
        Enrollment.subject_id == subject_id
    ))
    enrollment = result.scalars().first()
    
    if not enrollment:
        raise HTTPException(status_code=404, detail="Student not enrolled in this subject")
        
    mark = Mark(
        enrollment_id=enrollment.id,
        exam_type=exam_type,
        score=score,
        max_score=max_score
    )
    db.add(mark)
    await db.commit()
    return mark
