from fpdf import FPDF
import tempfile
import os

class ReportGenerator(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.cell(0, 10, 'UNIManager University', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

def generate_hall_ticket_pdf(student_data: dict, exams: list) -> str:
    """
    Generates a Hall Ticket PDF and returns the file path.
    """
    pdf = ReportGenerator()
    pdf.add_page()
    
    # Student Info
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 10, f"HALL TICKET - {student_data.get('term', 'Semester Exam')}", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)
    
    pdf.cell(50, 10, f"Name: {student_data.get('name')}")
    pdf.ln(6)
    pdf.cell(50, 10, f"Roll No: {student_data.get('id')}")
    pdf.ln(6)
    pdf.cell(50, 10, f"Course: {student_data.get('course')}")
    pdf.ln(15)
    
    # Exam Table
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(90, 10, 'Subject', border=1)
    pdf.cell(40, 10, 'Date', border=1)
    pdf.cell(40, 10, 'Time', border=1)
    pdf.ln()
    
    pdf.set_font('Helvetica', '', 10)
    for exam in exams:
        pdf.cell(90, 10, str(exam.get('subject')), border=1)
        pdf.cell(40, 10, str(exam.get('date', 'TBD')), border=1)
        pdf.cell(40, 10, str(exam.get('time', '10:00 AM')), border=1)
        pdf.ln()
        
    # Save to temp
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"hall_ticket_{student_data.get('id')}.pdf")
    pdf.output(file_path)
    return file_path

def generate_result_card_pdf(student_data: dict, results: list, sgpa: float) -> str:
    """
    Generates a Grade Card PDF.
    """
    pdf = ReportGenerator()
    pdf.add_page()
    
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 10, f"OFFICIAL GRADE CARD", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)
    
    pdf.cell(50, 10, f"Name: {student_data.get('name')}")
    pdf.ln(10)
    
    # Results Table
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(100, 10, 'Subject', border=1)
    pdf.cell(30, 10, 'Marks', border=1)
    pdf.cell(30, 10, 'Grade', border=1)
    pdf.ln()
    
    pdf.set_font('Helvetica', '', 10)
    for res in results:
        pdf.cell(100, 10, str(res.get('subject')), border=1)
        pdf.cell(30, 10, str(res.get('score')), border=1)
        pdf.cell(30, 10, str(res.get('grade')), border=1)
        pdf.ln()
        
    pdf.ln(10)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, f"SGPA: {sgpa}", align='R')
    
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"result_{student_data.get('id')}.pdf")
    pdf.output(file_path)
    return file_path
