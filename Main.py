import parser
import cleaner
import tokenizer
import chunker
import embedding
import sqlite3
from pathlib import Path
#Documents, Chunks, and Embeddings Tables
def create_tables(connection_1, cursor_1):
    cursor_1.execute("""
        CREATE TABLE IF NOT EXISTS Documents (
            document_id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            filetype TEXT NOT NULL,
            page_count INTEGER NOT NULL
        )
        """)
    cursor_1.execute("""
        CREATE TABLE IF NOT EXISTS Chunks (
            chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            chunk_index INTEGER,
            text TEXT
        )
        """)
    cursor_1.execute("""
        CREATE TABLE IF NOT EXISTS Embeddings (
            chunk_id INTEGER,
            embedding TEXT
        )
        """)
    connection_1.commit()
#Main function calls to preprocessing and then AI machine learning.
def main():
    #Tokenize test
    #print(tokenize("Hello, how are you doing today? Can't help you right now."))
    #print(parser.parse('SpaceX cover.docx').text)
    title = 'documents/learntocode.txt'
    title2 = 'documents/SpaceX cover.docx'
    '''
    #Loop through input folder
    documents_folder = Path("documents")

    for file in documents_folder.iterdir():
        if file.is_file():
    '''
    #DB set up
    connection = sqlite3.connect("db/ai_production.db")
    cursor = connection.cursor()
    create_tables(connection, cursor)

    #Data Preprocessing
    #Parse data from documents folder
    doc_id, doc_text = parser.parse(title, connection, cursor)

    #Clean data into proper format
    cleaned = cleaner.clean(doc_text)

    #Tokenize words
    tokenized = tokenizer.tokenize(cleaned)

    #Chunk into 100 word chunks
    chunked, chunk_ids = chunker.chunk(tokenized, doc_id, connection, cursor)

    #print(chunked)
    print(chunked[0])
    #AI transformation


    embeddings = embedding.generateEmbedding(chunked, chunk_ids, connection, cursor)
    #embedding.insert_embeddings(embeddings, connection, cursor)

    print(embeddings[0].shape)
    print(embeddings[0])
    #Close down shop (SQLite3 complete)
    connection.close()
if __name__ == "__main__":
    main()