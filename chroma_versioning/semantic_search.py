
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_versions(query, top_k=3):
    embedding = model.encode([query])[0]
    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=top_k
    )
    for i, doc in enumerate(results["documents"][0]):
        print(f"\n🔍 Match {i+1}:")
        print("Text:", doc)
        print("Metadata:", results["metadatas"][0][i])

# EXAMPLE USAGE
if __name__ == "__main__":
    search_versions("Find chapters rewritten in humorous tone")

