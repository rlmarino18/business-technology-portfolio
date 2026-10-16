import chromadb


COLLECTION_NAME = "document_chunks"


def get_collection():
    client = chromadb.PersistentClient(path="chroma_db")

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def add_chunks(chunks, embeddings):
    collection = get_collection()

    ids = []
    documents = []
    metadatas = []

    for index, chunk in enumerate(chunks):
        ids.append(
            f"{chunk['document']}-{chunk['page']}-{chunk['chunk_number']}-{index}"
        )

        documents.append(chunk["text"])

        metadatas.append(
            {
                "document": chunk["document"],
                "page": chunk["page"] if chunk["page"] is not None else -1,
                "chunk_number": chunk["chunk_number"],
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings,
    )


def query_chunks(query_embedding, n_results=3):
    collection = get_collection()

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )
