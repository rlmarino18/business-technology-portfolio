import re


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by",
    "for", "from", "how", "in", "is", "it", "of", "on",
    "or", "that", "the", "to", "what", "when", "where",
    "which", "who", "why", "with", "my", "does", "do",
}


def tokenize(text):
    return [
        token
        for token in re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower(),
        )
        if token not in STOPWORDS
    ]


def is_heading(line):
    if len(line) > 80:
        return False

    if line.startswith(("●", "-", "•")):
        return False

    if line.endswith((".", "?", "!")):
        return False

    return True


def build_sections(lines):
    sections = []
    current_section = []

    for line in lines:
        if is_heading(line) and current_section:
            sections.append(current_section)
            current_section = [line]
        else:
            current_section.append(line)

    if current_section:
        sections.append(current_section)

    return sections


def select_best_evidence(question, text):
    question_tokens = set(tokenize(question))

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    sections = build_sections(lines)

    scored_sections = []

    for section in sections:
        section_text = "\n".join(section)
        section_tokens = set(tokenize(section_text))

        matches = question_tokens.intersection(
            section_tokens
        )

        scored_sections.append(
            {
                "section": section,
                "score": len(matches),
            }
        )

    ranked = sorted(
        scored_sections,
        key=lambda item: item["score"],
        reverse=True,
    )

    if not ranked or ranked[0]["score"] == 0:
        return []

    best_section_index = scored_sections.index(
        ranked[0]
    )

    selected = list(
        scored_sections[best_section_index]["section"]
    )

    if best_section_index + 1 < len(scored_sections):
        next_section = scored_sections[
            best_section_index + 1
        ]["section"]

        selected.extend(next_section)

    return selected