"""
Career Copilot AI - Production FastAPI Backend Microservice
Provides RESTful endpoints for:
- Resume parsing & taxonomy extraction
- Job matching & skill gap diagnosis
- LLM-powered bullet point optimization
- RAG-powered interview question generation & STAR evaluation
- Application pipeline management
Interactive Swagger documentation available at: /docs
"""

from fastapi import FastAPI, HTTPException, Query, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

from modules.storage.database import (
    init_db, get_user_profile, get_all_applications, add_application,
    get_application_counts, get_active_resume
)
from modules.parsers.resume_parser import (
    parse_resume_complete, extract_contact_info, extract_skills_from_text,
    analyze_bullet_points, calculate_resume_readiness
)
from modules.matching.matcher import match_resume_to_job
from modules.agent.bullet_improver import improve_bullet_point
from modules.rag.interview_coach import RAGInterviewCoach
from modules.data.roles_data import ROLES_DATA, get_all_roles, get_role_titles
from modules.jobs.job_service import fetch_live_remote_jobs, filter_jobs

# Initialize database
init_db()

# Initialize FastAPI application
app = FastAPI(
    title="Career Copilot AI — API",
    description="Production-grade AI backend providing resume parsing, job matching, RAG interview coaching, and career tracking.",
    version="2.0.0"
)

# Enable CORS for external frontend or microservice integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------- PYDANTIC REQUEST & RESPONSE MODELS ----------------- #

class ResumeParseTextRequest(BaseModel):
    raw_text: str = Field(..., description="Plain text extracted from resume")
    filename: Optional[str] = "resume.txt"

class JobMatchRequest(BaseModel):
    resume_text: str = Field(..., description="Full text of candidate's resume")
    job_description: str = Field(..., description="Target job description text")
    target_role: Optional[str] = "Machine Learning Engineer"

class BulletImproveRequest(BaseModel):
    bullet_text: str = Field(..., description="Original resume bullet point to refine")
    style: Optional[str] = Field("Google XYZ Formula", description="Style: 'Google XYZ Formula', 'Senior Engineering & Scalability', 'Job-Targeted Keyword Alignment', 'Executive Brevity & Action'")
    target_role: Optional[str] = "Machine Learning Engineer"
    target_keywords: Optional[List[str]] = None

class InterviewQuestionsRequest(BaseModel):
    resume_text: str = Field(..., description="Candidate's resume text")
    job_description: str = Field(..., description="Target job description")
    target_role: Optional[str] = "Machine Learning Engineer"

class InterviewEvaluateRequest(BaseModel):
    question: str = Field(..., description="Interview question text")
    question_type: Optional[str] = "Technical Deep-Dive"
    candidate_answer: str = Field(..., description="Answer provided by candidate")
    sample_answer_guide: Optional[str] = ""

class ChatbotQueryRequest(BaseModel):
    query: str = Field(..., description="User query about resume, roadmap, interview, or job search")
    target_role: Optional[str] = "Machine Learning Engineer"

class ApplicationCreateSchema(BaseModel):
    company: str
    role: str
    location: Optional[str] = "Remote"
    status: str = "Interested"
    applied_date: Optional[str] = None
    follow_up_date: Optional[str] = None
    salary_range: Optional[str] = ""
    job_url: Optional[str] = ""
    notes: Optional[str] = ""


# ----------------- API ENDPOINTS ----------------- #

@app.get("/")
def root():
    """Health check and API metadata endpoint."""
    return {
        "service": "Career Copilot AI API",
        "version": "2.0.0",
        "status": "online",
        "documentation": "/docs"
    }


@app.post("/api/resume/parse")
def parse_resume_text(req: ResumeParseTextRequest):
    """Parse resume text, extracting contact info, skills taxonomy, and bullet quality metrics."""
    text = req.raw_text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Empty resume text provided.")

    contact = extract_contact_info(text)
    skills = extract_skills_from_text(text)
    bullets = analyze_bullet_points(text)
    score, strengths, improvements = calculate_resume_readiness(contact, skills, {}, bullets)

    return {
        "filename": req.filename,
        "readiness_score": score,
        "contact": contact,
        "skills_categorized": skills,
        "bullet_points_audited": bullets,
        "strengths": strengths,
        "improvements": improvements
    }


@app.post("/api/match")
def match_job(req: JobMatchRequest):
    """Compare resume against target job description and calculate transparent match coverage."""
    resume_data = {
        "raw_text": req.resume_text,
        "skills_categorized": extract_skills_from_text(req.resume_text)
    }
    match_result = match_resume_to_job(
        resume_data=resume_data,
        jd_text=req.job_description,
        target_role=req.target_role or "Machine Learning Engineer"
    )
    return match_result


@app.post("/api/bullets/improve")
def improve_bullet(req: BulletImproveRequest):
    """Optimize resume bullet point using Google XYZ, Senior Engineering, or Keyword Infusion styles."""
    result = improve_bullet_point(
        bullet_text=req.bullet_text,
        style=req.style or "Google XYZ Formula",
        target_role=req.target_role or "Machine Learning Engineer",
        target_keywords=req.target_keywords
    )
    return result


@app.post("/api/interview/questions")
def generate_interview_questions(req: InterviewQuestionsRequest):
    """Generate personalized RAG interview questions grounded in candidate's resume and job gaps."""
    coach = RAGInterviewCoach(
        resume_text=req.resume_text,
        jd_text=req.job_description,
        target_role=req.target_role or "Machine Learning Engineer"
    )
    questions = coach.generate_interview_questions()
    return {
        "target_role": req.target_role,
        "total_questions": len(questions),
        "questions": questions
    }


@app.post("/api/interview/evaluate")
def evaluate_interview_answer(req: InterviewEvaluateRequest):
    """Evaluate candidate interview response using STAR criteria, metrics, and engineering depth."""
    coach = RAGInterviewCoach(resume_text="", jd_text="", target_role="")
    dummy_q = {
        "question": req.question,
        "type": req.question_type,
        "sample_answer_guide": req.sample_answer_guide
    }
    evaluation = coach.evaluate_candidate_answer(dummy_q, req.candidate_answer)
    return evaluation


@app.post("/api/chatbot")
def chat_with_copilot(req: ChatbotQueryRequest):
    """AI Career Chatbot answering questions regarding resume, study roadmaps, interview prep, and platforms."""
    from modules.agent.career_chatbot import get_chatbot_response
    active = get_active_resume()
    response = get_chatbot_response(
        user_query=req.query,
        active_resume=active,
        target_role=req.target_role or "Machine Learning Engineer"
    )
    return {"query": req.query, "response": response}


@app.get("/api/applications")
def list_applications(status: Optional[str] = Query(None, description="Optional filter by status")):
    """List tracked job applications from SQLite database."""
    apps = get_all_applications(status_filter=status)
    counts = get_application_counts()
    return {
        "counts": counts,
        "applications": apps
    }


@app.post("/api/applications")
def create_application(app_data: ApplicationCreateSchema):
    """Record a new application in the tracker."""
    app_id = add_application(
        company=app_data.company,
        role=app_data.role,
        location=app_data.location or "Remote",
        status=app_data.status,
        applied_date=app_data.applied_date,
        follow_up_date=app_data.follow_up_date,
        salary_range=app_data.salary_range or "",
        job_url=app_data.job_url or "",
        notes=app_data.notes or ""
    )
    return {"message": "Application created successfully", "id": app_id}


@app.get("/api/roles")
def list_roles():
    """Retrieve all 9 curated engineering career tracks."""
    return {
        "roles": get_all_roles(),
        "titles": get_role_titles()
    }


@app.get("/api/jobs")
def search_jobs(role: Optional[str] = "All", workplace: Optional[str] = "All", keyword: Optional[str] = ""):
    """Fetch verified live jobs from Remotive API and curated corporate portals."""
    all_jobs = fetch_live_remote_jobs()
    filtered = filter_jobs(all_jobs, role_filter=role, workplace_filter=workplace, keyword_search=keyword)
    return {
        "total": len(filtered),
        "jobs": filtered
    }
