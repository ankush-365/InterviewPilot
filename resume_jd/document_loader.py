import fitz

def extract_resume_text(uploaded_file):

    pdf_bytes = uploaded_file.read()

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def load_jd(jd_text):

    return jd_text.strip()

