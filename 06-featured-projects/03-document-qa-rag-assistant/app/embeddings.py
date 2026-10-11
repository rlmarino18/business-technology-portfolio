from openai import OpenAI


EMBEDDING_MODEL = "text-embedding-3-small"


def create_embedding(text, client=None):
    if client is None:
        client = OpenAI()

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response.data[0].embedding


def create_embeddings(chunks, client=None):
    if client is None:
        client = OpenAI()

    embedded_chunks = []

    for chunk in chunks:
        embedding = create_embedding(
            text=chunk["text"],
            client=client,
        )

        embedded_chunks.append(
            {
                **chunk,
                "embedding": embedding,
            }
        )

    return embedded_chunks
