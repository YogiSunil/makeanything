from __future__ import annotations

from textwrap import dedent

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from studyflow.orchestrator import run_pipeline

app = FastAPI(title="StudyFlow Coach", version="0.2.0")


class PlanRequest(BaseModel):
    prompt: str = Field(min_length=1)
    docs: list[str] = Field(default_factory=list)


class PlanResponse(BaseModel):
    checklist: list[str]
    citations: list[str]
    used_fallback: bool
    confidence: float
    weak_context: bool
    is_valid: bool
    issues: list[str]


def _parse_docs(lines: list[str]) -> dict[str, str]:
    docs: dict[str, str] = {}
    for line in lines:
        raw = line.strip()
        if not raw or "::" not in raw:
            continue
        source, text = raw.split("::", 1)
        docs[source.strip()] = text.strip()
    return docs


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return dedent(
        """
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <title>StudyFlow Coach Studio</title>
          <style>
            @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=IBM+Plex+Mono:wght@400;600&display=swap');

            :root {
              --ink: #17202a;
              --bg-a: #f8f4ea;
              --bg-b: #e9f4f0;
              --card: #fffdf8;
              --accent: #c45a2a;
              --accent-soft: #ffe3d4;
              --ok: #1f6f3d;
              --bad: #9f2f2f;
              --border: #eadfcb;
              --mono: "IBM Plex Mono", monospace;
              --sans: "Manrope", "Segoe UI", sans-serif;
            }

            * { box-sizing: border-box; }

            body {
              margin: 0;
              font-family: var(--sans);
              color: var(--ink);
              background:
                radial-gradient(circle at 8% 5%, #ffd8b8 0, transparent 30%),
                radial-gradient(circle at 90% 85%, #d2ebdf 0, transparent 35%),
                linear-gradient(145deg, var(--bg-a), var(--bg-b));
              min-height: 100vh;
            }

            .shell {
              max-width: 1050px;
              margin: 0 auto;
              padding: 2.2rem 1.2rem 2.8rem;
              animation: fadeIn 0.45s ease;
            }

            .hero {
              border: 1px solid var(--border);
              border-radius: 20px;
              background: linear-gradient(130deg, #fff5e9, #f6fff9);
              padding: 1.4rem;
              box-shadow: 0 10px 30px rgba(23, 32, 42, 0.07);
            }

            .kicker {
              font-size: 0.75rem;
              text-transform: uppercase;
              letter-spacing: 0.14em;
              font-weight: 700;
              color: var(--accent);
              margin-bottom: 0.2rem;
            }

            h1 {
              font-size: clamp(1.8rem, 3.4vw, 2.8rem);
              margin: 0;
              line-height: 1.1;
            }

            .sub {
              margin-top: 0.65rem;
              margin-bottom: 0;
              max-width: 60ch;
              color: #34495e;
            }

            .grid {
              display: grid;
              grid-template-columns: 1fr 1fr;
              gap: 1rem;
              margin-top: 1rem;
            }

            .card {
              border: 1px solid var(--border);
              border-radius: 16px;
              background: var(--card);
              padding: 1rem;
              box-shadow: 0 8px 18px rgba(23, 32, 42, 0.06);
            }

            label {
              display: block;
              font-size: 0.8rem;
              text-transform: uppercase;
              letter-spacing: 0.12em;
              font-weight: 700;
              color: #6f4b39;
              margin-bottom: 0.5rem;
            }

            textarea {
              width: 100%;
              border: 1px solid #dccfb6;
              border-radius: 12px;
              padding: 0.75rem;
              font-family: var(--sans);
              font-size: 0.95rem;
              resize: vertical;
              background: #fffefb;
              color: var(--ink);
            }

            .hint {
              font-family: var(--mono);
              font-size: 0.78rem;
              color: #54606f;
              margin-top: 0.5rem;
            }

            .actions {
              margin-top: 0.9rem;
              display: flex;
              align-items: center;
              gap: 0.7rem;
            }

            .sample-actions {
              margin-top: 0.75rem;
              display: flex;
              flex-wrap: wrap;
              gap: 0.45rem;
            }

            button {
              border: 0;
              border-radius: 12px;
              padding: 0.75rem 1.05rem;
              font-family: var(--sans);
              font-weight: 700;
              background: var(--accent);
              color: #fff;
              cursor: pointer;
            }

            button:hover { filter: brightness(1.06); }
            button:disabled { opacity: 0.7; cursor: wait; }

            .sample-btn {
              padding: 0.45rem 0.65rem;
              font-size: 0.82rem;
              background: #2f5d8c;
            }

            .status {
              font-family: var(--mono);
              font-size: 0.85rem;
              color: #44515f;
            }

            .output h2 {
              margin-top: 0;
              margin-bottom: 0.7rem;
              font-size: 1.05rem;
            }

            .meta-row {
              display: flex;
              flex-wrap: wrap;
              align-items: center;
              gap: 0.45rem;
              margin-bottom: 0.7rem;
            }

            ol, ul {
              margin: 0;
              padding-left: 1.1rem;
            }

            li + li { margin-top: 0.34rem; }

            .pill {
              display: inline-block;
              font-family: var(--mono);
              font-size: 0.74rem;
              padding: 0.24rem 0.5rem;
              border-radius: 999px;
            }

            .confidence-pill {
              background: #e9eef7;
              color: #294569;
            }

            .ok { background: #d9f0df; color: var(--ok); }
            .bad { background: #f8dada; color: var(--bad); }

            .warning {
              border: 1px solid #efb7a7;
              background: #fff1ec;
              color: #8a3524;
              border-radius: 12px;
              padding: 0.55rem 0.7rem;
              font-size: 0.86rem;
              margin-bottom: 0.75rem;
            }

            .hide { display: none; }

            @media (max-width: 880px) {
              .grid { grid-template-columns: 1fr; }
            }

            @keyframes fadeIn {
              from { opacity: 0; transform: translateY(8px); }
              to { opacity: 1; transform: translateY(0); }
            }
          </style>
        </head>
        <body>
          <main class="shell">
            <section class="hero">
              <div class="kicker">StudyFlow Coach</div>
              <h1>Planning Studio</h1>
              <p class="sub">
                Turn one assignment prompt into a citation-backed checklist, then run an automatic review pass before execution.
              </p>
            </section>

            <section class="grid" style="margin-top: 1rem;">
              <article class="card">
                <label for="prompt">Assignment Prompt</label>
                <textarea id="prompt" rows="4" placeholder="Example: Plan my final AI engineering project submission."></textarea>

                <label for="docs" style="margin-top: 0.8rem;">Context Docs</label>
                <textarea id="docs" rows="7" placeholder="proposal.md::Build retrieval planner and collect evidence\nspec.md::Return at least 5 tasks with fallback"></textarea>
                <div class="hint">One line per source in source::text format.</div>

                <div class="sample-actions">
                  <button id="sample-final" class="sample-btn" type="button">Load Final Project Sample</button>
                  <button id="sample-exam" class="sample-btn" type="button">Load Exam Week Sample</button>
                </div>

                <div class="actions">
                  <button id="run">Generate Plan</button>
                  <span id="status" class="status">Ready.</span>
                </div>
              </article>

              <article class="card output">
                <h2>Plan Output</h2>
                <div class="meta-row">
                  <div id="review-pill" class="pill hide"></div>
                  <div id="confidence-pill" class="pill confidence-pill hide"></div>
                </div>
                <div id="context-warning" class="warning hide"></div>
                <ol id="plan-items"></ol>

                <h2 style="margin-top: 1rem;">Citations</h2>
                <ul id="citation-items"></ul>

                <h2 style="margin-top: 1rem;">Review Issues</h2>
                <ul id="issue-items"></ul>
              </article>
            </section>
          </main>

          <script>
            const runBtn = document.getElementById("run");
            const statusEl = document.getElementById("status");
            const promptEl = document.getElementById("prompt");
            const docsEl = document.getElementById("docs");
            const planEl = document.getElementById("plan-items");
            const citeEl = document.getElementById("citation-items");
            const issueEl = document.getElementById("issue-items");
            const pillEl = document.getElementById("review-pill");
            const confidenceEl = document.getElementById("confidence-pill");
            const warningEl = document.getElementById("context-warning");
            const sampleFinalBtn = document.getElementById("sample-final");
            const sampleExamBtn = document.getElementById("sample-exam");

            function loadSample(type) {
              if (type === "final") {
                promptEl.value = "Plan my final AI engineering project submission this week.";
                docsEl.value = [
                  "proposal.md::Build one retrieval-backed component and capture proof of concept notes.",
                  "spec.md::Return at least 5 tasks with fallback when context is weak.",
                  "tutorial3-checklist.md::Confirm architecture.md and poc-notes.md are complete before submission."
                ].join("\\n");
                statusEl.textContent = "Loaded final project sample.";
                return;
              }

              promptEl.value = "Help me plan exam week study and assignment deadlines.";
              docsEl.value = [
                "schedule.md::Math exam Tuesday, systems quiz Thursday, project report Friday.",
                "rubric.md::Include at least one review checkpoint and risk note per deliverable.",
                "notes.md::Prefer two focused work blocks daily and one nightly recap."
              ].join("\\n");
              statusEl.textContent = "Loaded exam week sample.";
            }

            function renderList(target, values) {
              target.innerHTML = "";
              if (!values.length) {
                const item = document.createElement("li");
                item.textContent = "None";
                target.appendChild(item);
                return;
              }
              for (const value of values) {
                const item = document.createElement("li");
                item.textContent = value;
                target.appendChild(item);
              }
            }

            async function runPlanner() {
              const prompt = promptEl.value.trim();
              const docs = docsEl.value
                .split("\n")
                .map(line => line.trim())
                .filter(Boolean);

              if (!prompt) {
                statusEl.textContent = "Add a prompt first.";
                return;
              }

              runBtn.disabled = true;
              statusEl.textContent = "Running pipeline...";

              try {
                const res = await fetch("/api/plan", {
                  method: "POST",
                  headers: { "Content-Type": "application/json" },
                  body: JSON.stringify({ prompt, docs }),
                });

                if (!res.ok) {
                  throw new Error("Request failed");
                }

                const data = await res.json();
                renderList(planEl, data.checklist);
                renderList(citeEl, data.citations);
                renderList(issueEl, data.issues);

                pillEl.classList.remove("hide", "ok", "bad");
                if (data.is_valid) {
                  pillEl.classList.add("ok");
                  pillEl.textContent = "Review: Valid";
                } else {
                  pillEl.classList.add("bad");
                  pillEl.textContent = "Review: Needs fixes";
                }

                const confidencePct = Math.round((data.confidence || 0) * 100);
                confidenceEl.classList.remove("hide");
                confidenceEl.textContent = `Confidence: ${confidencePct}%`;

                warningEl.classList.add("hide");
                warningEl.textContent = "";
                if (data.weak_context) {
                  warningEl.classList.remove("hide");
                  warningEl.textContent = "Weak context detected. Add richer or more specific docs to improve guidance quality.";
                }

                statusEl.textContent = data.weak_context
                  ? `Completed with weak context (${confidencePct}% confidence).`
                  : `Completed with solid context (${confidencePct}% confidence).`;
              } catch (err) {
                statusEl.textContent = "Pipeline failed. Try again.";
              } finally {
                runBtn.disabled = false;
              }
            }

            runBtn.addEventListener("click", runPlanner);
            sampleFinalBtn.addEventListener("click", () => loadSample("final"));
            sampleExamBtn.addEventListener("click", () => loadSample("exam"));
          </script>
        </body>
        </html>
        """
    )


@app.post("/api/plan", response_model=PlanResponse)
def api_plan(payload: PlanRequest) -> PlanResponse:
    docs = _parse_docs(payload.docs)
    result = run_pipeline(payload.prompt, docs)
    return PlanResponse(
        checklist=result.plan.checklist,
        citations=result.plan.citations,
        used_fallback=result.plan.used_fallback,
      confidence=result.confidence,
      weak_context=result.weak_context,
        is_valid=result.review.is_valid,
        issues=result.review.issues,
    )
