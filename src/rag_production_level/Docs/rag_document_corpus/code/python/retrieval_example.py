from dataclasses import dataclass


@dataclass(frozen=True)
class SearchResult:
    chunk_id: str
    score: float
    text: str


def reciprocal_rank_fusion(
    ranked_lists: list[list[SearchResult]],
    k: int = 60,
) -> list[SearchResult]:
    scores: dict[str, float] = {}
    by_id: dict[str, SearchResult] = {}

    for results in ranked_lists:
        for rank, result in enumerate(results, start=1):
            scores[result.chunk_id] = scores.get(result.chunk_id, 0.0) + 1.0 / (k + rank)
            by_id[result.chunk_id] = result

    return sorted(
        (by_id[chunk_id] for chunk_id in scores),
        key=lambda item: scores[item.chunk_id],
        reverse=True,
    )
