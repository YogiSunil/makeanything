from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass
class RetrievedResult:
    source: str
    score: int
    text: str


def _tokenize(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9_]+", value.lower()))


def retrieve(query: str, docs: dict[str, str], top_k: int = 3) -> list[RetrievedResult]:
    query_tokens = _tokenize(query)
    if not query_tokens:
        return []

    matches: list[RetrievedResult] = []
    for source, text in docs.items():
        score = len(query_tokens.intersection(_tokenize(text)))
        if score > 0:
            matches.append(RetrievedResult(source=source, score=score, text=text))

    matches.sort(key=lambda item: item.score, reverse=True)
    return matches[:top_k]
