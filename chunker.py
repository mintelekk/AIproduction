import math
import sqlite3
class ChunkObj:
    def __init__(self, words, chunk_id, document_id):
        self.words = words
        self.chunk_id = chunk_id
        self.document_id = document_id
    words: list
    chunk_id: int
    document_id: int
#Insert Chunk object into SQLite3
def insert_chunks(chunks, connection_1, cursor_1):
    chunk_ids = []
    for i, c in enumerate(chunks):
        cursor_1.execute(
            """
            INSERT INTO Chunks (text, chunk_index, document_id)
            VALUES (?, ?, ?)
            """,
            (" ".join(c.words), i+1, c.document_id)
        )
        chunk_ids.append(cursor_1.lastrowid)
    connection_1.commit()
    #Returns primary index key list
    return chunk_ids

#Order tokens into lists of 100 length.
def chunk(tokens, doc_id, connection_1, cursor_1):
    chunks = []
    for i in range(0, len(tokens), 100):
        chunki = []
        for i2 in range(i, min(i+ 100,len(tokens))):
            chunki.append(tokens[i2])
        #Chunks end with index label.
        #chunks.append(chunki + [math.floor((i+1)/100)])
        #chunks end with document_id
        chunks.append(ChunkObj(chunki, i+1, doc_id))
    chunk_ids = insert_chunks(chunks, connection_1, cursor_1)
    return chunks, chunk_ids