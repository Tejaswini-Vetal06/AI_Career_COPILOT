"""
Career Copilot AI - Conversational Career & Interview Chatbot
Answers queries regarding:
- Resume optimization & bullet point rewriting
- Technical study roadmaps & priority concepts
- Interview preparation (STAR method, system design, mock questions)
- Job search strategy, platform networking (LinkedIn, Naukri), and career navigation
Contextually grounded in the candidate's active resume, target role, and job description.
Runs 100% locally or interfaces with Gemini API if key is present.
"""

import os
import re
from typing import Dict, Any, List, Optional

# Pre-curated high-frequency advice topics
KNOWLEDGE_BASE = {
    "tell_me_about_yourself": (
        "**Formula to Answer 'Tell Me About Yourself' (Present -> Past -> Future):**\n\n"
        "1. **Present (30 sec):** State your current role/studies and your primary technical focus.\n"
        "   *Example:* 'I'm an aspiring ML Engineer focusing on building production-grade predictive pipelines and asynchronous FastAPI services.'\n"
        "2. **Past (45 sec):** Highlight 1-2 major projects or internships where you delivered measurable technical impact.\n"
        "   *Example:* 'Recently, I engineered an end-to-end churn prediction service with Scikit-Learn and Docker that achieved an 18% PR-AUC boost.'\n"
        "3. **Future (20 sec):** Connect your passion directly to why you want this specific role at their company.\n"
        "   *Example:* 'I'm excited about this opportunity because your team is solving high-scale inference challenges that align with my systems engineering background.'"
    ),
    "star_method": (
        "**The STAR Framework for Behavioral Questions:**\n\n"
        "• **S - Situation:** Set the context in 1-2 sentences (company, project, deadline).\n"
        "• **T - Task:** State the specific challenge or technical problem you were assigned.\n"
        "• **A - Action:** Describe *your* specific technical choices, code, algorithms, and debugging steps (70% of your answer).\n"
        "• **R - Result:** Quantify the outcome (e.g. 'reduced latency by 35%', 'prevented data leakage', 'passed all regression tests')."
    ),
    "salary_negotiation": (
        "**Tips for Salary & Compensation Discussions:**\n\n"
        "1. **Research Market Rates:** Check levels.fyi, AmbitionBox, and Glassdoor for your city and tier.\n"
        "2. **Deflect Early Range Questions:** 'I'm primarily focused on finding the right engineering fit right now; I'm confident we can agree on a competitive package once we establish mutual value.'\n"
        "3. **Evaluate the Entire Package:** Consider base pay, performance bonuses, ESOPs/equity, work-from-home allowances, and learning stipends."
    ),
    "linkedin_naukri_tips": (
        "**Getting Recruiter Attention on LinkedIn & Naukri:**\n\n"
        "• **Headline:** Don't just put 'Student'. Write: `Aspiring ML Engineer | Python • PyTorch • FastAPI • Docker | Building RAG Systems`.\n"
        "• **Naukri Key Skills:** Naukri's search algorithm matches exact keyword tags. Add at least 15 technical skills (e.g. `Python`, `SQL`, `Machine Learning`, `Data Science`, `REST API`).\n"
        "• **Active Search Signal:** Update your resume on Naukri once a week (even a tiny space edit) so your profile shows as 'Active in last 7 days' to recruiters."
    )
}


def get_chatbot_response(user_query: str,
                         chat_history: Optional[List[Dict[str, str]]] = None,
                         active_resume: Optional[Dict[str, Any]] = None,
                         latest_job: Optional[Dict[str, Any]] = None,
                         target_role: str = "Machine Learning Engineer",
                         gemini_api_key: Optional[str] = None) -> str:
    """Generate intelligent, grounded career assistant response."""
    query = user_query.strip().lower()
    api_key = gemini_api_key or os.environ.get("GEMINI_API_KEY", "")

    # Context variables
    resume_skills = []
    if active_resume and "extracted_data" in active_resume:
        skills_dict = active_resume["extracted_data"].get("skills_categorized", {})
        for cat_list in skills_dict.values():
            resume_skills.extend(cat_list)

    skills_str = ", ".join(resume_skills[:8]) if resume_skills else "Python, Machine Learning, SQL"

    # If Gemini is configured, we could execute external LLM call; fallback to local AI agent
    # Intent 1: "Tell me about yourself" / Elevator Pitch
    if any(k in query for k in ["tell me about yourself", "introduce yourself", "elevator pitch"]):
        return (
            f"Here is a customized pitch tailored to your target role as a **{target_role}**:\n\n"
            + KNOWLEDGE_BASE["tell_me_about_yourself"]
            + f"\n\n💡 *Grounded in your resume:* Highlight your verified tools ({skills_str}) when summarizing your technical stack!"
        )

    # Intent 2: STAR method / Behavioral interview
    if any(k in query for k in ["star", "behavioral", "situation task action", "soft skills"]):
        return (
            f"### The STAR Method for {target_role} Interviews\n\n"
            + KNOWLEDGE_BASE["star_method"]
            + "\n\n💡 **Mock Example:** If asked *'Tell me about a time a project was delayed'*, focus on how you identified the data bottleneck, communicated with your lead, and added automated tests to prevent recurrence."
        )

    # Intent 3: ATS Score & Resume Optimization Advice
    if any(k in query for k in ["ats", "resume score", "improve resume", "bullet point", "keyword"]):
        missing_skills = []
        if latest_job and "analysis" in latest_job:
            missing_skills = latest_job["analysis"].get("missing_required", [])

        missing_str = ", ".join(missing_skills[:3]) if missing_skills else "target tools specified in the JD"
        return (
            f"### How to Maximize Your Resume's ATS Score\n\n"
            f"1. **Use the Google XYZ Formula:** Replace passive words ('helped', 'worked on') with quantifiable impact: *'Accomplished [X] measured by [Y]% by implementing [Z]'*.\n"
            f"2. **Weave Missing Keywords:** Right now, your target job highlights **{missing_str}**. If you have working familiarity with them, add them to your Technical Skills or Projects.\n"
            f"3. **Simple One-Column Format:** Multi-column designs or raster graphics can confuse older ATS scanners. Use our built-in **Resume Builder** to export a clean, parseable A4 format."
        )

    # Intent 4: Study Roadmap & What to Learn Next
    if any(k in query for k in ["study", "roadmap", "what should i learn", "curriculum", "learn next", "where to start"]):
        from modules.data.roles_data import ROLES_DATA
        role_info = ROLES_DATA.get(target_role, {})
        branch = role_info.get("branch", "Engineering")
        skills = role_info.get("essential_skills", ["Core Principles", "Industry Tools", "Testing"])

        if "Civil" in branch or "Civil" in target_role:
            week1 = "Week 1: Strength of Materials & Codes (IS 456 / ACI) and AutoCAD 2D structural drafting."
            week2 = "Week 2: 3D Finite Element Modeling in STAAD.Pro / ETABS under dead, live, and seismic lateral loads."
            week3 = "Week 3: Concrete QA/QC, Bar Bending Schedules (BBS), and site estimation in Primavera P6."
            week4 = "Week 4: Portfolio Capstone (High-rise seismic design or industrial steel frame analysis) with drawings."
        elif "Mechanical" in branch or "Mechanical" in target_role:
            week1 = "Week 1: Machine Design fundamentals and parametric 3D CAD modeling in SolidWorks / CATIA."
            week2 = "Week 2: Geometric Dimensioning & Tolerancing (GD&T ASME Y14.5) and tolerance stack-up budgeting."
            week3 = "Week 3: Static structural FEA or CFD flow modeling in ANSYS with mesh convergence studies."
            week4 = "Week 4: Complete mechanism design portfolio package with exploded assemblies and DFMA validation."
        elif "Electrical" in branch or "Power" in target_role:
            week1 = "Week 1: Three-phase power calculations, per-unit systems, and transformer vector groups."
            week2 = "Week 2: Substation single-line diagrams, load flow, and short-circuit fault analysis in ETAP."
            week3 = "Week 3: Protection relay coordination (overcurrent 50/51, differential 87) and switchgear sizing."
            week4 = "Week 4: Grid integration model of renewable solar/battery inverter systems in MATLAB Simulink."
        elif "Electronics" in branch or "Embedded" in target_role or "VLSI" in target_role:
            week1 = "Week 1: Microcontroller memory maps, bare-metal C peripheral drivers (UART, I2C, SPI)."
            week2 = "Week 2: Real-time multi-tasking with FreeRTOS (queues, semaphores, priority inversion avoidance)."
            week3 = "Week 3: Schematic capture and 4-layer PCB layout with high-speed routing in KiCad / Altium."
            week4 = "Week 4: IoT telemetry prototype or synthesizable Verilog/FPGA RISC-V core in Vivado."
        elif "Medical" in branch or "Physician" in target_role or "Nursing" in target_role:
            week1 = "Week 1: Systematic physical examinations, emergency ABCDE resuscitation, and BLS/ACLS protocols."
            week2 = "Week 2: Rational evidence-based pharmacotherapy, antimicrobial stewardship, and dosage calculations."
            week3 = "Week 3: Diagnostic telemetry, 12-lead ECG analysis, ABG interpretation, and infection control."
            week4 = "Week 4: Clinical audit case study and standardized SBAR communication protocol."
        else:
            week1 = "Week 1: Foundations & Clean Code: Data structures, vectorized operations, and unit tests (`pytest`)."
            week2 = "Week 2: Core Modeling: Train baseline algorithms, perform cross-validation, and tune hyperparameters."
            week3 = "Week 3: Deployment: Package application into an asynchronous FastAPI service with Docker."
            week4 = "Week 4: Portfolio Capstone: Build an end-to-end reproducible pipeline with interactive Streamlit UI."

        return (
            f"### Recommended 4-Week Study Roadmap for {target_role}\n\n"
            f"Based on real hiring standards in **{branch}**, here is your weekly milestone plan:\n\n"
            f"• **{week1}**\n"
            f"• **{week2}**\n"
            f"• **{week3}**\n"
            f"• **{week4}**\n\n"
            f"👉 *Check your interactive checklist in the **Learning Roadmap** tab to track persistent progress!*"
        )

    # Intent 5: Platform Search (LinkedIn / Naukri / Indeed)
    if any(k in query for k in ["naukri", "linkedin", "indeed", "job search", "recruiter", "apply"]):
        return (
            f"### Multi-Platform Job Hunting Strategy\n\n"
            + KNOWLEDGE_BASE["linkedin_naukri_tips"]
            + f"\n\n👉 *You can visit the **Job Opportunities** page in the sidebar to search live openings directly across Naukri, LinkedIn, and Indeed!*"
        )

    # Intent 6: Salary & Offer Negotiation
    if any(k in query for k in ["salary", "negotiate", "compensation", "package", "ctc"]):
        return (
            f"### Professional Compensation & Negotiation Guide\n\n"
            + KNOWLEDGE_BASE["salary_negotiation"]
            + f"\n\nFor an entry to mid-level **{target_role}**, industry compensation packages vary by sector and city:\n"
            f"• **India:** ₹6 LPA - ₹25+ LPA (depending on industry sector, MNC tiers, and project complexity)\n"
            f"• **International / Remote:** $75,000 - $160,000+"
        )

    # General Fallback / Intelligent Technical Assistant
    return (
        f"### Career Copilot AI Advice\n\n"
        f"Regarding your question about *'{user_query}'*:\n\n"
        f"When aiming for a **{target_role}** role, hiring managers and interview panels evaluate:\n"
        f"1. **Verifiable Proof-of-Work:** Real portfolio artifacts—such as CAD designs, ETABS calculation models, PCB layouts, clinical audit reports, or Git repositories.\n"
        f"2. **Domain Standards & Tradeoffs:** Demonstrating why specific engineering formulas, safety factors, codes (IS, ASME, IEEE, AHA), or algorithms were chosen.\n"
        f"3. **Targeted Resume Alignment:** Expressing past contributions in the Google XYZ format: *Accomplished [X] measured by [Y] by doing [Z]*.\n\n"
        f"💡 **Suggested Next Steps:**\n"
        f"• Check your alignment on the **Job Description Matcher** page.\n"
        f"• Practice STAR-method interview questions in the **AI Interview Coach (RAG)** tab.\n"
        f"• Explore tailored benchmarks in **Project Recommendations**."
    )

