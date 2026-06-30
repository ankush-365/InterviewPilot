from resume_jd.document_loader import extract_resume_text

def parse_resume(pdf_path):
    resume_text = extract_resume_text(
        pdf_path
    )

    return resume_text
