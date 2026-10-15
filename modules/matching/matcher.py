"""
Career Copilot AI - Job Description Matcher & Skill Gap Engine
Performs transparent matching, skill gap prioritization, and tailored bullet guidance.
Grounds scores in explicit formulas without representing keyword overlap as hire probability.
"""

import re
import urllib.parse
from typing import Dict, Any, List, Set, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from modules.parsers.resume_parser import TECH_TAXONOMY, extract_skills_from_text


# High-quality learning resources & practice exercises across Engineering & Healthcare
SKILL_LEARNING_GUIDES = {
    # Tech & AI
    "python": {
        "why_matters": "Core foundational language for modern AI, backend services, and automated data pipelines.",
        "resource": "Official Python Docs & Real Python Intermediate Tutorials",
        "resource_url": "https://docs.python.org/3/tutorial/",
        "exercise": "Implement an asynchronous web scraper or custom context manager handling API rate limits.",
        "project": "RESTful microservice with FastAPI, SQLAlchemy 2.0, and Pytest coverage."
    },
    "pytorch": {
        "why_matters": "Dominant deep learning research and deployment framework for modern transformer and neural architectures.",
        "resource": "PyTorch Official 60-Minute Blitz & Deep Learning with PyTorch Book",
        "resource_url": "https://pytorch.org/tutorials/",
        "exercise": "Write a custom PyTorch nn.Module with forward pass, cross-entropy loss, and gradient clipping.",
        "project": "Fine-tune a vision or language model using custom PyTorch training loop and learning rate scheduler."
    },
    "docker": {
        "why_matters": "Standard containerization technology ensuring reproducible environments across dev, staging, and production.",
        "resource": "Docker Get Started Guide & Multi-Stage Builds Documentation",
        "resource_url": "https://docs.docker.com/get-started/",
        "exercise": "Author a production multi-stage Dockerfile that minimizes image size (<150MB) and drops root privileges.",
        "project": "Containerize a FastAPI ML inference application with non-root user and health-check probes."
    },
    "fastapi": {
        "why_matters": "High-performance asynchronous Python web framework optimized for serving ML inference and REST APIs.",
        "resource": "FastAPI Official Interactive Tutorial & Dependency Injection Guide",
        "resource_url": "https://fastapi.tiangolo.com/tutorial/",
        "exercise": "Build an API endpoint with Pydantic request validation, API key middleware, and async background tasks.",
        "project": "Model inference microservice handling concurrent batches with sub-30ms latency."
    },
    "sql": {
        "why_matters": "Universal lingua franca for relational data extraction, metric aggregation, and database interaction.",
        "resource": "Mode Analytics SQL Tutorial for Data Analysis & PostgreSQL Official Docs",
        "resource_url": "https://mode.com/sql-tutorial/",
        "exercise": "Write queries employing Window functions (DENSE_RANK, LEAD/LAG, PARTITION BY) to compute cohort retention.",
        "project": "Design a relational schema with 3NF normalization, foreign keys, and performant indexes."
    },
    "scikit-learn": {
        "why_matters": "Standard library for classical machine learning, feature pipelines, and model evaluation.",
        "resource": "Scikit-Learn User Guide & Supervised Learning Documentation",
        "resource_url": "https://scikit-learn.org/stable/user_guide.html",
        "exercise": "Construct an end-to-end Pipeline combining StandardScaler, OneHotEncoder, and GridSearchCV.",
        "project": "Predictive classification model with cross-validated PR-AUC evaluation and feature importance plots."
    },
    "langchain": {
        "why_matters": "Framework for orchestrating LLM prompt chains, external tool calling, and RAG document stores.",
        "resource": "LangChain Official Conceptual Docs & Architecture Patterns",
        "resource_url": "https://python.langchain.com/docs/introduction/",
        "exercise": "Implement a Conversational Retrieval Chain with token-buffered memory and source document citation.",
        "project": "Domain RAG assistant with hybrid semantic search, MMR reranking, and citation badges."
    },
    "git": {
        "why_matters": "Essential source code version control and collaborative development standard across all engineering teams.",
        "resource": "Pro Git Book (Free) by Scott Chacon",
        "resource_url": "https://git-scm.com/book/en/v2",
        "exercise": "Perform interactive rebasing, resolve complex merge conflicts, and manage feature branch workflows.",
        "project": "Maintain a clean GitHub repository with atomic commits, conventional commit messages, and PR templates."
    },
    # Civil Engineering
    "autocad": {
        "why_matters": "Primary industry drafting standard for architectural blueprints, structural drawings, and civil plans.",
        "resource": "Autodesk AutoCAD Official Fundamentals & Civil Drafting Tutorials",
        "resource_url": "https://www.autodesk.com/support/technical/product/autocad",
        "exercise": "Draft a multi-layer residential floor plan with dimensions, grid lines, and title block.",
        "project": "Complete structural reinforcement drawing with bar bending schedule in AutoCAD."
    },
    "staad.pro": {
        "why_matters": "Standard 3D finite element structural analysis software for commercial buildings, steel frames, and foundations.",
        "resource": "Bentley STAAD.Pro Official Learning Modules & IS Code Analysis",
        "resource_url": "https://www.bentley.com/software/staad/",
        "exercise": "Model a 3-bay, 4-story RCC frame and perform dead, live, and wind load combinations.",
        "project": "Industrial steel shed analysis with crane girder and wind pressure checks in STAAD.Pro."
    },
    "etabs": {
        "why_matters": "Industry leading structural analysis software specifically tuned for high-rise buildings and seismic design.",
        "resource": "CSI ETABS Official Tutorials & Response Spectrum Modeling",
        "resource_url": "https://www.csiamerica.com/products/etabs",
        "exercise": "Model a G+10 high-rise frame with shear walls and compute modal mass participation ratios.",
        "project": "Seismic response spectrum analysis of an irregular building compliant with IS 1893."
    },
    # Mechanical Engineering
    "solidworks": {
        "why_matters": "Premier 3D parametric CAD modeling standard for mechanism design, assemblies, and manufacturing drawings.",
        "resource": "SolidWorks Official Tutorials & Parametric Design Certification Prep",
        "resource_url": "https://www.solidworks.com/",
        "exercise": "Model a parametric mechanical assembly with mates, kinematic degrees of freedom, and interference checks.",
        "project": "Design a 2-stage planetary gearbox with exploded assembly and 2D manufacturing drawings."
    },
    "ansys": {
        "why_matters": "World standard for finite element analysis (FEA) and computational fluid dynamics (CFD) simulation.",
        "resource": "ANSYS Innovation Courses (Free Official Certification)",
        "resource_url": "https://innovationspace.ansys.com/courses/",
        "exercise": "Perform static structural analysis of an aluminum bracket, evaluate mesh convergence, and verify Von Mises stress.",
        "project": "Thermal fatigue and stress simulation of an automotive brake rotor or heat exchanger."
    },
    # Electrical & Electronics
    "matlab": {
        "why_matters": "Mathematical computing, numerical analysis, and simulation standard across control systems and signal processing.",
        "resource": "MathWorks MATLAB Onramp & Simulink Interactive Tutorials",
        "resource_url": "https://matlabacademy.mathworks.com/",
        "exercise": "Simulate a closed-loop PID speed controller with step response and overshoot analysis.",
        "project": "Power electronics DC-DC buck-boost converter simulation in MATLAB Simulink."
    },
    "etap": {
        "why_matters": "Industry standard electrical power system analysis software for substations, load flow, and fault analysis.",
        "resource": "ETAP Official Video Tutorials & Power Engineering Handbook",
        "resource_url": "https://etap.com/",
        "exercise": "Model a 33kV industrial distribution single-line diagram and compute load flow voltages.",
        "project": "Protection relay coordination and short-circuit fault analysis for an electrical substation in ETAP."
    },
    "embedded c": {
        "why_matters": "Direct hardware register programming standard for ARM microcontrollers, automotive ECUs, and IoT.",
        "resource": "ARM Cortex-M Embedded Systems Programming & STM32 Bare-Metal Tutorials",
        "resource_url": "https://developer.arm.com/",
        "exercise": "Write register-level peripheral drivers for UART and I2C with interrupt service routines.",
        "project": "Real-time sensor telemetry acquisition firmware using FreeRTOS queues on STM32."
    },
    "verilog": {
        "why_matters": "Hardware Description Language (HDL) standard for RTL digital logic, FPGA prototyping, and ASIC synthesis.",
        "resource": "HDLBits Verilog Practice Problems & ASIC World",
        "resource_url": "https://hdlbits.01xz.net/",
        "exercise": "Implement a synthesizable finite state machine (FSM) with synchronous reset and debounced inputs.",
        "project": "Pipelined 32-bit RISC-V processor core implementation with hazard detection in Verilog."
    },
    # Healthcare & Medical
    "clinical diagnosis": {
        "why_matters": "Core physician competency for evaluating patient symptoms, history, physical signs, and evidence-based workup.",
        "resource": "WHO Clinical Guidelines & UpToDate Clinical Decision Support",
        "resource_url": "https://www.who.int/publications/guidelines",
        "exercise": "Perform structured SOAP clinical case presentations with prioritized differential diagnoses.",
        "project": "Clinical audit evaluating outpatient antimicrobial prescription compliance against hospital protocol."
    },
    "pharmacology": {
        "why_matters": "Essential knowledge of drug mechanisms, indications, contraindications, dosage titration, and adverse interactions.",
        "resource": "Goodman & Gilman's Pharmacological Basis of Therapeutics & Medscape Reference",
        "resource_url": "https://reference.medscape.com/drugs",
        "exercise": "Calculate pediatric weight-based drug doses and identify potential CYP450 drug-drug interactions.",
        "project": "Formulate an evidence-based pharmacotherapy guideline for inpatient glycemic management."
    },
    "bls": {
        "why_matters": "Life-saving resuscitation protocols for cardiac arrest, airway obstruction, and medical emergencies.",
        "resource": "American Heart Association (AHA) Basic Life Support (BLS) Guidelines",
        "resource_url": "https://cpr.heart.org/",
        "exercise": "Practice high-quality chest compressions, AED placement, and bag-valve-mask ventilations.",
        "project": "Conduct hospital emergency code blue simulation and response time audit."
    }
}


def extract_skills_from_job_description(jd_text: str) -> Dict[str, Set[str]]:
    """Partition extracted job skills into Required vs Preferred based on contextual proximity."""
    all_known_skills = {}
    for cat, skills in TECH_TAXONOMY.items():
        for s in skills:
            all_known_skills[s] = cat

    preferred_keywords = ["preferred", "nice to have", "plus", "bonus", "desired", "beneficial", "good to have", "optional"]
    required_keywords = ["required", "must have", "minimum", "requirements", "essential", "basic qualifications", "qualifications", "needed", "need", "responsibilities"]

    required_skills = set()
    preferred_skills = set()

    # Split into lines and sentences
    lines = [line.strip() for line in jd_text.replace(";", "\n").replace(".", "\n").split("\n") if line.strip()]

    current_context = "required"  # default context

    for line in lines:
        line_lower = line.lower()
        if any(k in line_lower for k in preferred_keywords):
            current_context = "preferred"
        elif any(k in line_lower for k in required_keywords):
            current_context = "required"

        for skill in all_known_skills:
            pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"
            if re.search(pattern, line_lower):
                display_name = skill.title() if len(skill) > 3 and not skill.isupper() else skill.upper()
                if current_context == "preferred" or any(k in line_lower for k in preferred_keywords):
                    preferred_skills.add(display_name)
                else:
                    required_skills.add(display_name)

    # Clean overlap: if skill is in both, required takes precedence
    preferred_skills = preferred_skills - required_skills

    # Fallback if no skills segregated
    if not required_skills and not preferred_skills:
        extracted = extract_skills_from_text(jd_text)
        all_skills = [s for sublist in extracted.values() for s in sublist]
        required_skills = set(all_skills[:6])
        preferred_skills = set(all_skills[6:])

    return {
        "required": required_skills,
        "preferred": preferred_skills
    }


def compute_semantic_similarity(resume_text: str, jd_text: str) -> float:
    """Compute TF-IDF cosine similarity between resume and job description."""
    try:
        vectorizer = TfidfVectorizer(stop_words="english", max_features=1500)
        tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
        sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(sim * 100.0)
    except Exception:
        return 50.0


def match_resume_to_job(resume_data: Dict[str, Any], jd_text: str, target_role: str) -> Dict[str, Any]:
    """Execute complete match analysis between parsed resume and job description."""
    resume_text = resume_data.get("raw_text", "")
    resume_skills_dict = resume_data.get("skills_categorized", {})

    # Flatten all resume skills to lowercase set
    resume_skills_set = set()
    for skill_list in resume_skills_dict.values():
        for s in skill_list:
            resume_skills_set.add(s.lower())

    # Extract JD skills
    jd_skills = extract_skills_from_job_description(jd_text)
    required_jd = jd_skills["required"]
    preferred_jd = jd_skills["preferred"]

    # If JD extracted no skills (very short or unusual format), fallback to taxonomy scan
    if not required_jd and not preferred_jd:
        extracted = extract_skills_from_text(jd_text)
        all_extracted = [s for sublist in extracted.values() for s in sublist]
        required_jd = set(all_extracted[:6])
        preferred_jd = set(all_extracted[6:])

    # Check match against resume
    matched_required = []
    missing_required = []
    for s in required_jd:
        if s.lower() in resume_skills_set or re.search(r"\b" + re.escape(s.lower()) + r"\b", resume_text.lower()):
            matched_required.append(s)
        else:
            missing_required.append(s)

    matched_preferred = []
    missing_preferred = []
    for s in preferred_jd:
        if s.lower() in resume_skills_set or re.search(r"\b" + re.escape(s.lower()) + r"\b", resume_text.lower()):
            matched_preferred.append(s)
        else:
            missing_preferred.append(s)

    # Coverage calculations
    req_pct = (len(matched_required) / max(len(required_jd), 1)) * 100.0 if required_jd else 80.0
    pref_pct = (len(matched_preferred) / max(len(preferred_jd), 1)) * 100.0 if preferred_jd else 70.0
    semantic_sim = compute_semantic_similarity(resume_text, jd_text)

    # Transparent Composite Match Formula:
    # 50% Required Skill Coverage + 20% Preferred Skill Coverage + 30% Semantic Relevancy
    composite_score = round(0.50 * req_pct + 0.20 * pref_pct + 0.30 * min(semantic_sim * 1.5, 100.0), 1)
    composite_score = min(max(composite_score, 15.0), 96.0)

    # Categorize skills into 3 gap buckets:
    # 1. Demonstrated: found in resume and corroborated
    # 2. To Improve: mentioned once without clear bullet context
    # 3. Not Demonstrated: missing entirely from resume
    demonstrated = sorted(list(set(matched_required + matched_preferred)))
    not_demonstrated = sorted(list(set(missing_required + missing_preferred)))

    to_improve = []
    # If a demonstrated skill has no metric in resume text, consider it for improvement
    for s in list(demonstrated):
        if not re.search(r"(\d+%\b|\$\d+|\b\d+\s*(users|ms|records)\b)", resume_text.lower()):
            if len(demonstrated) > 3 and s not in ["Python", "Git"]:
                to_improve.append(s)
                demonstrated.remove(s)
                if len(to_improve) >= 3:
                    break

    # Prioritized skill gaps with learning resources
    prioritized_gaps = []
    for skill_name in not_demonstrated + to_improve:
        low = skill_name.lower()
        guide = SKILL_LEARNING_GUIDES.get(low, {
            "why_matters": f"Key technical capability required by employers hiring for {target_role} roles.",
            "resource": f"Official documentation and production tutorials for {skill_name}.",
            "resource_url": f"https://www.google.com/search?q={urllib.parse.quote_plus(skill_name)}+official+documentation",
            "exercise": f"Build a focused hands-on exercise implementing a core feature using {skill_name}.",
            "project": f"Incorporate {skill_name} into your active portfolio project with unit tests."
        })
        is_required = skill_name in required_jd
        prioritized_gaps.append({
            "skill": skill_name,
            "priority": "High (Required)" if is_required else "Medium (Preferred)",
            "status": "Needs Improvement" if skill_name in to_improve else "Not Demonstrated",
            "why_matters": guide["why_matters"],
            "resource": guide["resource"],
            "resource_url": guide.get("resource_url", "#"),
            "exercise": guide["exercise"],
            "project": guide["project"]
        })

    # Suggestions for bullet point tailoring
    tailoring_suggestions = []
    if missing_required:
        tailoring_suggestions.append(
            f"Explicitly weave critical required technologies like {', '.join(missing_required[:3])} into your recent project descriptions if you have practical familiarity with them."
        )
    tailoring_suggestions.append(
        "Highlight domain terminology from this job description (e.g. latency constraints, testing coverage, scale) to demonstrate operational context."
    )
    tailoring_suggestions.append(
        "Ensure bullet points follow the Google XYZ formula: 'Accomplished [X] as measured by [Y] by doing [Z]'."
    )

    # Calculate Application Readiness Verdict ("Is it OK to apply?")
    if composite_score >= 70.0:
        verdict_status = "Ready to Apply"
        verdict_color = "success"
        verdict_summary = "Strong Alignment! Your resume demonstrates the core essential skills required for this job. You have a solid profile to submit your application with confidence."
        action_advice = "Make sure your contact links (GitHub, LinkedIn) are up to date and proceed with applying!"
    elif composite_score >= 45.0:
        verdict_status = "Good Potential — Tailor First"
        verdict_color = "warning"
        verdict_summary = "Moderate Alignment. You possess relevant baseline engineering skills, but the resume lacks 2-3 specific keywords or quantifiable metric evidence highlighted in the job description."
        action_advice = f"Use the Resume Builder to weave in {', '.join(missing_required[:2]) if missing_required else 'required frameworks'} before applying to boost interview callback rates."
    else:
        verdict_status = "Significant Skill Gap"
        verdict_color = "error"
        verdict_summary = "High Gap. This role demands several specialized qualifications not yet evidenced on your resume. Applying as-is may result in automated ATS filtering."
        action_advice = f"Focus on building a portfolio project demonstrating {', '.join(missing_required[:2]) if missing_required else 'target tools'} or study the personalized roadmap first."

    return {
        "target_role": target_role,
        "composite_score": composite_score,
        "jd_ats_score": int(composite_score),
        "application_verdict": {
            "status": verdict_status,
            "badge_color": verdict_color,
            "summary": verdict_summary,
            "action_advice": action_advice
        },
        "score_breakdown": {
            "required_coverage_pct": round(req_pct, 1),
            "preferred_coverage_pct": round(pref_pct, 1),
            "semantic_relevance_pct": round(min(semantic_sim * 1.5, 100.0), 1),
            "formula_explanation": (
                "Composite ATS score = (50% x Required Skill Coverage) + "
                "(20% x Preferred Skill Coverage) + (30% x Semantic Experience Relevancy). "
                "This indicates keyword and contextual alignment with the job description. "
                "It does not represent hiring probability."
            )
        },
        "required_skills": sorted(list(required_jd)),
        "preferred_skills": sorted(list(preferred_jd)),
        "matched_required": sorted(matched_required),
        "missing_required": sorted(missing_required),
        "matched_preferred": sorted(matched_preferred),
        "missing_preferred": sorted(missing_preferred),
        "demonstrated_skills": demonstrated,
        "to_improve_skills": to_improve,
        "not_demonstrated_skills": not_demonstrated,
        "prioritized_gaps": prioritized_gaps,
        "tailoring_suggestions": tailoring_suggestions
    }
