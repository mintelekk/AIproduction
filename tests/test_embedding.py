
import sqlite3
import json
import numpy as np

from embedding import generateEmbedding
from chunker import ChunkObj


def test_generate_embedding():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Embeddings (
            chunk_id INTEGER,
            embedding TEXT
        )
    """)

    chunks = [
        ChunkObj(["The", "cat", "sat", "on", "the", "mat"], 1, 1),
        ChunkObj(["Python", "is", "a", "programming", "language"], 2, 1)
    ]

    chunk_ids = [1, 2]

    embeddings = generateEmbedding(
        chunks,
        chunk_ids,
        connection,
        cursor
    )

    # Verify two embeddings were generated
    assert len(embeddings) == 2

    # Verify each embedding has 384 dimensions
    for embedding in embeddings:
        assert isinstance(embedding, np.ndarray)
        assert embedding.shape == (384,)

    connection.close()


def test_embeddings_inserted_into_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Embeddings (
            chunk_id INTEGER,
            embedding TEXT
        )
    """)

    chunks = [
        ChunkObj(["The", "cat", "sat"], 1, 1),
        ChunkObj(["The", "dog", "ran"], 2, 1)
    ]

    chunk_ids = [10, 11]

    generateEmbedding(
        chunks,
        chunk_ids,
        connection,
        cursor
    )

    cursor.execute("""
        SELECT chunk_id, embedding
        FROM Embeddings
    """)

    rows = cursor.fetchall()

    # Verify two rows were inserted
    assert len(rows) == 2

    # Verify chunk IDs
    assert rows[0][0] == 10
    assert rows[1][0] == 11

    # Verify embeddings were stored as JSON text
    for chunk_id, embedding_json in rows:
        assert isinstance(embedding_json, str)

        # Convert JSON back into a Python list
        embedding_list = json.loads(embedding_json)

        # Verify it contains 384 numbers
        assert len(embedding_list) == 384
        assert all(isinstance(value, (int, float)) for value in embedding_list)

    connection.close()
