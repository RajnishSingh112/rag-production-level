from rag_production_level.retrieval.fusion.rrf import (
    ReciprocalRankFusion,
)


def test_rrf_combines_rankings():

    vector_results = [
        "A",
        "B",
        "C",
    ]

    bm25_results = [
        "B",
        "A",
        "D",
    ]

    rrf = ReciprocalRankFusion()

    results = rrf.fuse(
        [vector_results, bm25_results],
        top_k=4,
    )

    assert results[0] in ["A", "B"]
    assert "A" in results
    assert "B" in results
    assert "D" in results
    assert "C" in results