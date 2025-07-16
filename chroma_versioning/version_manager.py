
import chromadb
from sentence_transformers import SentenceTransformer
import os

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

model = SentenceTransformer('all-MiniLM-L6-v2')

def add_version(chapter_id, version_text, metadata):
    embedding = model.encode([version_text])[0]
    collection.add(
        documents=[version_text],
        ids=[chapter_id],
        embeddings=[embedding.tolist()],
        metadatas=[metadata]
    )
    print(f"✅ Stored version: {chapter_id} with metadata {metadata}")

# EXAMPLE USAGE (for testing)
if __name__ == "__main__":
    with open("../output/chapter1_review.txt", "r", encoding="utf-8") as f:
        text = f.read()

    add_version(
        chapter_id="chapter1_reviewed",
        version_text=text,
        metadata={
            "version": "reviewed",
            "chapter": "1",
            "author": "AI",
            "date": "2025-07-13",
            "feedback_score": 4.5
        }
    )
