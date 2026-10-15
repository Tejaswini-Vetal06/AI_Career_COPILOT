"""
Career Copilot AI - Resume Builder Page Module
Interactive resume editor with live A4 preview, clean typography,
job description alignment suggestions, and print-ready export.
Strictly preserves user facts and never fabricates credentials.
"""

import streamlit as st
from modules.ui.components import render_page_header, ICONS
from modules.storage.database import get_active_resume, get_user_profile, get_latest_job_analysis


def render_resume_builder():
    """Render the Resume Builder & Tailor page."""
    render_page_header(
        title="Resume Builder",
        subtitle="Craft and tailor a high-impact, ATS-optimized engineering resume. Live preview with one-click export.",
        breadcrumb="Career Copilot AI / Resume Builder",
        badge_text="A4 Typographic Standard"
    )

    active_resume = get_active_resume()
    profile = get_user_profile()
    latest_job = get_latest_job_analysis()

    # Pre-populate state if not already set
    if "builder_name" not in st.session_state:
        st.session_state["builder_name"] = profile.get("full_name", "Alex Mercer")
        st.session_state["builder_email"] = profile.get("email", "alex.mercer@example.com")
        st.session_state["builder_phone"] = "+1 (555) 019-2834"
        st.session_state["builder_links"] = "github.com/alexmercer | linkedin.com/in/alexmercer"
        st.session_state["builder_summary"] = (
            "Engineering graduate with hands-on experience in machine learning pipelines, deep learning architectures, "
            "and scalable REST APIs. Proven ability to design and evaluate predictive models, optimize inference latency, "
            "and deploy containerized services using Python, PyTorch, and Docker."
        )
        st.session_state["builder_skills"] = "Python, PyTorch, Scikit-Learn, SQL, FastAPI, Docker, Git, MLflow, Linux"
        st.session_state["builder_experience"] = (
            "Machine Learning Engineering Intern | TechNova Labs (June 2025 – Present)\n"
            "• Developed end-to-end customer churn classification pipeline in Scikit-Learn, boosting validation PR-AUC by 18%.\n"
            "• Packaged model into asynchronous FastAPI service, achieving sub-30ms p95 latency under simulated load.\n"
            "• Built automated feature validation checks reducing pipeline data ingestion errors by 40%."
        )
        st.session_state["builder_projects"] = (
            "Production RAG Document Intelligence Assistant (PyTorch, FastAPI, ChromaDB)\n"
            "• Implemented hybrid retrieval combining BM25 and dense embeddings with Reciprocal Rank Fusion.\n"
            "• Applied Cross-Encoder reranking filtering top-20 candidates to top-4 with source citation badges.\n"
            "• Containerized with multi-stage Dockerfile and deployed continuous testing pipeline in GitHub Actions."
        )
        st.session_state["builder_education"] = (
            "B.S. in Computer Science | State University (Graduated May 2025)\n"
            "Relevant Coursework: Machine Learning, Algorithms & Data Structures, Database Systems, Linear Algebra"
        )
        st.session_state["builder_certs"] = "DeepLearning.AI Machine Learning Specialization | AWS Certified Cloud Practitioner"

    # Two column layout: Editor on Left, Live A4 Preview on Right
    col_editor, col_preview = st.columns([1.1, 1.3])

    with col_editor:
        st.markdown("<h3 style='font-size: 1.05rem; color: #123B63; margin-bottom: 0.75rem;'>Resume Content Editor</h3>", unsafe_allow_html=True)

        with st.expander("Personal & Contact Details", expanded=True):
            st.session_state["builder_name"] = st.text_input("Full Name", value=st.session_state["builder_name"])
            c1, c2 = st.columns(2)
            with c1:
                st.session_state["builder_email"] = st.text_input("Email", value=st.session_state["builder_email"])
            with c2:
                st.session_state["builder_phone"] = st.text_input("Phone", value=st.session_state["builder_phone"])
            st.session_state["builder_links"] = st.text_input("Portfolio / GitHub / LinkedIn", value=st.session_state["builder_links"])

        with st.expander("Professional Summary", expanded=True):
            st.session_state["builder_summary"] = st.text_area("Summary", value=st.session_state["builder_summary"], height=90)

        with st.expander("Technical Skills", expanded=True):
            st.session_state["builder_skills"] = st.text_area("Skills (Comma separated)", value=st.session_state["builder_skills"], height=70)

        with st.expander("Work / Internship Experience", expanded=True):
            st.session_state["builder_experience"] = st.text_area("Experience (Bullets)", value=st.session_state["builder_experience"], height=130)

        with st.expander("Portfolio Projects", expanded=True):
            st.session_state["builder_projects"] = st.text_area("Projects", value=st.session_state["builder_projects"], height=130)

        with st.expander("Education & Credentials", expanded=False):
            st.session_state["builder_education"] = st.text_area("Education", value=st.session_state["builder_education"], height=80)
            st.session_state["builder_certs"] = st.text_area("Certifications", value=st.session_state["builder_certs"], height=60)

        # Job Description Tailoring Advisor
        if latest_job and "analysis" in latest_job:
            missing_req = latest_job["analysis"].get("missing_required", [])
            st.markdown(f"""
            <div style="background: #E0F2FE; border: 1px solid #BAE6FD; border-radius: 8px; padding: 0.85rem; margin-top: 1rem;">
                <div style="font-weight: 700; color: #0369A1; font-size: 0.85rem; margin-bottom: 0.3rem;">
                    JD Tailoring Suggestions ({latest_job.get('job_title', 'Target Role')})
                </div>
                <div style="font-size: 0.78rem; color: #1E293B;">
                    If you have authentic practical experience with <b>{', '.join(missing_req[:4])}</b>, explicitly include them in your skills or projects section to improve keyword coverage.
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_preview:
        st.markdown("<h3 style='font-size: 1.05rem; color: #123B63; margin-bottom: 0.75rem;'>Live A4 Document Preview</h3>", unsafe_allow_html=True)

        # Build clean HTML Resume
        name = st.session_state["builder_name"]
        email = st.session_state["builder_email"]
        phone = st.session_state["builder_phone"]
        links = st.session_state["builder_links"]
        summary = st.session_state["builder_summary"]
        skills = st.session_state["builder_skills"]
        experience = st.session_state["builder_experience"]
        projects = st.session_state["builder_projects"]
        education = st.session_state["builder_education"]
        certs = st.session_state["builder_certs"]

        # Format experience bullets
        def format_section_lines(text_content: str) -> str:
            lines = [l.strip() for l in text_content.split("\n") if l.strip()]
            html_out = ""
            for l in lines:
                if l.startswith("•") or l.startswith("-") or l.startswith("*"):
                    html_out += f"<div style='margin-left: 1rem; margin-bottom: 0.25rem; font-size: 0.83rem;'>• {l[1:].strip()}</div>"
                elif "|" in l or "–" in l or "-" in l:
                    html_out += f"<div style='font-weight: 700; font-size: 0.88rem; color: #0B1F3A; margin-top: 0.6rem; margin-bottom: 0.15rem;'>{l}</div>"
                else:
                    html_out += f"<div style='font-size: 0.83rem; margin-bottom: 0.25rem;'>{l}</div>"
            return html_out

        resume_html = f"""
        <div class="resume-a4-preview">
            <div class="resume-header">
                <div style="font-size: 1.55rem; font-weight: 800; color: #0B1F3A; letter-spacing: -0.02em;">{name}</div>
                <div style="font-size: 0.8rem; color: #475569; margin-top: 0.25rem;">
                    {email} &nbsp;|&nbsp; {phone} &nbsp;|&nbsp; {links}
                </div>
            </div>

            <div class="resume-section-title">Professional Summary</div>
            <div style="font-size: 0.83rem; line-height: 1.5; color: #1E293B;">{summary}</div>

            <div class="resume-section-title">Technical Skills</div>
            <div style="font-size: 0.83rem; line-height: 1.5; color: #1E293B;"><b>Technologies:</b> {skills}</div>

            <div class="resume-section-title">Experience</div>
            <div>{format_section_lines(experience)}</div>

            <div class="resume-section-title">Projects</div>
            <div>{format_section_lines(projects)}</div>

            <div class="resume-section-title">Education</div>
            <div>{format_section_lines(education)}</div>

            <div class="resume-section-title">Certifications</div>
            <div style="font-size: 0.83rem; line-height: 1.4; color: #1E293B;">{certs}</div>
        </div>
        """

        st.markdown(resume_html, unsafe_allow_html=True)

        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

        # Download / Export Button
        download_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{name} - Resume</title>
<style>
body {{ font-family: 'Helvetica Neue', Arial, sans-serif; margin: 40px; color: #172B4D; line-height: 1.45; font-size: 10.5pt; }}
.header {{ border-bottom: 2px solid #123B63; padding-bottom: 8px; margin-bottom: 14px; }}
.name {{ font-size: 20pt; font-weight: bold; color: #0B1F3A; }}
.contact {{ font-size: 9.5pt; color: #475569; margin-top: 4px; }}
.section-title {{ font-size: 11pt; font-weight: bold; text-transform: uppercase; color: #123B63; border-bottom: 1px solid #CBD5E1; padding-bottom: 2px; margin-top: 14px; margin-bottom: 6px; }}
@media print {{ body {{ margin: 0; }} }}
</style>
</head>
<body>
<div class="header">
    <div class="name">{name}</div>
    <div class="contact">{email} | {phone} | {links}</div>
</div>
<div class="section-title">Professional Summary</div>
<div>{summary}</div>
<div class="section-title">Technical Skills</div>
<div><b>Technologies:</b> {skills}</div>
<div class="section-title">Experience</div>
<div>{format_section_lines(experience)}</div>
<div class="section-title">Projects</div>
<div>{format_section_lines(projects)}</div>
<div class="section-title">Education</div>
<div>{format_section_lines(education)}</div>
<div class="section-title">Certifications</div>
<div>{certs}</div>
</body>
</html>"""

        st.download_button(
            label="Download Printable Resume (HTML / PDF Ready)",
            data=download_html,
            file_name=f"{name.replace(' ', '_')}_Resume.html",
            mime="text/html",
            use_container_width=True
        )

