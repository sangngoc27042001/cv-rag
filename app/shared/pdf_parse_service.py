import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file_content):
    """The same as extract_text_from_pdf but returns text for each slide separately."""
    list_texts = []
    
    reader = PyPDF2.PdfReader(BytesIO(pdf_file_content))
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        list_texts.append(f'**Page number {i+1}**\n{text}')
    
    result_text = '\n\n------page separator------\n\n'.join(list_texts)
    return result_text
