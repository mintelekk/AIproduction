from sentence_transformers import SentenceTransformer
import sqlite3
import json
# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
def insert_embedding(embeddings_1, chunk_ids, connection, cursor):
    

    for i, e in zip(chunk_ids, embeddings_1):
        #Serialize into string for sql db
        e_j = json.dumps(e.tolist())
        cursor.execute(
            """
            INSERT INTO Embeddings (chunk_id, embedding)
            VALUES(?, ?)
            """,
            (i, e_j)
        )
    connection.commit()

def generateEmbedding(chunks, chunk_ids, connection_1, cursor_1):
    embeddings = []
    #Loop through chunks of 100 tokens.
    for chunk_i in chunks:
        #Textual form of chunk without ending index
        #print(chunk_i)
        string1 = " ".join(chunk_i.words)
        embedding1 = model.encode(string1)
        #print(embeddings.shape)
        #print(embeddings)
        embeddings.append(embedding1)

    insert_embedding(embeddings, chunk_ids, connection_1, cursor_1)
    return embeddings