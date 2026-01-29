from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Mark, Enrollment, Subject

def get_grade_point(score: int, max_score: int) -> float:
    """
    Convert raw score to grade point (10-point scale).
    Example: 90-100 -> 10, 80-89 -> 9, etc.
    """
    percentage = (score / max_score) * 100
    if percentage >= 90: return 10.0
    if percentage >= 80: return 9.0
    if percentage >= 70: return 8.0
    if percentage >= 60: return 7.0
    if percentage >= 50: return 6.0
    if percentage >= 40: return 5.0
    return 0.0

async def calculate_sgpa(student_id: str, db: AsyncSession) -> float:
    """
    Calculate Semester Grade Point Average (SGPA).
    Formula: Σ(Grade Point * Credits) / Σ(Credits)
    """
    # Fetch all enrollments for the student with their marks and subjects
    # Note: In a real app, filtering by semester is needed. Here we calculate overall.
    
    # We join Enrollment -> Subject and Enrollment -> Marks
    query = select(Enrollment).where(Enrollment.student_id == student_id)
    result = await db.execute(query)
    enrollments = result.scalars().all()
    
    total_credits = 0
    total_points = 0
    
    for enrollment in enrollments:
        # Load subject and marks specifically if not eager loaded
        # Ideally use select options(joinedload...) but for now simple lazy/explicit fetch
        
        # Fetch Subject
        subject_q = select(Subject).where(Subject.id == enrollment.subject_id)
        subject_res = await db.execute(subject_q)
        subject = subject_res.scalars().first()
        
        if not subject or not subject.credits:
            continue
            
        # Fetch Marks
        # Assuming we use the 'FINAL' exam for GPA or an average of all
        marks_q = select(Mark).where(Mark.enrollment_id == enrollment.id)
        marks_res = await db.execute(marks_q)
        marks = marks_res.scalars().all()
        
        if not marks:
            continue
            
        # Strategy: Use the mark with highest max_score (likely Final) or sum
        # For simplicity: Take the first mark found
        mark = marks[0] 
        
        grade_point = get_grade_point(mark.score, mark.max_score)
        total_points += (grade_point * subject.credits)
        total_credits += subject.credits
        
    if total_credits == 0:
        return 0.0
        
    return round(total_points / total_credits, 2)
