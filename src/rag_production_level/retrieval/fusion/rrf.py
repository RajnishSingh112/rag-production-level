from collections import defaultdict


class ReciprocalRankFusion:

    def __init__(self, k: int = 60):
        self.k = k

    def fuse(
        self,
        ranked_lists: list[list[str]],
        top_k: int = 5,
    ) -> list[str]:

        scores = defaultdict(float)

        for ranked_list in ranked_lists:

            for rank, document_id in enumerate(
                ranked_list,
                start=1,
            ):
                scores[document_id] += 1 / (
                    self.k + rank
                )

        ranked_documents = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            document_id
            for document_id, _ in ranked_documents[:top_k]
        ]