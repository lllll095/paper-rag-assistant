import re
from dataclasses import dataclass
from typing import List


@dataclass
class QueryRoute:
    query_type: str
    retrieval_mode: str
    paper_k: int
    chunk_k: int
    max_per_source: int
    reason: str


class QueryRouter:
    """
    A lightweight rule-based query router.

    It classifies user questions into different retrieval types and returns
    retrieval parameters for the RAG pipeline.
    """

    def __init__(self):
        self.comparison_patterns = [
            "difference between",
            "differences between",
            "compare",
            "comparison",
            "vs",
            "versus",
            "区别",
            "比较",
            "对比",
        ]

        self.survey_patterns = [
            "what methods",
            "which methods",
            "what approaches",
            "which approaches",
            "overview",
            "survey",
            "summarize the methods",
            "discussed in these papers",
            "in these papers",
            "all methods",
            "有哪些方法",
            "哪些方法",
            "综述",
            "总结这些方法",
        ]

        self.evidence_patterns = [
            "statistical guarantee",
            "statistical guarantees",
            "guarantee",
            "guarantees",
            "theorem",
            "proof",
            "bound",
            "control",
            "fnr",
            "tnr",
            "显著性",
            "统计保证",
            "理论保证",
        ]

        self.experiment_patterns = [
            "experiment",
            "experiments",
            "dataset",
            "datasets",
            "baseline",
            "baselines",
            "result",
            "results",
            "evaluation",
            "benchmark",
            "auroc",
            "accuracy",
            "实验",
            "数据集",
            "基准",
            "结果",
        ]

        self.method_patterns = [
            "how does",
            "how do",
            "work",
            "method",
            "algorithm",
            "framework",
            "pipeline",
            "propose",
            "proposed",
            "怎么做",
            "如何做",
            "方法",
            "算法",
            "框架",
        ]

    @staticmethod
    def normalize(text: str) -> str:
        text = text.lower()
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @staticmethod
    def contains_any(text: str, patterns: List[str]) -> bool:
        return any(pattern in text for pattern in patterns)

    def route(self, question: str) -> QueryRoute:
        q = self.normalize(question)

        if self.contains_any(q, self.comparison_patterns):
            return QueryRoute(
                query_type="comparison",
                retrieval_mode="global",
                paper_k=6,
                chunk_k=10,
                max_per_source=4,
                reason="The question asks for comparison between methods or papers.",
            )

        if self.contains_any(q, self.survey_patterns):
            return QueryRoute(
                query_type="survey",
                retrieval_mode="global",
                paper_k=6,
                chunk_k=10,
                max_per_source=3,
                reason="The question asks for a broad overview across papers.",
            )

        if self.contains_any(q, self.evidence_patterns):
            return QueryRoute(
                query_type="evidence",
                retrieval_mode="global",
                paper_k=6,
                chunk_k=10,
                max_per_source=3,
                reason="The question asks for theoretical/statistical evidence.",
            )

        if self.contains_any(q, self.experiment_patterns):
            return QueryRoute(
                query_type="experiment",
                retrieval_mode="global",
                paper_k=6,
                chunk_k=10,
                max_per_source=3,
                reason="The question asks about experiments, datasets, or results.",
            )

        if self.contains_any(q, self.method_patterns):
            return QueryRoute(
                query_type="method",
                retrieval_mode="auto",
                paper_k=4,
                chunk_k=8,
                max_per_source=3,
                reason="The question asks about how a method works.",
            )

        return QueryRoute(
            query_type="general",
            retrieval_mode="auto",
            paper_k=4,
            chunk_k=8,
            max_per_source=3,
            reason="No strong query type was detected; use automatic retrieval.",
        )