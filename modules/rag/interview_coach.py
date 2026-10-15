"""
Career Copilot AI - RAG Interview Coach
Uses Retrieval-Augmented Generation over the candidate's resume and target job description
to generate personalized, highly contextual interview questions and evaluate candidate responses.
"""

import re
from typing import Dict, Any, List, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RAGInterviewCoach:
    """RAG-powered interview generation and evaluation engine."""

    def __init__(self, resume_text: str, jd_text: str, target_role: str,
                 resume_data: Optional[Dict[str, Any]] = None,
                 matched_analysis: Optional[Dict[str, Any]] = None):
        self.resume_text = resume_text
        self.jd_text = jd_text
        self.target_role = target_role
        self.resume_data = resume_data or {}
        self.matched_analysis = matched_analysis or {}
        self.chunks = self._build_document_chunks()

    def _build_document_chunks(self) -> List[Dict[str, str]]:
        """Chunk resume and job description into structured semantic passages."""
        chunks = []

        # 1. Resume Bullets / Projects
        lines = [l.strip() for l in self.resume_text.split("\n") if l.strip()]
        for line in lines:
            if len(line) > 30 and (line.startswith("•") or line.startswith("-") or "developed" in line.lower() or "engineered" in line.lower() or "built" in line.lower()):
                clean = re.sub(r"^[-*•]\s*", "", line)
                chunks.append({"source": "resume", "category": "experience", "text": clean})

        # 2. Job Description Requirements
        jd_lines = [l.strip() for l in self.jd_text.replace(";", "\n").split("\n") if l.strip()]
        for line in jd_lines:
            if len(line) > 20 and any(k in line.lower() for k in ["experience", "knowledge", "ability", "proficient", "requirements", "skills"]):
                chunks.append({"source": "job_description", "category": "requirement", "text": line})

        # Fallback if too few chunks
        if len(chunks) < 3:
            chunks.append({"source": "resume", "category": "experience", "text": self.resume_text[:400]})
            chunks.append({"source": "job_description", "category": "requirement", "text": self.jd_text[:400]})

        return chunks

    def retrieve_context(self, query: str, top_k: int = 2) -> List[Dict[str, str]]:
        """Retrieve most relevant chunks for a specific prompt query via TF-IDF cosine similarity."""
        if not self.chunks:
            return []

        corpus = [c["text"] for c in self.chunks]
        try:
            vectorizer = TfidfVectorizer(stop_words="english")
            matrix = vectorizer.fit_transform(corpus + [query])
            sims = cosine_similarity(matrix[-1:], matrix[:-1])[0]
            top_indices = sims.argsort()[-top_k:][::-1]
            return [self.chunks[i] for i in top_indices if sims[i] > 0.05]
        except Exception:
            return self.chunks[:top_k]

    def generate_interview_questions(self) -> List[Dict[str, Any]]:
        """Generate targeted interview questions based on resume evidence and job gaps."""
        questions = []

        # 1. Technical Deep-Dive on Candidate's Strongest Project / Experience
        resume_chunks = [c for c in self.chunks if c["source"] == "resume"]
        best_resume_chunk = resume_chunks[0]["text"] if resume_chunks else "your recent machine learning project"

        q1 = {
            "id": "rag_q_1",
            "type": "Resume Technical Deep-Dive",
            "question": (
                f"On your resume, you highlighted: '{best_resume_chunk[:140]}...'. "
                f"Can you walk through the system architecture, how you chose the underlying algorithms, "
                f"and how you validated performance against latency or data drift constraints?"
            ),
            "context_retrieved": best_resume_chunk,
            "evaluation_focus": "Technical depth, architectural tradeoffs, metric justification, and failure modes.",
            "sample_answer_guide": (
                "Structure your answer with: 1) Problem context & baseline, 2) Technical design decisions & algorithms, "
                "3) Specific metrics achieved (e.g. 18% PR-AUC gain, sub-30ms latency), and 4) Production tradeoffs."
            )
        }
        questions.append(q1)

        # 2. Skill-Gap Probing Question
        missing_skills = self.matched_analysis.get("missing_required", [])
        if not missing_skills:
            missing_skills = self.matched_analysis.get("missing_preferred", [])
        probe_skill = missing_skills[0] if missing_skills else "Kubernetes / Scalable Deployment"

        demonstrated_skills = self.matched_analysis.get("demonstrated_skills", ["Python", "FastAPI"])
        anchor_skill = demonstrated_skills[0] if demonstrated_skills else "Python"

        q2 = {
            "id": "rag_q_2",
            "type": "Skill Gap & Applied Scenario",
            "question": (
                f"This target position requires practical proficiency in {probe_skill}. "
                f"Given your strong foundation in {anchor_skill}, how would you architect an end-to-end service "
                f"incorporating {probe_skill} for high-availability production workloads?"
            ),
            "context_retrieved": f"Target Job Requirement: {probe_skill} | Candidate Baseline: {anchor_skill}",
            "evaluation_focus": "Transferable knowledge, conceptual understanding of required tool, and proactive learning ability.",
            "sample_answer_guide": (
                f"Acknowledge where your hands-on experience started (e.g. {anchor_skill}), then demonstrate conceptual "
                f"mastery of {probe_skill} by describing its core primitives (e.g. cluster orchestration, state management, or isolation)."
            )
        }
        questions.append(q2)

        # 3. Behavioral / High-Stakes Incident (STAR Method)
        q3 = {
            "id": "rag_q_3",
            "type": "Behavioral & Incident Response (STAR)",
            "question": (
                f"Describe a situation in your engineering journey where a model or software service failed in testing "
                f"or produced unexpected outputs under time pressure. How did you diagnose the root cause, communicate with "
                f"collaborators, and implement a permanent safeguard?"
            ),
            "context_retrieved": "Evaluation Schema: STAR (Situation, Task, Action, Result) + Engineering Accountability",
            "evaluation_focus": "Systematic debugging, cross-functional communication, composure under pressure, and post-mortem safeguards.",
            "sample_answer_guide": (
                "Use the STAR format: Briefly set the Situation, clarify your specific Task, detail your debugging Actions "
                "(profiling, unit tests, rollback), and quantify the final Result with the preventative monitoring added."
            )
        }
        questions.append(q3)

        # 4. Systems Design & Scalability
        q4 = {
            "id": "rag_q_4",
            "type": "Systems Design & Scale",
            "question": (
                f"If you were tasked with scaling your current {self.target_role} pipeline to handle 100x the data volume "
                f"or 1,000 concurrent requests per second, where would the primary bottlenecks emerge (CPU, GPU memory, network I/O, database locks), "
                f"and how would you re-architect it?"
            ),
            "context_retrieved": f"Target Role: {self.target_role} | Scalability Dimension: 100x Concurrency",
            "evaluation_focus": "Bottleneck identification, caching strategies (Redis), asynchronous queues (Celery/Kafka), and horizontal scaling.",
            "sample_answer_guide": (
                "Deconstruct the request flow: 1) Ingress rate-limiting, 2) Async decoupled queues to prevent memory blowup, "
                "3) Distributed caching, 4) Batching inference on worker pods."
            )
        }
        questions.append(q4)

        return questions

    def evaluate_candidate_answer(self, question_item: Dict[str, Any], candidate_answer: str) -> Dict[str, Any]:
        """Evaluate a candidate's answer against STAR criteria, technical specificity, and metrics."""
        text = candidate_answer.strip()
        text_lower = text.lower()

        if len(text) < 40:
            return {
                "score": 35,
                "verdict": "Needs Expansion",
                "star_feedback": {
                    "situation": "Missing context",
                    "task": "Missing problem definition",
                    "action": "Insufficient detail on what you specifically built or resolved",
                    "result": "No quantifiable outcome or business impact"
                },
                "strengths": ["Submitted an initial response."],
                "improvements": ["Your answer is too brief for an engineering interview. Elaborate on the technical steps and quantifiable results."],
                "model_answer": question_item.get("sample_answer_guide", "")
            }

        score = 50
        strengths = []
        improvements = []

        # Check STAR Components
        has_situation = any(k in text_lower for k in ["when", "during", "at", "project", "scenario", "while", "working on"])
        has_task = any(k in text_lower for k in ["goal", "task", "objective", "needed to", "required", "responsible for"])
        has_action = any(k in text_lower for k in ["implemented", "built", "designed", "used", "created", "refactored", "analyzed", "investigated"])
        has_result = any(k in text_lower for k in ["reduced", "increased", "improved", "resulting", "achieved", "learned", "prevented", "%", "ms"])

        if has_situation and has_task:
            score += 15
            strengths.append("Clearly established the background situation and the technical objective.")
        else:
            improvements.append("Set the stage faster: state the initial problem and what your specific role was.")

        if has_action:
            score += 20
            strengths.append("Described concrete engineering actions and tools used.")
        else:
            improvements.append("Detail the exact technical steps, algorithms, or tools you selected.")

        # Metric detection
        has_metric = bool(re.search(r"(\d+%\b|\$\d+|\b\d+\s*(ms|seconds|hours|users|records|x)\b|\b\d{2,}\b)", text_lower))
        if has_metric or has_result:
            score += 15
            strengths.append("Provided a measurable outcome or tangible result.")
        else:
            improvements.append("Quantify the result: How much faster did it run? Did accuracy or reliability improve?")

        # Check technical depth
        tech_words = ["python", "pytorch", "fastapi", "docker", "sql", "cache", "latency", "pipeline", "model", "test", "api"]
        tech_count = sum(1 for w in tech_words if w in text_lower)
        if tech_count >= 3:
            score = min(score + 10, 95)
            strengths.append("Demonstrated good engineering vocabulary and domain terminology.")

        verdict = "Excellent" if score >= 80 else ("Strong" if score >= 65 else "Acceptable")

        return {
            "score": score,
            "verdict": verdict,
            "star_feedback": {
                "situation": "Present" if has_situation else "Needs clearer context",
                "task": "Present" if has_task else "Could be more explicit",
                "action": "Well explained" if has_action else "Needs more technical depth",
                "result": "Quantified" if has_metric else "Needs measurable impact"
            },
            "strengths": strengths,
            "improvements": improvements,
            "model_answer": question_item.get("sample_answer_guide", "")
        }
