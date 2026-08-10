import sqlite3
from chunker import insert_chunks, ChunkObj


def test_insert_chunks():
    # Create temporary in-memory database
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create the table
    cursor.execute("""
        CREATE TABLE Chunks (
            chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            chunk_index INTEGER,
            text TEXT
        )
    """)

    # Create test chunks
    chunks = [
        ChunkObj(["The", "cat", "sat"], 1, 1),
        ChunkObj(["The", "dog", "ran"], 2, 1),
        ChunkObj(["The", "bird", "flew"], 3, 1)
    ]

    # Test your function
    chunk_ids = insert_chunks(chunks, connection, cursor)

    # Verify IDs were generated
    assert len(chunk_ids) == 3
    assert chunk_ids == [1, 2, 3]

    # Verify database contents
    cursor.execute("SELECT text, chunk_index, document_id FROM Chunks")
    rows = cursor.fetchall()

    assert rows == [
        ("The cat sat", 1, 1),
        ("The dog ran", 2, 1),
        ("The bird flew", 3, 1)
    ]

    connection.close()