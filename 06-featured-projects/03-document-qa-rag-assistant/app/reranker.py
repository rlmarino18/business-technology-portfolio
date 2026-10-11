import re

from sentence_transformers import CrossEncoder


RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

_model = None


def get_reranker():
    global _model

    if _model is None:
        _model = CrossEncoder(RERANKER_MODEL)

    return _model


def tokenize(text):
    return set(
        re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower(),
        )
    )


def rerank_results(
    question,
    documents,
    metadatas,
    distances,
):
    model = get_reranker()

    pairs = [
        [question, document]
        for document in documents
    ]

    scores = model.predict(pairs)

    question_tokens = tokenize(question)

    ranked_results = []

    for text, metadata, distance, score in zip(
        documents,
        metadatas,
        distances,
        scores,
    ):
        document_tokens = tokenize(text)

        keyword_matches = len(
            question_tokens.intersection(
                document_tokens
            )
        )

        ranked_results.append(
            {
                "text": text,
                "metadata": metadata,
                "distance": distance,
                "keyword_matches": keyword_matches,
                "proximity_score": 0.0,
                "score": float(score),
            }
        )

    return sorted(
        ranked_results,
        key=lambda result: result["score"],
        reverse=True,
    )