from app.local_embeddings import (
    create_local_embeddings,
    create_local_query_embedding,
)
from app.vector_store import add_chunks, query_chunks


chunks = [
    {
        "document": "procurement_policy.txt",
        "page": 1,
        "chunk_number": 1,
        "text": "Purchases over $10,000 require approval from the Finance Director.",
    },
    {
        "document": "travel_policy.txt",
        "page": 2,
        "chunk_number": 1,
        "text": "Employees must submit travel expenses within 30 days.",
    },
]

embeddings = create_local_embeddings(chunks)

add_chunks(
    chunks=chunks,
    embeddings=embeddings,
)

question = "Who must approve purchases above ten thousand dollars?"

query_embedding = create_local_query_embedding(question)

results = query_chunks(
    query_embedding=query_embedding,
    n_results=1,
)

print(results["documents"][0][0])
print(results["metadatas"][0][0])
