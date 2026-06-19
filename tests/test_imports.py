"""Smoke tests for paper-rag-assistant."""

import sys
from pathlib import Path


def test_reranker_import():
    """Verify core modules can be imported."""
    src_dir = Path(__file__).resolve().parents[1] / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    from query_router import QueryRouter
    from reranker import CrossEncoderReranker
    assert QueryRouter is not None
    assert CrossEncoderReranker is not None


def test_query_router_classification():
    """Test query router classifies question types correctly."""
    src_dir = Path(__file__).resolve().parents[1] / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    from query_router import QueryRouter

    router = QueryRouter()

    route = router.route("How does AdaDetectGPT work?")
    assert route is not None
    assert route.query_type == "method"

    route2 = router.route("What is the difference between DetectGPT and AdaDetectGPT?")
    assert route2 is not None
    assert route2.query_type == "comparison"


def test_reranker_import():
    """Test CrossEncoderReranker can be instantiated."""
    src_dir = Path(__file__).resolve().parents[1] / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    from reranker import CrossEncoderReranker
    assert CrossEncoderReranker is not None


def test_split_text():
    """Test text chunking utilities."""
    src_dir = Path(__file__).resolve().parents[1] / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    from split_text import infer_chunk_type, clean_text

    assert infer_chunk_type("This is main text content") == "main"
    assert infer_chunk_type("References\n1. Paper A") == "references"
    assert clean_text(None) == ""
    assert clean_text("  hello  ") == "hello"
