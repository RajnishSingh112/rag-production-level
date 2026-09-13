def recall_at_k(
    retrieved_sources: list[str],
    expected_sources: list[str],
    k: int,
) -> float:

    expected = set(expected_sources)

    retrieved = set(retrieved_sources[:k])

    if not expected:
        return 0.0

    return float(bool(expected.intersection(retrieved)))

def precision_at_k(
    retrieved_sources: list[str],
    expected_sources: list[str],
    k: int,
) -> float:

    expected = set(expected_sources)
    retrieved = retrieved_sources[:k]

    if not retrieved:
        return 0.0

    relevant_count = sum(
        1 for source in retrieved
        if source in expected
    )

    return relevant_count / len(retrieved)

def reciprocal_rank(
    retrieved_sources: list[str],
    expected_sources: list[str],
    k: int,
) -> float:

    expected = set(expected_sources)

    for rank, source in enumerate(retrieved_sources[:k], start=1):
        if source in expected:
            return 1.0 / rank

    return 0.0