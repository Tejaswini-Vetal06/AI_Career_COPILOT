"""
Career Copilot AI - Resume Extraction & Bullet Quality Analyzer
Supports text-based PDF (via PyMuPDF/pypdf) and DOCX (via python-docx/zipfile XML).
Performs structural section extraction, skill classification, ATS hygiene checks,
and deep bullet point quality analysis without ever inventing qualifications.
"""

import re
import io
import zipfile
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Optional, Tuple

# Try PyMuPDF first, fallback to pypdf
try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

try:
    import pypdf
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

try:
    import docx
    HAS_PYTHON_DOCX = True
except ImportError:
    HAS_PYTHON_DOCX = False


# Universal Multi-Disciplinary Taxonomy (All Engineering Branches + Healthcare & Medical)
UNIVERSAL_TAXONOMY = {
    # 1. Computer Science & Software
    "Programming & Core CS": [
        "python", "c++", "c#", "c", "java", "javascript", "typescript", "sql", "r", "go",
        "rust", "bash", "shell", "scala", "kotlin", "ruby", "php", "swift", "matlab", "html", "css",
        "data structures", "algorithms", "object-oriented programming"
    ],
    "AI, ML & Data Science": [
        "pytorch", "tensorflow", "scikit-learn", "keras", "hugging face", "transformers",
        "xgboost", "lightgbm", "catboost", "opencv", "spacy", "nltk", "langchain", "llamaindex",
        "dspy", "deep learning", "nlp", "computer vision", "rag", "llm", "genai", "prompt engineering",
        "fine-tuning", "lora", "qlora", "reinforcement learning", "onnx", "tensorrt",
        "pandas", "numpy", "polars", "scipy", "matplotlib", "seaborn", "plotly", "apache spark",
        "pyspark", "kafka", "airflow", "dbt", "bigquery", "snowflake", "power bi", "tableau"
    ],
    "Cloud, DevOps & Systems": [
        "docker", "kubernetes", "aws", "gcp", "google cloud", "azure", "linux", "git",
        "github", "github actions", "gitlab ci", "ci/cd", "terraform", "ansible", "prometheus",
        "grafana", "mlflow", "wandb", "weights & biases", "fastapi", "flask", "django",
        "node.js", "express", "spring boot", "rest api", "graphql", "microservices", "postgresql", "mysql", "mongodb", "redis"
    ],
    # 2. Civil & Infrastructure Engineering
    "Civil & Structural Engineering": [
        "autocad", "revit", "staad.pro", "etabs", "civil 3d", "bim", "surveying", "total station",
        "concrete technology", "structural analysis", "rcc design", "steel structures", "is 456",
        "soil mechanics", "geotechnical engineering", "foundation engineering", "primavera", "primavera p6",
        "estimation", "costing", "quantity surveying", "highway engineering", "pavement design",
        "hydrology", "environmental engineering", "construction management", "site supervision"
    ],
    # 3. Mechanical, Thermal & Robotics
    "Mechanical & Manufacturing Engineering": [
        "solidworks", "catia", "creo", "autodesk inventor", "ansys", "fea", "cfd", "gd&t",
        "thermodynamics", "fluid mechanics", "heat transfer", "machine design", "kinematics",
        "hvac", "mechatronics", "robotics", "cnc", "cam", "manufacturing processes", "dfma",
        "finite element analysis", "computational fluid dynamics", "six sigma", "lean manufacturing"
    ],
    # 4. Electrical, Power & Renewables
    "Electrical & Power Systems": [
        "power systems", "matlab simulink", "simulink", "etap", "switchgear", "substation engineering",
        "high voltage", "transformers", "transmission lines", "power electronics", "motor drives",
        "plc", "scada", "industrial automation", "solar pv", "photovoltaic", "renewable energy",
        "battery storage", "electric vehicles", "ev powertrain", "smart grid", "power distribution"
    ],
    # 5. Electronics & Communication (ECE / VLSI / IoT)
    "Electronics, Embedded & VLSI": [
        "embedded c", "embedded systems", "microcontrollers", "arm cortex", "arduino", "esp32",
        "freertos", "rtos", "verilog", "vhdl", "systemverilog", "fpga", "vlsi", "cadence",
        "synopsys", "static timing analysis", "pcb design", "kicad", "altium designer",
        "i2c", "spi", "uart", "dsp", "digital signal processing", "iot", "internet of things",
        "rf engineering", "wireless communication", "5g", "bluetooth low energy"
    ],
    # 6. Chemical & Process Engineering
    "Chemical & Process Engineering": [
        "aspen plus", "aspen hysys", "p&id", "process flow diagrams", "mass transfer", "heat transfer",
        "chemical reaction engineering", "distillation", "process simulation", "process safety",
        "hazop", "piping engineering", "refinery operations", "bioprocess engineering"
    ],
    # 7. Medical, Healthcare & Clinical Sciences
    "Medical & Healthcare Clinical Skills": [
        "clinical diagnosis", "patient assessment", "patient care", "internal medicine", "general surgery",
        "pediatrics", "emergency medicine", "triage", "bls", "acls", "basic life support",
        "pharmacology", "pharmacotherapy", "dosage calculation", "vital signs monitoring",
        "ecg interpretation", "medical records", "electronic medical records", "emr", "ehr",
        "infection control", "critical care", "icu management", "telemedicine", "medical ethics",
        "healthcare administration", "nabh compliance", "pathology", "radiology interpretation"
    ]
}

# Alias for backwards-compatibility
TECH_TAXONOMY = UNIVERSAL_TAXONOMY

# Strong Action Verbs across Engineering, Tech & Healthcare
STRONG_ACTION_VERBS = {
    "architected", "engineered", "developed", "built", "designed", "deployed", "implemented",
    "optimized", "accelerated", "reduced", "increased", "scaled", "automated", "trained",
    "benchmarked", "integrated", "constructed", "spearheaded", "formulated", "published",
    "migrated", "orchestrated", "streamlined", "eliminated", "led", "enhanced", "resolved",
    "diagnosed", "treated", "administered", "supervised", "inspected", "calculated", "drafted",
    "simulated", "modeled", "commissioned", "calibrated", "audited", "procured", "synthesized"
}

WEAK_PASSIVE_VERBS = {
    "helped", "assisted", "worked on", "responsible for", "participated in", "handled",
    "did", "contributed to", "tried", "supported", "tasked with", "involved in"
}


def extract_text_from_pdf(file_bytes: bytes) -> Tuple[str, Optional[str]]:
    """Extract text from PDF file bytes with graceful library fallbacks."""
    text = ""
    # Attempt PyMuPDF first
    if HAS_PYMUPDF:
        try:
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                text += page.get_text() + "\n"
            if text.strip():
                return text.strip(), None
        except Exception:
            pass

    # Fallback to pypdf
    if HAS_PYPDF:
        try:
            reader = pypdf.PdfReader(io.BytesIO(file_bytes))
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            if text.strip():
                return text.strip(), None
        except Exception as e:
            return "", f"Error reading PDF: {str(e)}"

    if not text.strip():
        return "", (
            "Could not extract selectable text. The document may be a scanned image or "
            "uses an unsupported font encoding. Please upload a standard text PDF or DOCX."
        )

    return text.strip(), None


def extract_text_from_docx(file_bytes: bytes) -> Tuple[str, Optional[str]]:
    """Extract text from DOCX file bytes using python-docx or native XML zip extraction."""
    # Attempt python-docx if available
    if HAS_PYTHON_DOCX:
        try:
            doc = docx.Document(io.BytesIO(file_bytes))
            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        if cell.text.strip():
                            paragraphs.append(cell.text.strip())
            return "\n".join(paragraphs).strip(), None
        except Exception:
            pass

    # Native zipfile + XML fallback
    try:
        with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
            xml_content = z.read("word/document.xml")
            tree = ET.fromstring(xml_content)
            # Namespace for WordprocessingML
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            texts = []
            for node in tree.iter(f"{{{ns['w']}}}p"):
                p_text = "".join(node.itertext()).strip()
                if p_text:
                    texts.append(p_text)
            full_text = "\n".join(texts).strip()
            if full_text:
                return full_text, None
    except Exception as e:
        return "", f"Failed to extract text from DOCX: {str(e)}"

    return "", "Could not extract text from the uploaded DOCX file."


def extract_contact_info(text: str) -> Dict[str, Any]:
    """Extract email, phone, and professional portfolio links."""
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone_match = re.search(r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    linkedin_match = re.search(r"linkedin\.com/in/[a-zA-Z0-9_-]+", text, re.IGNORECASE)
    github_match = re.search(r"github\.com/[a-zA-Z0-9_-]+", text, re.IGNORECASE)

    return {
        "email": email_match.group(0) if email_match else None,
        "phone": phone_match.group(0) if phone_match else None,
        "linkedin": linkedin_match.group(0) if linkedin_match else None,
        "github": github_match.group(0) if github_match else None,
    }


def extract_skills_from_text(text: str) -> Dict[str, List[str]]:
    """Match words against our tech taxonomy using word boundaries."""
    text_lower = f" {text.lower()} "
    found_categorized = {}
    total_skills = set()

    for category, skill_list in TECH_TAXONOMY.items():
        matched = []
        for skill in skill_list:
            # Match with regex word boundary
            pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"
            if re.search(pattern, text_lower):
                matched.append(skill.title() if len(skill) > 3 and not skill.isupper() else skill.upper())
                total_skills.add(skill)
        if matched:
            found_categorized[category] = sorted(list(set(matched)))

    return found_categorized


def parse_resume_sections(text: str) -> Dict[str, str]:
    """Heuristic detection of main standard resume sections."""
    sections: Dict[str, str] = {
        "summary": "",
        "experience": "",
        "education": "",
        "projects": "",
        "skills": "",
        "certifications": ""
    }

    heading_patterns = {
        "summary": r"(professional summary|summary|about me|profile|objective)",
        "skills": r"(technical skills|skills|technologies|core competencies|tools & skills)",
        "experience": r"(work experience|experience|professional experience|employment history|internships)",
        "education": r"(education|academic background|qualifications|degrees)",
        "projects": r"(projects|key projects|academic projects|technical projects|portfolio)",
        "certifications": r"(certifications|certificates|licenses|accreditations)"
    }

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    current_section = None
    section_buffers: Dict[str, List[str]] = {k: [] for k in sections}

    for line in lines:
        matched_section = None
        # Check if line looks like a header (short, capitalized or matches pattern)
        if len(line) < 40:
            for sec_name, pattern in heading_patterns.items():
                if re.fullmatch(pattern, line.lower().strip(": ")):
                    matched_section = sec_name
                    break

        if matched_section:
            current_section = matched_section
        elif current_section:
            section_buffers[current_section].append(line)
        else:
            # Preliminary header lines (contact info / headline)
            section_buffers["summary"].append(line)

    for k in sections:
        sections[k] = "\n".join(section_buffers[k]).strip()

    return sections


def analyze_bullet_points(text: str) -> List[Dict[str, Any]]:
    """Deep analysis of experience and project bullet points."""
    bullet_results = []
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    # Extract lines that look like bullet points or list items
    bullet_candidates = []
    for line in lines:
        clean = re.sub(r"^[-*•–—\d\.\)]\s*", "", line).strip()
        if len(clean) > 25:
            bullet_candidates.append(clean)

    for bullet in bullet_candidates[:12]:
        lower_b = bullet.lower()
        first_word = lower_b.split()[0] if lower_b.split() else ""

        # Check action verb
        has_strong_verb = any(v in lower_b[:30] for v in STRONG_ACTION_VERBS)
        has_weak_verb = any(v in lower_b[:30] for v in WEAK_PASSIVE_VERBS)

        # Check quantitative metric
        has_metric = bool(re.search(r"(\d+%\b|\$\d+|\b\d+\s*(users|clients|ms|seconds|hours|x|gb|tb|rows|records|models)\b|\b\d{2,}\b)", lower_b))

        # Check impact indicator
        has_impact = any(k in lower_b for k in ["resulting in", "improving", "reducing", "increasing", "achieving", "enabling", "by"])

        if has_strong_verb and has_metric:
            status = "Strong"
            score = 90
            feedback = "Excellent! Uses a decisive action verb and measurable business/technical impact."
            rewrite = None
        elif has_strong_verb and not has_metric:
            status = "Needs Improvement"
            score = 65
            feedback = "Good action verb, but lacks quantifiable evidence (e.g. latency reduced, dataset size, percentage improvement)."
            rewrite = f"Quantify the outcome: e.g. '{bullet} — improving efficiency by X% across N datasets.'"
        elif has_weak_verb:
            status = "Weak"
            score = 40
            feedback = "Begins with a passive or vague phrase ('helped', 'worked on', 'responsible for'). Take ownership of your technical contribution."
            rewrite = f"Replace passive verb with an engineering action: e.g. 'Engineered...' or 'Designed...' instead of '{first_word.capitalize()}'."
        else:
            status = "Needs Improvement"
            score = 60
            feedback = "Ensure this bullet clearly states: What you built, how you built it (tech stack), and what the measured result was."
            rewrite = f"Apply Google XYZ format: 'Accomplished [Impact] as measured by [Metric] by implementing [Technology].'"

        bullet_results.append({
            "original": bullet,
            "status": status,
            "score": score,
            "feedback": feedback,
            "suggested_rewrite": rewrite
        })

    return bullet_results


def calculate_resume_readiness(contact: Dict[str, Any], skills: Dict[str, List[str]],
                               sections: Dict[str, str], bullets: List[Dict[str, Any]]) -> Tuple[int, List[str], List[str]]:
    """Compute structural ATS readiness score (0-100) with honest explanations."""
    score = 0
    strengths = []
    improvements = []

    # 1. Contact info (max 15)
    contact_points = 0
    if contact.get("email"):
        contact_points += 5
    if contact.get("phone"):
        contact_points += 5
    if contact.get("linkedin") or contact.get("github"):
        contact_points += 5
    score += contact_points

    if contact_points == 15:
        strengths.append("Complete contact profile with professional portfolio links.")
    else:
        improvements.append("Add missing contact channels (Email, Phone, or GitHub/LinkedIn links).")

    # 2. Technical Skills Section (max 25)
    total_skills_count = sum(len(v) for v in skills.values())
    if total_skills_count >= 12:
        score += 25
        strengths.append(f"Strong, diverse technical skill representation ({total_skills_count} verified tools detected).")
    elif total_skills_count >= 6:
        score += 18
        improvements.append("Expand technical stack to highlight specialized frameworks, cloud tools, or libraries.")
    else:
        score += 8
        improvements.append("Very few technical skills detected. Ensure technologies are explicitly listed in a dedicated section.")

    # 3. Section Completeness (max 30)
    has_exp = len(sections.get("experience", "")) > 50
    has_edu = len(sections.get("education", "")) > 30
    has_proj = len(sections.get("projects", "")) > 50

    if has_exp:
        score += 10
        strengths.append("Clear work/internship experience section identified.")
    else:
        improvements.append("No distinct work or internship experience section identified.")

    if has_edu:
        score += 10
        strengths.append("Education and academic background verified.")
    else:
        improvements.append("Education section is missing or unclear.")

    if has_proj:
        score += 10
        strengths.append("Portfolio projects section is clearly delineated.")
    else:
        improvements.append("Add a dedicated Projects section to demonstrate hands-on software proof-of-work.")

    # 4. Bullet Point Quality (max 30)
    if bullets:
        strong_bullets = sum(1 for b in bullets if b["status"] == "Strong")
        ratio = strong_bullets / len(bullets)
        bullet_score = int(ratio * 30)
        score += bullet_score
        if ratio >= 0.5:
            strengths.append(f"{strong_bullets} of {len(bullets)} sampled bullets feature measurable metrics and strong action verbs.")
        else:
            improvements.append("Most bullet points lack quantified impact metrics (percentages, speedups, user metrics).")
    else:
        score += 10
        improvements.append("Could not extract distinct bullet points for impact evaluation.")

    final_score = min(max(score, 10), 98)
    return final_score, strengths, improvements


def parse_resume_complete(file_bytes: bytes, filename: str) -> Dict[str, Any]:
    """Execute complete analysis pipeline on uploaded resume bytes."""
    file_size_kb = round(len(file_bytes) / 1024, 1)

    if filename.lower().endswith(".pdf"):
        text, error = extract_text_from_pdf(file_bytes)
    elif filename.lower().endswith(".docx"):
        text, error = extract_text_from_docx(file_bytes)
    else:
        return {"error": "Unsupported file format. Please upload a .pdf or .docx document."}

    if error:
        return {"error": error}

    if len(text.strip()) < 50:
        return {"error": "The uploaded resume file contains insufficient readable text."}

    contact = extract_contact_info(text)
    skills = extract_skills_from_text(text)
    sections = parse_resume_sections(text)
    bullets = analyze_bullet_points(text)
    readiness_score, strengths, improvements = calculate_resume_readiness(contact, skills, sections, bullets)

    return {
        "file_name": filename,
        "file_size_kb": file_size_kb,
        "raw_text": text,
        "contact": contact,
        "skills_categorized": skills,
        "sections": sections,
        "bullets_analysis": bullets,
        "readiness_score": readiness_score,
        "strengths": strengths,
        "improvements": improvements
    }

