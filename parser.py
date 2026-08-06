from pypdf import PdfReader
import sys
import re
from dataclasses import dataclass
import docx2txt
import sqlite3
@dataclass
class Document:
    
    filename: str
    file_type: str
    text: str
    page_count:int

def is_valid_filename(filename, ending):
    # Define a regex pattern for invalid filename characters
    invalid_chars_pattern = r'[<>:"\\|?*]'
    
    # Check if the filename contains invalid characters or doesn't end with ".pdf"
    if re.search(invalid_chars_pattern, filename) or not filename.lower().endswith(ending):
        return False
    return True

#Insert document obj into SQLite3 database
def insert_document(document, connection_1, cursor_1):
    cursor_1.execute(
        """
        INSERT INTO Documents (filename, filetype, page_count)
        VALUES (?, ?, ?)
        """,
        (document.filename, document.file_type, document.page_count)
    )
    connection_1.commit()
    #Returns primary index key
    return cursor_1.lastrowid

def parse(filename, connection_1, cursor_1):
    
    if is_valid_filename(filename, '.pdf'):
        #Parse pdf
        reader = PdfReader(filename)
        text = "\n".join(p.extract_text() for p in reader.pages)
    
        # Document Data container -> Filename, File Type, Text, Page count, document_id
        doc_1 = Document(filename, '.pdf', text, len(reader.pages))
        doc_id = insert_document(doc_1, connection_1, cursor_1)
        return doc_id, doc_1.text
    elif is_valid_filename(filename, '.txt'):
        #Parse txt
        reader = open(filename, 'r+')
        text = "".join(line for line in reader.readlines())
        doc_1 = Document(filename, '.txt', text, 1)
        doc_id = insert_document(doc_1, connection_1, cursor_1)
        return doc_id, doc_1.text
    elif is_valid_filename(filename, '.docx'):
        #Parse docx
        text1 = docx2txt.process(filename)
        doc_1 = Document(filename, '.docx', text1, 1)
        doc_id = insert_document(doc_1, connection_1, cursor_1)
        return doc_id, doc_1.text
    else:
        print("Invalid file. File must exist and end with .pdf, .txt, or .docx")
        sys.exit()
    