def merge_adjacent_chunks(results):
    merged = []

    for result in results:
        if not merged:
            merged.append(result)
            continue

        previous = merged[-1]

        same_document = (
            previous["metadata"]["document"]
            == result["metadata"]["document"]
        )

        previous_page = previous["metadata"]["page"]
        current_page = result["metadata"]["page"]

        adjacent_page = (
            current_page == previous_page
            or current_page == previous_page + 1
        )

        if same_document and adjacent_page:
            previous["text"] = (
                previous["text"].rstrip()
                + "\n"
                + result["text"].lstrip()
            )

            previous["metadata"]["page_end"] = current_page

            previous["score"] = max(
                previous["score"],
                result["score"],
            )

        else:
            merged.append(result)

    return merged

