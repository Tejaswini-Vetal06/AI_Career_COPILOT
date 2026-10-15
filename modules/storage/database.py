"""
Career Copilot AI - SQLite Database Storage
Provides persistence for user profiles, parsed resumes, job analyses,
roadmap milestones, applications tracker, and audit activity logs.
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")
DB_PATH = os.path.join(DB_DIR, "career_copilot.db")


def get_db_connection() -> sqlite3.Connection:
    """Return an open SQLite database connection with row factory enabled."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database tables with appropriate schemas and indexes."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # User Profile table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY,
            full_name TEXT DEFAULT 'Alex Mercer',
            email TEXT DEFAULT 'alex.mercer@example.com',
            headline TEXT DEFAULT 'Aspiring AI / ML Engineer',
            target_role TEXT DEFAULT 'Machine Learning Engineer',
            experience_level TEXT DEFAULT 'Entry Level (0-2 yrs)',
            weekly_study_hours INTEGER DEFAULT 12,
            summary TEXT DEFAULT 'Engineering graduate focused on building scalable machine learning systems and intelligent applications.',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Resumes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            file_size_kb REAL NOT NULL,
            raw_text TEXT NOT NULL,
            extracted_data_json TEXT NOT NULL,
            readiness_score INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Job Matches / Analyses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company_name TEXT DEFAULT '',
            job_description TEXT NOT NULL,
            target_role TEXT NOT NULL,
            match_score REAL NOT NULL,
            analysis_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Roadmap Progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roadmap_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_id TEXT NOT NULL,
            week_id INTEGER NOT NULL,
            task_id TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(role_id, task_id)
        )
    """)

    # Applications Tracker table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            location TEXT DEFAULT 'Remote',
            status TEXT NOT NULL CHECK(status IN ('Interested', 'To Apply', 'Applied', 'Interview', 'Offer', 'Rejected')),
            applied_date TEXT,
            follow_up_date TEXT,
            salary_range TEXT DEFAULT '',
            job_url TEXT DEFAULT '',
            notes TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Activity Logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_type TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            badge_color TEXT DEFAULT 'sky',
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Ensure default user profile exists
    cursor.execute("SELECT COUNT(*) FROM user_profiles WHERE id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO user_profiles (id, full_name, email, headline, target_role, experience_level, weekly_study_hours, summary)
            VALUES (1, 'Alex Mercer', 'alex.mercer@example.com', 'Aspiring AI / ML Engineer', 'Machine Learning Engineer', 'Entry Level (0-2 yrs)', 12, 'Engineering graduate focused on building scalable machine learning systems and intelligent applications.')
        """)

    # Seed initial authentic sample resume if empty
    cursor.execute("SELECT COUNT(*) FROM resumes")
    if cursor.fetchone()[0] == 0:
        sample_path = os.path.join(DB_DIR, "sample_engineering_resume.docx")
        if os.path.exists(sample_path):
            try:
                from modules.parsers.resume_parser import parse_resume_complete
                with open(sample_path, "rb") as sf:
                    file_bytes = sf.read()
                parsed = parse_resume_complete(file_bytes, "sample_engineering_resume.docx")
                if "error" not in parsed:
                    cursor.execute("""
                        INSERT INTO resumes (file_name, file_size_kb, raw_text, extracted_data_json, readiness_score, is_active)
                        VALUES (?, ?, ?, ?, ?, 1)
                    """, (parsed["file_name"], parsed["file_size_kb"], parsed["raw_text"], json.dumps(parsed), parsed["readiness_score"]))
            except Exception:
                pass

    # Seed initial job match analysis if empty
    cursor.execute("SELECT COUNT(*) FROM job_analyses")
    if cursor.fetchone()[0] == 0:
        sample_jd = (
            "We are seeking a Machine Learning Engineer to design, build, and deploy predictive systems.\n\n"
            "Requirements:\n"
            "- Strong programming proficiency in Python and SQL.\n"
            "- Hands-on experience with PyTorch or TensorFlow, and Scikit-Learn.\n"
            "- Experience building and consuming RESTful APIs with FastAPI.\n"
            "- Practical knowledge of Docker containerization and Git workflows.\n\n"
            "Preferred Qualifications:\n"
            "- Experience with MLflow or Weights & Biases for experiment tracking.\n"
            "- Familiarity with Kubernetes and cloud environments (AWS/GCP)."
        )
        sample_match = {
            "target_role": "Machine Learning Engineer",
            "composite_score": 78.5,
            "score_breakdown": {
                "required_coverage_pct": 85.0,
                "preferred_coverage_pct": 60.0,
                "semantic_relevance_pct": 74.0,
                "formula_explanation": "Composite score = (50% x Required Skill Coverage) + (20% x Preferred Skill Coverage) + (30% x Semantic Context)."
            },
            "required_skills": ["Docker", "FastAPI", "Git", "Python", "PyTorch", "Scikit-Learn", "SQL"],
            "preferred_skills": ["AWS", "GCP", "Kubernetes", "MLflow"],
            "matched_required": ["Docker", "FastAPI", "Git", "Python", "PyTorch", "Scikit-Learn", "SQL"],
            "missing_required": [],
            "matched_preferred": ["AWS", "MLflow"],
            "missing_preferred": ["GCP", "Kubernetes"],
            "demonstrated_skills": ["AWS", "Docker", "FastAPI", "Git", "MLflow", "Python", "PyTorch", "Scikit-Learn", "SQL"],
            "to_improve_skills": ["FastAPI", "MLflow"],
            "not_demonstrated_skills": ["GCP", "Kubernetes"],
            "prioritized_gaps": [
                {
                    "skill": "Kubernetes",
                    "priority": "Medium (Preferred)",
                    "status": "Not Demonstrated",
                    "why_matters": "Standard container orchestration platform for resilient distributed applications and GPU workloads.",
                    "resource": "Kubernetes Interactive Tutorials & kubectl Cheat Sheet",
                    "resource_url": "https://kubernetes.io/docs/tutorials/",
                    "exercise": "Deploy a containerized service with Deployment, Service (ClusterIP), and Ingress configurations.",
                    "project": "Kubernetes cluster configuration with Horizontal Pod Autoscaler (HPA) and resource limits."
                }
            ],
            "tailoring_suggestions": [
                "Highlight domain terminology from this job description to demonstrate operational context.",
                "Ensure bullet points follow the Google XYZ formula: 'Accomplished [X] as measured by [Y] by doing [Z]'."
            ]
        }
        cursor.execute("""
            INSERT INTO job_analyses (job_title, company_name, job_description, target_role, match_score, analysis_json)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("Machine Learning Engineer", "TechNova Labs", sample_jd, "Machine Learning Engineer", 78.5, json.dumps(sample_match)))

    # Seed initial applications if empty
    cursor.execute("SELECT COUNT(*) FROM applications")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO applications (company, role, location, status, applied_date, follow_up_date, salary_range, job_url, notes)
            VALUES 
            ('Anthropic', 'Machine Learning Engineer', 'San Francisco, CA / Remote', 'Interview', '2026-10-10', '2026-10-18', '$180k - $260k', 'https://www.anthropic.com/careers', 'Technical phone screen scheduled with systems team.'),
            ('Google', 'AI Application Engineer', 'Mountain View, CA', 'Applied', '2026-10-12', '2026-10-22', '$140k - $210k', 'https://www.google.com/about/careers', 'Submitted referral via engineering alumni network.'),
            ('Databricks', 'MLOps Engineer', 'Remote', 'Interested', NULL, NULL, '$160k - $230k', 'https://www.databricks.com/company/careers', 'Tailoring resume to emphasize MLflow and Docker experience.')
        """)

    # Seed activity logs
    cursor.execute("SELECT COUNT(*) FROM activity_logs")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO activity_logs (action_type, title, description, badge_color)
            VALUES
            ('Resume', 'Resume Uploaded', 'sample_engineering_resume.docx (75% readiness)', 'success'),
            ('Matcher', 'Job Match Calculated', 'Matched with ML Engineer at TechNova Labs (78% match)', 'sky'),
            ('Application', 'Interview Logged', 'Anthropic - Machine Learning Engineer', 'warning')
        """)

    conn.commit()
    conn.close()


# ---------------- Activity Logging ---------------- #

def log_activity(action_type: str, title: str, description: str, badge_color: str = "sky"):
    """Record an audit trail activity in SQLite."""
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO activity_logs (action_type, title, description, badge_color) VALUES (?, ?, ?, ?)",
            (action_type, title, description, badge_color)
        )
        conn.commit()
    finally:
        conn.close()


def get_recent_activities(limit: int = 6) -> List[Dict[str, Any]]:
    """Retrieve the most recent activity logs."""
    conn = get_db_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM activity_logs ORDER BY timestamp DESC LIMIT ?", (limit,)
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


# ---------------- Profile CRUD ---------------- #

def get_user_profile() -> Dict[str, Any]:
    """Retrieve the current user profile."""
    conn = get_db_connection()
    try:
        row = conn.execute("SELECT * FROM user_profiles WHERE id = 1").fetchone()
        if row:
            return dict(row)
        return {
            "id": 1,
            "full_name": "Job Seeker",
            "email": "user@example.com",
            "headline": "Engineering Student / Job Seeker",
            "target_role": "Machine Learning Engineer",
            "experience_level": "Entry Level (0-2 yrs)",
            "weekly_study_hours": 12,
            "summary": "Building foundational skills in modern AI, ML and engineering."
        }
    finally:
        conn.close()


def update_user_profile(full_name: str, email: str, headline: str, target_role: str,
                        experience_level: str, weekly_study_hours: int, summary: str):
    """Update profile attributes."""
    conn = get_db_connection()
    try:
        conn.execute("""
            UPDATE user_profiles
            SET full_name = ?, email = ?, headline = ?, target_role = ?,
                experience_level = ?, weekly_study_hours = ?, summary = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = 1
        """, (full_name, email, headline, target_role, experience_level, weekly_study_hours, summary))
        conn.commit()
        log_activity("Profile", "Profile Updated", f"Target role set to {target_role}", "sky")
    finally:
        conn.close()


# ---------------- Resumes CRUD ---------------- #

def save_resume(file_name: str, file_size_kb: float, raw_text: str, extracted_data: Dict[str, Any], readiness_score: int) -> int:
    """Save parsed resume and set as active."""
    conn = get_db_connection()
    try:
        # Mark previous resumes as inactive
        conn.execute("UPDATE resumes SET is_active = 0 WHERE is_active = 1")
        cursor = conn.execute("""
            INSERT INTO resumes (file_name, file_size_kb, raw_text, extracted_data_json, readiness_score, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        """, (file_name, file_size_kb, raw_text, json.dumps(extracted_data), readiness_score))
        resume_id = cursor.lastrowid
        conn.commit()
        log_activity("Resume", "Resume Uploaded", f"Parsed '{file_name}' ({readiness_score}% readiness)", "success")
        return resume_id
    finally:
        conn.close()


def get_active_resume() -> Optional[Dict[str, Any]]:
    """Retrieve the currently active resume, if any."""
    conn = get_db_connection()
    try:
        row = conn.execute("SELECT * FROM resumes WHERE is_active = 1 ORDER BY uploaded_at DESC LIMIT 1").fetchone()
        if not row:
            return None
        res = dict(row)
        res["extracted_data"] = json.loads(res["extracted_data_json"])
        return res
    finally:
        conn.close()


def get_all_resumes() -> List[Dict[str, Any]]:
    """Retrieve all uploaded resumes history."""
    conn = get_db_connection()
    try:
        rows = conn.execute("SELECT id, file_name, file_size_kb, readiness_score, is_active, uploaded_at FROM resumes ORDER BY uploaded_at DESC").fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def set_active_resume(resume_id: int):
    """Switch the active resume."""
    conn = get_db_connection()
    try:
        conn.execute("UPDATE resumes SET is_active = 0")
        conn.execute("UPDATE resumes SET is_active = 1 WHERE id = ?", (resume_id,))
        conn.commit()
    finally:
        conn.close()


# ---------------- Job Analyses CRUD ---------------- #

def save_job_analysis(job_title: str, company_name: str, job_description: str,
                      target_role: str, match_score: float, analysis_dict: Dict[str, Any]) -> int:
    """Save a job match analysis result."""
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            INSERT INTO job_analyses (job_title, company_name, job_description, target_role, match_score, analysis_json)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (job_title, company_name, job_description, target_role, match_score, json.dumps(analysis_dict)))
        analysis_id = cursor.lastrowid
        conn.commit()
        log_activity("Matcher", "Job Analyzed", f"Matched against '{job_title}' ({int(match_score)}% match)", "sky")
        return analysis_id
    finally:
        conn.close()


def get_latest_job_analysis() -> Optional[Dict[str, Any]]:
    """Get the most recent job description analysis."""
    conn = get_db_connection()
    try:
        row = conn.execute("SELECT * FROM job_analyses ORDER BY created_at DESC LIMIT 1").fetchone()
        if not row:
            return None
        res = dict(row)
        res["analysis"] = json.loads(res["analysis_json"])
        return res
    finally:
        conn.close()


def get_all_job_analyses() -> List[Dict[str, Any]]:
    """Retrieve all historical job analyses."""
    conn = get_db_connection()
    try:
        rows = conn.execute("SELECT id, job_title, company_name, target_role, match_score, created_at FROM job_analyses ORDER BY created_at DESC").fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


# ---------------- Roadmap Progress CRUD ---------------- #

def set_roadmap_task_status(role_id: str, week_id: int, task_id: str, is_completed: bool):
    """Mark a roadmap task completed or incomplete."""
    conn = get_db_connection()
    try:
        conn.execute("""
            INSERT INTO roadmap_progress (role_id, week_id, task_id, is_completed, updated_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(role_id, task_id) DO UPDATE SET
                is_completed = excluded.is_completed,
                updated_at = CURRENT_TIMESTAMP
        """, (role_id, week_id, task_id, 1 if is_completed else 0))
        conn.commit()
    finally:
        conn.close()


def get_roadmap_progress(role_id: str) -> Dict[str, bool]:
    """Return a dictionary mapping task_id to completion boolean for a given role."""
    conn = get_db_connection()
    try:
        rows = conn.execute(
            "SELECT task_id, is_completed FROM roadmap_progress WHERE role_id = ?",
            (role_id,)
        ).fetchall()
        return {r["task_id"]: bool(r["is_completed"]) for r in rows}
    finally:
        conn.close()


def get_completed_tasks_count(role_id: str) -> int:
    """Return count of completed tasks for a role."""
    conn = get_db_connection()
    try:
        row = conn.execute(
            "SELECT COUNT(*) FROM roadmap_progress WHERE role_id = ? AND is_completed = 1",
            (role_id,)
        ).fetchone()
        return row[0] if row else 0
    finally:
        conn.close()


# ---------------- Applications Tracker CRUD ---------------- #

def add_application(company: str, role: str, location: str, status: str,
                    applied_date: Optional[str] = None, follow_up_date: Optional[str] = None,
                    salary_range: str = "", job_url: str = "", notes: str = "") -> int:
    """Add a new job application."""
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            INSERT INTO applications (company, role, location, status, applied_date, follow_up_date, salary_range, job_url, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (company, role, location, status, applied_date, follow_up_date, salary_range, job_url, notes))
        app_id = cursor.lastrowid
        conn.commit()
        log_activity("Application", "Application Added", f"{role} at {company} ({status})", "warning" if status == "Interested" else "success")
        return app_id
    finally:
        conn.close()


def update_application(app_id: int, company: str, role: str, location: str, status: str,
                       applied_date: Optional[str], follow_up_date: Optional[str],
                       salary_range: str, job_url: str, notes: str):
    """Update an existing job application."""
    conn = get_db_connection()
    try:
        conn.execute("""
            UPDATE applications
            SET company = ?, role = ?, location = ?, status = ?,
                applied_date = ?, follow_up_date = ?, salary_range = ?,
                job_url = ?, notes = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (company, role, location, status, applied_date, follow_up_date, salary_range, job_url, notes, app_id))
        conn.commit()
        log_activity("Application", "Application Updated", f"{role} at {company} changed to {status}", "sky")
    finally:
        conn.close()


def delete_application(app_id: int):
    """Delete a job application by ID."""
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM applications WHERE id = ?", (app_id,))
        conn.commit()
    finally:
        conn.close()


def get_all_applications(status_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve all job applications, optionally filtered by status."""
    conn = get_db_connection()
    try:
        if status_filter and status_filter != "All":
            rows = conn.execute(
                "SELECT * FROM applications WHERE status = ? ORDER BY updated_at DESC",
                (status_filter,)
            ).fetchall()
        else:
            rows = conn.execute("SELECT * FROM applications ORDER BY updated_at DESC").fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_application_counts() -> Dict[str, int]:
    """Return count of applications grouped by status."""
    conn = get_db_connection()
    try:
        counts = {
            "Interested": 0,
            "To Apply": 0,
            "Applied": 0,
            "Interview": 0,
            "Offer": 0,
            "Rejected": 0,
            "Total": 0
        }
        rows = conn.execute("SELECT status, COUNT(*) as cnt FROM applications GROUP BY status").fetchall()
        for r in rows:
            counts[r["status"]] = r["cnt"]
            counts["Total"] += r["cnt"]
        return counts
    finally:
        conn.close()


# ---------------- System Maintenance ---------------- #

def reset_all_data():
    """Clear all user data tables and restore initial default state."""
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM resumes")
        conn.execute("DELETE FROM job_analyses")
        conn.execute("DELETE FROM roadmap_progress")
        conn.execute("DELETE FROM applications")
        conn.execute("DELETE FROM activity_logs")
        conn.execute("DELETE FROM user_profiles")
        conn.commit()
    finally:
        conn.close()
    init_db()
    log_activity("System", "Data Reset", "All data tables re-initialized to clean state", "warning")


# Initialize on import
init_db()
