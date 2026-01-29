from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum
from database import Base

class UserRole(str, enum.Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    FACULTY = "FACULTY"
    STUDENT = "STUDENT"

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.STUDENT)
    is_active = Column(Boolean, default=True)

    # Relationships
    department_head_of = relationship("Department", back_populates="head_of_dept", uselist=False)
    enrollments = relationship("Enrollment", back_populates="student")

class College(Base):
    __tablename__ = "colleges"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)
    
    departments = relationship("Department", back_populates="college")

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    college_id = Column(UUID(as_uuid=True), ForeignKey("colleges.id"))
    head_of_dept_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    college = relationship("College", back_populates="departments")
    head_of_dept = relationship("User", back_populates="department_head_of")
    courses = relationship("Course", back_populates="department")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String) # e.g. B.Tech CSE
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="courses")
    semesters = relationship("Semester", back_populates="course")

class Semester(Base):
    __tablename__ = "semesters"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String) # e.g. Semester 1
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"))
    
    course = relationship("Course", back_populates="semesters")
    subjects = relationship("Subject", back_populates="semester")

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    code = Column(String)
    credits = Column(Integer)
    semester_id = Column(UUID(as_uuid=True), ForeignKey("semesters.id"))
    
    semester = relationship("Semester", back_populates="subjects")
    enrollments = relationship("Enrollment", back_populates="subject")

class Enrollment(Base):
    __tablename__ = "enrollments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"))
    academic_year = Column(String) # e.g. "2023-2024"
    
    student = relationship("User", back_populates="enrollments")
    subject = relationship("Subject", back_populates="enrollments")
    attendance_records = relationship("Attendance", back_populates="enrollment")
    marks = relationship("Mark", back_populates="enrollment")

class AttendanceStatus(str, enum.Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    LATE = "LATE"
    EXCUSED = "EXCUSED"

class Attendance(Base):
    __tablename__ = "attendance"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enrollment_id = Column(UUID(as_uuid=True), ForeignKey("enrollments.id"))
    date = Column(String) # Storing as ISO Date String for simplicity or could use Date
    status = Column(Enum(AttendanceStatus), default=AttendanceStatus.ABSENT)
    
    enrollment = relationship("Enrollment", back_populates="attendance_records")

class Mark(Base):
    __tablename__ = "marks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enrollment_id = Column(UUID(as_uuid=True), ForeignKey("enrollments.id"))
    exam_type = Column(String) # One of: MST1, MST2, FINAL, ASSIGNMENT
    score = Column(Integer)
    max_score = Column(Integer)
    
    enrollment = relationship("Enrollment", back_populates="marks")

