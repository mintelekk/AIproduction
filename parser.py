from pypdf import PdfReader
import sys
import re
from dataclasses import dataclass
import docx2txt
@dataclass
class Document:
    filename: str
    file_type: str
    text: str
    page_count:int
    document_id: int

def is_valid_filename(filename, ending):
    # Define a regex pattern for invalid filename characters
    invalid_chars_pattern = r'[<>:"\\|?*]'
    
    # Check if the filename contains invalid characters or doesn't end with ".pdf"
    if re.search(invalid_chars_pattern, filename) or not filename.lower().endswith(ending):
        return False
    return True

document_id = 1
def parse(filename):
    
    if is_valid_filename(filename, '.pdf'):
        #Parse pdf
        reader = PdfReader(filename)
        text = "\n".join(p.extract_text() for p in reader.pages)
    
        # Document Data container -> Filename, File Type, Text, Page count, document_id
        doc_1 = Document(filename, '.pdf', text, len(reader.pages), document_id)
        document_id += 1
        return doc_1
    elif is_valid_filename(filename, '.txt'):
        #Parse txt
        reader = open(filename, 'r+')
        text = "".join(line for line in reader.readlines())
        doc_1 = Document(filename, '.txt', text, 1, document_id)
        document_id += 1
        return doc_1
    elif is_valid_filename(filename, '.docx'):
        #Parse docx
        text1 = docx2txt.process(filename)
        doc_1 = Document(filename, '.docx', text1, 1, document_id)
        document_id += 1
        return doc_1
    else:
        print("Invalid file. File must exist and end with .pdf, .txt, or .docx")
        sys.exit()
    