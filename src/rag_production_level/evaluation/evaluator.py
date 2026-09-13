from pathlib import Path
import json

from rag_production_level.evaluation.metrics import (recall_at_k , precision_at_k, reciprocal_rank)

class Evaluator:

    def load_evaluation_data(self, file_path: Path) -> list[dict]:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def evaluate(self, question:dict,retriever,documents,k:int=5) -> float:
        retrieved_docs = retriever.retrieve(question["question"], documents, top_k=k)
        #retrieved_sources = [doc.metadata.get("source", "unknown") for doc in retrieved_docs]
        retrieved_sources = []
        for document in retrieved_docs:
            print("RAW SOURCE:", document.metadata.get("source"))
        
            source = Path(document.metadata.get("source", "")).name
        
            print("EXTRACTED SOURCE:", source)
        
            retrieved_sources.append(source)
        expected_sources = question["sources"]
        print("\nQuestion:", question["question"])
        print("Expected Sources:", expected_sources)
        print("Retrieved Sources:", retrieved_sources)
        recall =  recall_at_k(retrieved_sources, expected_sources, k)
        precision = precision_at_k(retrieved_sources, expected_sources, k)
        reciprocal_rank_value = reciprocal_rank(retrieved_sources, expected_sources, k)
        return {"recall": recall, "precision": precision, "reciprocal_rank": reciprocal_rank_value}

    def evaluate_all(self,questions: list[dict],retriever,documents,k: int = 5,) -> float:

        results = []
        precision = []
        reciprocal_ranks = []
    
        for question in questions:
            result = self.evaluate(
                question,
                retriever,
                documents,
                k,
            )
    
            results.append(result["recall"])
            precision.append(result["precision"])
            reciprocal_ranks.append(result["reciprocal_rank"])
    
            print(
                f"{question['id']} Recall@{k}: {result['recall']:.2%} Precision@{k}: {result['precision']:.2%} Reciprocal Rank@{k}: {result['reciprocal_rank']:.2%}"
            )
    
        overall_recall = sum(results) / len(results)
        overall_precision = sum(precision) / len(precision)
        overall_reciprocal_rank = sum(reciprocal_ranks) / len(reciprocal_ranks)

        return {
            "overall_recall": overall_recall,
            "overall_precision": overall_precision,
            "overall_reciprocal_rank": overall_reciprocal_rank
        }