import streamlit as st

from document_processor import extract_text
from text_chunker import chunk_text
from local_embeddings import (
    create_local_embeddings,
    create_local_query_embedding,
)
from vector_store import add_chunks, query_chunks
from reranker import rerank_results


EVIDENCE_DISTANCE_THRESHOLD = 2.0


def get_grounding_label(distance):
    if distance <= 0.35:
        return "High"
    if distance <= 0.60:
        return "Medium"
    return "Low"


st.set_page_config(
    page_title="Document QA RAG Assistant",
    page_icon="📄",
    layout="wide",
)

st.title("Document QA RAG Assistant")

st.write(
    "Upload operational documents and retrieve evidence grounded in their contents."
)

uploaded_files = st.file_uploader(
    "Upload documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
)

if "documents_indexed" not in st.session_state:
    st.session_state.documents_indexed = False

if uploaded_files and not st.session_state.documents_indexed:
    all_chunks = []

    with st.spinner("Processing and indexing documents..."):
        for uploaded_file in uploaded_files:
            try:
                extracted_sections = extract_text(uploaded_file)

                chunks = chunk_text(
                    extracted_sections=extracted_sections,
                    document_name=uploaded_file.name,
                )

                all_chunks.extend(chunks)

                st.success(
                    f"{uploaded_file.name}: "
                    f"{len(chunks)} chunk(s) created."
                )

            except Exception as error:
                st.error(
                    f"Could not process {uploaded_file.name}: {error}"
                )

        if all_chunks:
            embeddings = create_local_embeddings(all_chunks)

            add_chunks(
                chunks=all_chunks,
                embeddings=embeddings,
            )

            st.session_state.documents_indexed = True

            st.success(
                f"Indexed {len(all_chunks)} total document chunks."
            )

question = st.text_input(
    "Ask a question about your documents"
)

if question and st.session_state.documents_indexed:
    query_embedding = create_local_query_embedding(question)

    results = query_chunks(
        query_embedding=query_embedding,
        n_results=15,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    reranked = rerank_results(
        question=question,
        documents=documents,
        metadatas=metadatas,
        distances=distances,
    )

    st.subheader("Retrieved Evidence")

    for index, result in enumerate(
        reranked,
        start=1,
    ):
        grounding = get_grounding_label(
            result["distance"]
        )

        st.markdown(f"### Result {index}")

        st.write(result["text"])

        st.caption(
            f"Source: {result['metadata']['document']} | "
            f"Page: {result['metadata']['page']} | "
            f"Chunk: {result['metadata']['chunk_number']} | "
            f"Grounding: {grounding} | "
            f"Distance: {result['distance']:.4f} | "
            f"Keyword Matches: {result['keyword_matches']} | "
            f"Proximity Score: {result['proximity_score']:.2f} | "
            f"Rerank Score: {result['score']:.4f}"
        )

elif question:
    st.warning(
        "Upload and index documents before asking a question."
    )
