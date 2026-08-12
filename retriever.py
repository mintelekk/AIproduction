import sqlite3
import json
from ollama import chat
import numpy as np
from sentence_transformers import SentenceTransformer
def cosineSimilarity(v1, v2):
    #Cosine similarity calculation
    dotProduct= np.dot(v1,v2)
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    denominator = np.multiply(mag1,mag2)
    ans = np.divide(dotProduct, denominator)
    return ans

def get_embeddings(cursor):
    ans = []
    #SQL select query to get from database
    cursor.execute(""" 
        SELECT chunk_id, embedding
        FROM Embeddings
    """)
    #Append to answer string the loaded embedding
    for row in cursor.fetchall():
        embedding = np.array(json.loads(row[1]))
        ans.append((row[0], embedding))
    return ans

def rank_chunks(question_embedding, rows, top_n):

    cosine_sim = []
    #Compute all cosine similarities
    for row in rows:
        cosine_sim.append((row[0], cosineSimilarity(question_embedding, row[1])))
    #Sort in reverse (Highest to lowest) top n results for cosine similarity
    top_n_chunks = sorted([(chunk_id, similarity) for chunk_id, similarity in cosine_sim], key=lambda x: x[1], reverse=True)[:top_n]
    return top_n_chunks
    #Convert to dictionary to find chunks
    #embedding_dict = {chunk_id: embedding for chunk_id, embedding in rows}
    #Answer -> embeddings of each chunk
    #top_n_embeddings = [embedding_dict[chunk_id] for chunk_id, sim in top_n_chunks]

def get_chunk_text(top_n_chunks, cursor):
    texts = []
    for chunk_id, score in top_n_chunks:
        cursor.execute("""
            SELECT text
            FROM chunks
            WHERE chunk_id = ?
        """, (chunk_id,))
        row = cursor.fetchone()
        texts.append(row[0])
    return texts

def print_answer(top_n_chunks, cursor):
    texts = get_chunk_text(top_n_chunks, cursor)
    #print(top_n_chunks)
    for i in range(len(top_n_chunks)):

        print("\nCosine Similarity: ", top_n_chunks[i][1])
        print("\n", texts[i])

def print_answer_LLM(top_n_chunks, question, cursor):
    texts = get_chunk_text(top_n_chunks, cursor)
    context = "\n\n".join(texts)
    response = chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": "Answer the user's question using only the provided context."
            },
            {
                "role": "user",
                "content": f"""
                Context:
                {context}

                Question:
                {question}
                """
            }
        ]
    )
    print(response.message.content, "\n Accuracy ranking: ", round(top_n_chunks[4][1],3), "-", round(top_n_chunks[0][1], 3))

def main():
    # 1. Load a pretrained Sentence Transformer model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    
    connection = sqlite3.connect("db/ai_production.db")
    cursor = connection.cursor()

    rows = get_embeddings(cursor)

    question = input("Enter a question you want to ask about the source books in documents/ folder:\n")
    q_embedding = model.encode(question)
    rows_1 = rank_chunks(q_embedding, rows, 5)
    print_answer_LLM(rows_1, question, cursor)
    connection.close()
if __name__ == "__main__":
    main()