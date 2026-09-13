from rag_production_level.evaluation.metrics import (recall_at_k, precision_at_k, reciprocal_rank)


def test_recall_at_k_hit():
    retrieved = ["C", "A", "D", "E", "F"]
    expected = ["A"]

    result = recall_at_k(retrieved, expected, 5)

    assert result == 1.0


def test_recall_at_k_miss():
    retrieved = ["C", "D", "E", "F", "G"]
    expected = ["A"]

    result = recall_at_k(retrieved, expected, 5)

    assert result == 0.0

def test_reciprocal_rank():
    retrieved = [
        "wrong1.txt",
        "wrong2.txt",
        "correct.txt",
        "wrong3.txt",
    ]

    expected = ["correct.txt"]

    result = reciprocal_rank(
        retrieved,
        expected,
        k=4,
    )

    assert result == 1 / 3

def test_reciprocal_rank_not_found():
    retrieved = [
        "wrong1.txt",
        "wrong2.txt",
        "wrong3.txt",
    ]

    expected = ["correct.txt"]

    result = reciprocal_rank(
        retrieved,
        expected,
        k=3,
    )

    assert result == 0.0

def test_precision_at_k():
    retrieved = [
        "a.txt",
        "b.txt",
        "wrong.txt",
        "c.txt",
        "another.txt",
    ]

    expected = [
        "a.txt",
        "c.txt",
    ]

    result = precision_at_k(retrieved, expected, k=5)

    assert result == 0.4