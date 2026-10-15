"""
Career Copilot AI - Resume Analyzer Page Module
Provides PDF/DOCX drag-and-drop upload, section-by-section breakdown,
weak bullet point detection, ATS structural readiness, and honest improvement suggestions.
Rendered entirely using native Streamlit containers and components.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_skill_badges, render_metric_card, render_empty_state
)
from modules.parsers.resume_parser import parse_resume_complete
from modules.storage.database import save_resume, get_active_resume, get_all_resumes, set_active_resume


def render_resume_analyzer():
    """Render the Resume Analyzer page with clean native UI."""
    render_page_header(
        title="Resume Analyzer",
        subtitle="Upload your PDF or DOCX resume to extract technical credentials, audit bullet strength, and optimize for ATS.",
        breadcrumb="Career Copilot AI / Resume Analyzer",
        badge_text="Parser Engine v2"
    )

    tab_upload, tab_improver, tab_history = st.tabs(["Analyze Resume", "AI Bullet Point Improver", "Upload History & Switch Active"])

    with tab_upload:
        render_upload_section()

    with tab_improver:
        render_bullet_improver_section()

    with tab_history:
        render_history_section()


def render_upload_section():
    """Render upload form and active parsed resume results using native containers."""
    with st.container(border=True):
        st.subheader("Upload & Parse Resume")
        st.write("Accepts text-based **.PDF** and **.DOCX** files. Scanned images without extractable OCR text are rejected for factual fidelity.")

        uploaded_file = st.file_uploader(
            "Choose your resume file",
            type=["pdf", "docx"],
            help="Upload standard PDF or Word document",
            key="resume_file_uploader"
        )

        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            filename = uploaded_file.name

            if st.button("Parse & Analyze Resume", type="primary", key="btn_parse_resume"):
                with st.spinner("Extracting sections, verifying technical skills, and analyzing bullet points..."):
                    analysis_result = parse_resume_complete(file_bytes, filename)

                    if "error" in analysis_result:
                        st.error(f"Extraction Error: {analysis_result['error']}")
                    else:
                        save_resume(
                            file_name=filename,
                            file_size_kb=analysis_result["file_size_kb"],
                            raw_text=analysis_result["raw_text"],
                            extracted_data=analysis_result,
                            readiness_score=analysis_result["readiness_score"]
                        )
                        st.success(f"Successfully parsed '{filename}' ({analysis_result['file_size_kb']} KB)")
                        st.rerun()

    # Display Active Resume Details
    active = get_active_resume()
    if not active:
        render_empty_state(
            title="No Active Resume Loaded",
            message="Upload a PDF or DOCX resume file above to see extracted technical skills, bullet point impact evaluations, and structural ATS suggestions."
        )
        return

    data = active.get("extracted_data", {})
    score = active.get("readiness_score", 0)

    st.divider()

    # Top KPI Metrics row
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        badge = "success" if score >= 75 else "warning"
        render_metric_card("ATS Readiness", f"{score}/100", "Structural Integrity", badge)
    with kpi2:
        skills_count = sum(len(v) for v in data.get("skills_categorized", {}).values())
        render_metric_card("Verified Skills", str(skills_count), "Extracted Tools", "sky")
    with kpi3:
        bullets = data.get("bullets_analysis", [])
        strong_count = sum(1 for b in bullets if b.get("status") == "Strong")
        render_metric_card("Strong Bullets", f"{strong_count}/{len(bullets)}", "Metric + Action Verb", "success" if strong_count > 0 else "warning")
    with kpi4:
        render_metric_card("Active Document", active.get("file_name", "Resume.pdf")[:18], f"{active.get('file_size_kb', 0)} KB", "navy")

    # Two column review
    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        # Candidate Overview Card
        with st.container(border=True):
            st.subheader("Extracted Candidate Profile")
            contact = data.get("contact", {})
            c_e1, c_e2 = st.columns(2)
            with c_e1:
                st.markdown(f"**Email:** {contact.get('email') or 'Not detected in header'}")
                st.markdown(f"**Phone:** {contact.get('phone') or 'Not detected in header'}")
            with c_e2:
                st.markdown(f"**GitHub:** {contact.get('github') or 'Not linked'}")
                st.markdown(f"**LinkedIn:** {contact.get('linkedin') or 'Not linked'}")

        # Categorized Technical Skills
        with st.container(border=True):
            st.subheader("Extracted Technical Skills")
            st.caption("Categorized by domain across engineering and healthcare taxonomies.")

            cat_skills = data.get("skills_categorized", {})
            if cat_skills:
                for cat_name, skill_list in cat_skills.items():
                    st.markdown(f"**{cat_name} ({len(skill_list)})**")
                    render_skill_badges(skill_list, category="default")
            else:
                st.info("No standard technical skills identified in the document text.")

        # Bullet Point Quality Audit
        st.subheader("Bullet Point Quality Audit")
        st.caption("Evaluating bullet points against the Google XYZ formula: *Accomplished [X] as measured by [Y] by doing [Z]*.")

        bullets_data = data.get("bullets_analysis", [])
        if bullets_data:
            for b in bullets_data:
                status = b.get("status", "Needs Improvement")
                with st.container(border=True):
                    c_b_title, c_b_badge = st.columns([0.8, 0.2])
                    with c_b_title:
                        st.markdown(f"**\"{b.get('original', '')}\"**")
                    with c_b_badge:
                        if status == "Strong":
                            st.success(f"**{status}**")
                        elif status == "Weak":
                            st.error(f"**{status}**")
                        else:
                            st.warning(f"**{status}**")

                    st.write(b.get("feedback", ""))
                    if b.get("suggested_rewrite"):
                        st.info(f"💡 **Suggested Action:** {b['suggested_rewrite']}")
        else:
            st.info("No distinct bullet points were identified for line-by-line quality auditing.")

    with col_right:
        # Strengths & Missing Information
        with st.container(border=True):
            st.subheader("ATS Optimization Checklist")

            strengths = data.get("strengths", [])
            if strengths:
                st.markdown("**Verified Strengths:**")
                for s in strengths:
                    st.markdown(f"- ✅ {s}")

            improvements = data.get("improvements", [])
            if improvements:
                st.markdown("**Recommended Improvements:**")
                for imp in improvements:
                    st.markdown(f"- ⚠️ {imp}")

        # Extracted Sections Raw View
        with st.expander("View Raw Extracted Sections", expanded=False):
            sections = data.get("sections", {})
            for sec_name, content in sections.items():
                st.markdown(f"**{sec_name.upper()}**")
                if content:
                    st.text(content[:350] + ("..." if len(content) > 350 else ""))
                else:
                    st.caption("Section was not detected by parser.")


def render_history_section():
    """Render list of past uploaded resumes with ability to switch active resume."""
    resumes = get_all_resumes()
    if not resumes:
        st.info("No uploaded resume history found.")
        return

    st.subheader("Saved Resumes")

    for r in resumes:
        is_active = bool(r["is_active"])
        with st.container(border=True):
            col_info, col_btn = st.columns([0.75, 0.25])
            with col_info:
                active_tag = " [ACTIVE]" if is_active else ""
                st.markdown(f"**{r['file_name']}{active_tag}**")
                st.caption(f"ATS Score: {r['readiness_score']}%  |  Size: {r['file_size_kb']} KB  |  Uploaded: {str(r['uploaded_at'])[:16]}")
            with col_btn:
                if not is_active:
                    if st.button("Set Active", key=f"btn_activate_{r['id']}"):
                        set_active_resume(r["id"])
                        st.rerun()
                else:
                    st.success("Currently Active")


def render_bullet_improver_section():
    """Interactive tool to transform weak bullet points into high-impact engineering accomplishments."""
    from modules.agent.bullet_improver import improve_bullet_point
    from modules.storage.database import get_user_profile, get_latest_job_analysis

    profile = get_user_profile()
    latest_job = get_latest_job_analysis()
    target_role = profile.get("target_role", "Machine Learning Engineer")

    # Get keywords from latest job if present
    keywords = ["AutoCAD", "SolidWorks", "Python", "FastAPI"]
    if latest_job and "analysis" in latest_job:
        missing = latest_job["analysis"].get("missing_required", [])
        if missing:
            keywords = missing[:4]

    with st.container(border=True):
        st.subheader("AI Bullet Point Improver")
        st.caption("Turn passive descriptions into verifiable, metric-driven achievements for your target discipline.")

    c1, c2 = st.columns([1.3, 1])

    with c1:
        default_bullet = "Worked on engineering calculations and helped team deliver project on schedule."
        bullet_input = st.text_area("Original Bullet Point:", value=default_bullet, height=90, key="txt_bullet_input")

        style_opts = [
            "Google XYZ Formula",
            "Senior Engineering & Scalability",
            "Job-Targeted Keyword Alignment",
            "Executive Brevity & Action"
        ]
        selected_style = st.selectbox("Enhancement Strategy:", style_opts, index=0, key="sel_bullet_style")

        if st.button("Enhance Bullet Point with AI", type="primary", key="btn_run_bullet_agent"):
            with st.spinner("Reframing with action verbs, quantifiable metrics, and architecture patterns..."):
                res = improve_bullet_point(
                    bullet_text=bullet_input,
                    style=selected_style,
                    target_role=target_role,
                    target_keywords=keywords
                )
                st.session_state["active_bullet_improvement"] = res
                st.rerun()

    with c2:
        res = st.session_state.get("active_bullet_improvement")
        if not res:
            with st.container(border=True):
                st.subheader("✨ Awaiting Optimization")
                st.write("Click 'Enhance Bullet Point with AI' on the left to see instant transformations and architectural rationales.")
            return

        with st.container(border=True):
            st.caption("RECOMMENDED OPTIMIZATION")
            st.markdown(f"### \"{res['primary_recommendation']}\"")
            st.info(f"**Why this works:** {res['rationale']}")
            st.caption(f"Engine: {res.get('engine_used', 'Local Agentic Optimizer')}")

        with st.expander("View Alternative Style Variations", expanded=False):
            for var in res.get("all_variations", []):
                if var["style"] != res["selected_style"]:
                    st.markdown(f"**{var['style']}:**")
                    st.markdown(f"*{var['text']}*")
                    st.divider()
