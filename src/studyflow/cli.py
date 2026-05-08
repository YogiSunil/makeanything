from __future__ import annotations

import argparse
from typing import Sequence

from studyflow.orchestrator import run_pipeline


def _parse_docs_arg(raw_docs: str) -> dict[str, str]:
    docs: dict[str, str] = {}
    if not raw_docs:
        return docs

    for item in raw_docs.split("||"):
        if "::" not in item:
            continue
        source, text = item.split("::", 1)
        docs[source.strip()] = text.strip()
    return docs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="StudyFlow Coach CLI")
    parser.add_argument("prompt", help="Planning prompt")
    parser.add_argument(
        "--docs",
        default="",
        help="Inline docs as 'source::text' entries separated by '||'",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    docs = _parse_docs_arg(args.docs)
    result = run_pipeline(args.prompt, docs)

    print("StudyFlow Plan")
    print("=============")
    for idx, item in enumerate(result.plan.checklist, start=1):
        print(f"{idx}. {item}")

    print("\nReview")
    print("======")
    print(f"Valid: {result.review.is_valid}")
    if result.review.issues:
        for issue in result.review.issues:
            print(f"- {issue}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
