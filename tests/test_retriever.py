from __future__ import annotations

from studyflow.retriever import retrieve


def test_retrieve_prefers_relevant_document():
    docs = {
        "assignment.md": "Build architecture proposal and proof of concept for final project.",
        "notes.md": "Remember to buy groceries and clean your desk.",
    }

    results = retrieve("architecture proof of concept", docs, top_k=2)

    assert results, "Expected at least one retrieved result"
    assert results[0].source == "assignment.md"
    assert results[0].score > 0


def test_retrieve_returns_empty_when_no_match():
    docs = {"notes.md": "This text has no overlapping terms."}

    results = retrieve("mcp rag agent", docs, top_k=3)

    assert results == []
