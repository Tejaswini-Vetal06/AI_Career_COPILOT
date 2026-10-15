"""
Career Copilot AI - Automated Test Suite
Covers SQLite storage, resume parsing, bullet auditing, job matching,
gap prioritization, roadmap progress calculation, and job filtering.
"""

import pytest
import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.storage.database import (
    init_db, get_user_profile, update_user_profile, save_resume,
    get_active_resume, add_application, update_application, delete_application,
    get_all_applications, set_roadmap_task_status, get_roadmap_progress,
    log_activity, get_recent_activities
)
from modules.parsers.resume_parser import (
    extract_contact_info, extract_skills_from_text, analyze_bullet_points,
    calculate_resume_readiness
)
from modules.matching.matcher import (
    extract_skills_from_job_description, match_resume_to_job,
    compute_semantic_similarity
)
from modules.data.roles_data import ROLES_DATA, get_all_roles, get_role_titles
from modules.data.projects_data import get_projects_for_role
from modules.data.roadmap_data import get_roadmap_for_role, get_total_roadmap_tasks
from modules.jobs.job_service import filter_jobs, VERIFIED_TECH_JOBS


@pytest.fixture(autouse=True)
def setup_test_db():
    """Ensure database schema is ready before tests."""
    init_db()


def test_storage_user_profile():
    """Test reading and updating user profile."""
    p = get_user_profile()
    assert p is not None
    assert "target_role" in p

    update_user_profile(
        full_name="Jane Developer",
        email="jane.dev@example.com",
        headline="Senior AI Systems Engineer",
        target_role="AI Engineer",
        experience_level="Mid Level (2-5 yrs)",
        weekly_study_hours=15,
        summary="Specializing in RAG and Agentic LLM systems."
    )

    updated = get_user_profile()
    assert updated["full_name"] == "Jane Developer"
    assert updated["target_role"] == "AI Engineer"
    assert updated["weekly_study_hours"] == 15


def test_storage_application_tracker():
    """Test application CRUD operations."""
    app_id = add_application(
        company="DeepMind",
        role="Research Engineer",
        location="London / Remote",
        status="Applied",
        applied_date="2026-10-14",
        salary_range="$170k - $240k",
        notes="Applied with tailored RAG portfolio."
    )
    assert app_id > 0

    apps = get_all_applications(status_filter="Applied")
    assert any(a["company"] == "DeepMind" for a in apps)

    update_application(
        app_id=app_id,
        company="DeepMind",
        role="Research Engineer",
        location="London / Remote",
        status="Interview",
        applied_date="2026-10-14",
        follow_up_date="2026-10-20",
        salary_range="$170k - $240k",
        job_url="https://deepmind.google/careers",
        notes="First technical interview scheduled."
    )
    updated_apps = get_all_applications(status_filter="Interview")
    assert any(a["id"] == app_id for a in updated_apps)

    delete_application(app_id)
    post_delete = get_all_applications()
    assert not any(a["id"] == app_id for a in post_delete)


def test_resume_parser_contact_and_skills():
    """Test contact extraction and taxonomy skill matching."""
    sample_text = """
    Jane Doe | jane.doe@example.com | (555) 234-5678
    linkedin.com/in/janedoe | github.com/janedoe
    Technical Skills:
    Languages: Python, SQL, C++
    Frameworks: PyTorch, Scikit-Learn, FastAPI, LangChain
    Databases & Tools: PostgreSQL, Docker, Git, MLflow
    """
    contact = extract_contact_info(sample_text)
    assert contact["email"] == "jane.doe@example.com"
    assert contact["github"] == "github.com/janedoe"
    assert contact["linkedin"] == "linkedin.com/in/janedoe"

    skills = extract_skills_from_text(sample_text)
    prog_key = "Programming & Core CS" if "Programming & Core CS" in skills else "Programming Languages"
    assert prog_key in skills
    assert any(s.lower() == "python" for s in skills[prog_key])
    ai_key = "AI, ML & Data Science" if "AI, ML & Data Science" in skills else "AI & Machine Learning"
    assert ai_key in skills
    assert any(s.lower() == "pytorch" for s in skills[ai_key])


def test_bullet_point_quality_auditor():
    """Test detection of strong action verbs, metrics, and passive verbs."""
    text_with_bullets = """
    • Developed automated ETL pipeline reducing latency by 35% across 2M daily records.
    • Helped with website bugs and assisted team members.
    • Architected distributed Redis cache layer.
    """
    bullets = analyze_bullet_points(text_with_bullets)
    assert len(bullets) >= 2

    # Check strong bullet
    strong_b = next((b for b in bullets if "reducing latency by 35%" in b["original"]), None)
    assert strong_b is not None
    assert strong_b["status"] == "Strong"

    # Check weak bullet
    weak_b = next((b for b in bullets if "Helped with website" in b["original"]), None)
    assert weak_b is not None
    assert weak_b["status"] == "Weak"
    assert "Replace passive verb" in weak_b["suggested_rewrite"]


def test_job_description_matcher():
    """Test required vs preferred skill segmentation and score calculation."""
    resume_mock = {
        "raw_text": "Experienced Python and PyTorch engineer with FastAPI and Docker. Built production models.",
        "skills_categorized": {
            "Languages": ["Python"],
            "ML": ["PyTorch"],
            "Backend": ["FastAPI"],
            "DevOps": ["Docker"]
        }
    }

    jd_text = """
    Senior Machine Learning Engineer
    Requirements:
    - Python programming expertise.
    - Deep learning experience with PyTorch and Scikit-Learn.
    - Experience deploying with FastAPI.
    Preferred Qualifications:
    - Familiarity with Kubernetes and MLflow.
    - Docker containerization is a plus.
    """

    res = match_resume_to_job(resume_mock, jd_text, "Machine Learning Engineer")

    assert res["composite_score"] > 0
    assert "Python" in res["matched_required"]
    assert "Pytorch" in res["matched_required"] or "PyTorch" in res["matched_required"]
    assert "Scikit-Learn" in res["missing_required"]
    assert "Docker" in res["matched_preferred"]
    assert "formula_explanation" in res["score_breakdown"]


def test_all_9_career_roles_exist():
    """Verify all 9 mandated engineering career tracks exist with valid schemas."""
    expected_roles = [
        "AI Engineer",
        "Machine Learning Engineer",
        "NLP Engineer",
        "Data Scientist",
        "Data Analyst",
        "Python Software Engineer",
        "Backend Developer",
        "Generative AI Engineer",
        "MLOps Engineer"
    ]
    titles = get_role_titles()
    for role in expected_roles:
        assert role in titles
        role_data = ROLES_DATA[role]
        assert len(role_data["essential_skills"]) >= 5
        assert len(role_data["portfolio_projects"]) >= 1
        assert len(role_data["learning_topics"]) >= 4


def test_roadmap_persistence():
    """Verify interactive checkbox updates persist in SQLite database."""
    role = "AI Engineer"
    set_roadmap_task_status(role, week_id=1, task_id="ai_w1_t1", is_completed=True)
    set_roadmap_task_status(role, week_id=1, task_id="ai_w1_t2", is_completed=False)

    progress = get_roadmap_progress(role)
    assert progress.get("ai_w1_t1") is True
    assert progress.get("ai_w1_t2") is False


def test_job_opportunities_filter():
    """Verify filtering logic for verified tech job postings."""
    jobs = VERIFIED_TECH_JOBS
    filtered = filter_jobs(jobs, role_filter="Machine Learning Engineer")
    assert len(filtered) >= 1
    assert all(j["role_category"] == "Machine Learning Engineer" for j in filtered)

    # Search keyword filter
    kw_filtered = filter_jobs(jobs, keyword_search="Anthropic")
    assert len(kw_filtered) >= 1
    assert any(j["company"] == "Anthropic" for j in kw_filtered)


def test_rag_interview_coach_generation_and_eval():
    """Verify RAG interview question generation and STAR evaluation."""
    from modules.rag.interview_coach import RAGInterviewCoach

    resume_text = (
        "Built customer churn classification model in Scikit-Learn with 18% PR-AUC gain.\n"
        "Deployed FastAPI inference service with sub-30ms latency on Docker."
    )
    jd_text = (
        "Seeking Machine Learning Engineer proficient in Python, PyTorch, and FastAPI.\n"
        "Requirements: Experience with distributed systems and Kubernetes."
    )

    coach = RAGInterviewCoach(
        resume_text=resume_text,
        jd_text=jd_text,
        target_role="Machine Learning Engineer",
        matched_analysis={"missing_required": ["Kubernetes"], "demonstrated_skills": ["Python", "FastAPI"]}
    )

    questions = coach.generate_interview_questions()
    assert len(questions) >= 3

    # Check question types
    q_types = [q["type"] for q in questions]
    assert any("Resume Technical Deep-Dive" in t for t in q_types)
    assert any("Skill Gap" in t for t in q_types)
    assert any("Behavioral" in t for t in q_types)

    # Test STAR evaluation on strong response
    strong_ans = (
        "When our payment microservice experienced unexpected data drift, my task was to identify the root cause. "
        "I implemented automated drift telemetry in PyTorch and deployed an alerting threshold, reducing false alarms by 40%."
    )
    eval_res = coach.evaluate_candidate_answer(questions[0], strong_ans)
    assert eval_res["score"] >= 65
    assert "star_feedback" in eval_res
    assert len(eval_res["strengths"]) > 0


def test_bullet_point_improver_agent():
    """Verify LLM bullet point improver across multiple styles."""
    from modules.agent.bullet_improver import improve_bullet_point

    orig = "Worked on machine learning model and helped team."
    res_xyz = improve_bullet_point(orig, style="Google XYZ Formula", target_keywords=["PyTorch", "Docker"])
    assert "Engineered" in res_xyz["primary_recommendation"] or "driving" in res_xyz["primary_recommendation"]
    assert "PyTorch" in res_xyz["primary_recommendation"] or "Docker" in res_xyz["primary_recommendation"]

    res_concise = improve_bullet_point(orig, style="Executive Brevity & Action")
    assert len(res_concise["primary_recommendation"].split()) > 3


def test_fastapi_endpoints():
    """Verify FastAPI backend REST endpoints using TestClient."""
    from starlette.testclient import TestClient
    from api import app

    client = TestClient(app)

    # 1. Healthcheck
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["status"] == "online"

    # 2. Parse Resume
    resp = client.post("/api/resume/parse", json={"raw_text": "Email: test@example.com Python, Docker, PyTorch engineer."})
    assert resp.status_code == 200
    assert resp.json()["contact"]["email"] == "test@example.com"

    # 3. Job Match
    resp = client.post("/api/match", json={
        "resume_text": "Python and PyTorch developer with Docker experience.",
        "job_description": "We need Python, PyTorch, Kubernetes, and FastAPI.",
        "target_role": "Machine Learning Engineer"
    })
    assert resp.status_code == 200
    assert resp.json()["composite_score"] > 0

    # 4. Bullet Improve
    resp = client.post("/api/bullets/improve", json={
        "bullet_text": "Worked on data pipeline.",
        "style": "Google XYZ Formula"
    })
    assert resp.status_code == 200
    assert "primary_recommendation" in resp.json()

    # 5. Roles
    resp = client.get("/api/roles")
    assert resp.status_code == 200
    assert len(resp.json()["titles"]) >= 9

    # 6. Chatbot
    resp = client.post("/api/chatbot", json={"query": "Explain the STAR method", "target_role": "Machine Learning Engineer"})
    assert resp.status_code == 200
    assert "STAR" in resp.json()["response"]


def test_career_chatbot_logic():
    """Verify context-aware chatbot response generation."""
    from modules.agent.career_chatbot import get_chatbot_response

    # Test STAR query
    r1 = get_chatbot_response("Can you explain the STAR method?")
    assert "Situation" in r1 and "Result" in r1

    # Test tell me about yourself
    r2 = get_chatbot_response("How do I answer tell me about yourself?")
    assert "Present" in r2 and "Future" in r2

    # Test Naukri/LinkedIn advice
    r3 = get_chatbot_response("How do I get jobs on Naukri and LinkedIn?")
    assert "Naukri" in r3 and "LinkedIn" in r3


def test_platform_search_urls_generator():
    """Verify generation of deep search URLs for Naukri, LinkedIn, Indeed, and Google."""
    from modules.jobs.job_service import generate_platform_search_urls

    urls = generate_platform_search_urls("Machine Learning Engineer", "Bengaluru")
    assert "naukri.com" in urls["naukri"]
    assert "linkedin.com" in urls["linkedin"]
    assert "indeed.com" in urls["indeed"]
    assert "google.com" in urls["google"]


