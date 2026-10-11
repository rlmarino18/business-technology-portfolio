from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

_model = None


def get_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)

    return _model


def create_local_embeddings(chunks):
    model = get_model()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
    )

    return embeddings.tolist()


def create_local_query_embedding(question):
    model = get_model()

    embedding = model.encode(
        question,
        normalize_embeddings=True,
    )

    return embedding.tolist()
