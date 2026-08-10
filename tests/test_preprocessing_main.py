import sqlite3
def test_preprocessing():
    #DB set up
    connection = sqlite3.connect("db/ai_production.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT chunk_id
        FROM Embeddings
    """)
    rows = cursor.fetchall()
    #print(rows)
    cursor.execute("""
        SELECT filename, page_count FROM Documents
    """)
    documents = cursor.fetchall()
    print("\nDocuments:")
    for document in documents:
        print(document)

    cursor.execute("""
        SELECT document_id, COUNT(*)
        FROM Chunks
        GROUP BY document_id;
    """)
    chunk_counts = cursor.fetchall()
    print("chunks per document:")
    for count in chunk_counts:
        print(count)
    connection.close()