from sentence_transformers import SentenceTransformer
import sqlite3
# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def generateEmbedding(chunks, chunk_ids):
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
    return embeddings