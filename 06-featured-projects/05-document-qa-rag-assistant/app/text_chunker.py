def chunk_text(
    extracted_sections,
    document_name,
    max_chunk_size=900,
    page_overlap_lines=8,
):
    chunks = []
    previous_page_context = []

    for section in extracted_sections:
        original_text = section["text"]
        page = section.get("page")

        lines = [
            line.strip()
            for line in original_text.split("\n")
            if line.strip()
        ]

        combined_lines = previous_page_context + lines

        current_parts = []
        current_length = 0
        chunk_number = 1

        for line in combined_lines:
            line_length = len(line)

            if (
                current_parts
                and current_length + line_length > max_chunk_size
            ):
                chunks.append(
                    {
                        "document": document_name,
                        "page": page,
                        "chunk_number": chunk_number,
                        "text": "\n".join(current_parts),
                    }
                )

                chunk_number += 1
                current_parts = []
                current_length = 0

            current_parts.append(line)
            current_length += line_length

        if current_parts:
            chunks.append(
                {
                    "document": document_name,
                    "page": page,
                    "chunk_number": chunk_number,
                    "text": "\n".join(current_parts),
                }
            )

        previous_page_context = lines[-page_overlap_lines:]

    return chunks
