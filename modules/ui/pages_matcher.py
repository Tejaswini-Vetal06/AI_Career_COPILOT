"""
Career Copilot AI - Job Description Matcher & Application Fit Checker
Provides a streamlined, user-friendly interface:
1. Upload resume directly or select active resume
2. Paste target Job Description (JD)
3. Check application readiness: "Is it OK to apply for this job?"
4. Inspect job-specific ATS score, matched vs missing skills, and instant tailoring advice.
Rendered entirely with native Streamlit containers and components.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_skill_badges, render_empty_state
)
from modules.storage.database import (
    get_active_resume, save_resume, save_job_analysis, get_latest_job_analysis, get_user_profile
)
from modules.parsers.resume_parser import parse_resume_complete
from modules.matching.matcher import match_resume_to_job
from modules.data.roles_data import get_role_titles


def render_job_matcher():
    """Render the streamlined Job Matcher & Application Readiness page."""
    render_page_header(
        title="Check Job Fit & ATS Score",
        subtitle="Upload your resume, paste a job description, and find out whether your profile is ready to apply.",
        breadcrumb="Career Copilot AI / Job Fit & ATS Check",
        badge_text="Readiness Evaluator"
    )

    active_resume = get_active_resume()
    profile = get_user_profile()
    roles = get_role_titles()

    # Desktop Two-Column Layout
    col_input, col_results = st.columns([1.1, 1.4])

    with col_input:
        with st.container(border=True):
            st.subheader("1. Resume & Target Job Input")
            st.caption("Upload your resume or use your active document, then paste the employer's job description.")

            # Direct File Upload in Job Matcher
            uploaded_resume_file = st.file_uploader(
                "Upload Resume (PDF or DOCX)",
                type=["pdf", "docx"],
                help="Upload a new resume directly here to test against this job",
                key="matcher_resume_uploader"
            )

            if uploaded_resume_file is not None:
                f_bytes = uploaded_resume_file.read()
                f_name = uploaded_resume_file.name
                if st.button("Parse & Use Uploaded Resume", key="btn_parse_matcher_upload", type="primary"):
                    with st.spinner("Extracting credentials from resume..."):
                        parsed = parse_resume_complete(f_bytes, f_name)
                        if "error" in parsed:
                            st.error(parsed["error"])
                        else:
                            save_resume(f_name, parsed["file_size_kb"], parsed["raw_text"], parsed, parsed["readiness_score"])
                            st.success(f"Loaded '{f_name}' as active resume!")
                            st.rerun()

            # Active Resume Status
            active_resume = get_active_resume()
            if active_resume:
                st.success(f"📄 **Active Document:** {active_resume.get('file_name')} ({active_resume.get('readiness_score')}% baseline ATS score)")
                resume_data = active_resume.get("extracted_data", {})
            else:
                st.warning("No resume file loaded yet. Please upload a PDF/DOCX above or paste text below.")
                pasted_resume = st.text_area("Or Paste Resume Text", height=120, placeholder="Paste your resume contents here...", key="txt_pasted_resume")
                resume_data = {"raw_text": pasted_resume, "skills_categorized": {}}

            st.divider()

            default_target = profile.get("target_role", "Machine Learning Engineer")
            default_idx = roles.index(default_target) if default_target in roles else 0

            target_role = st.selectbox(
                "Target Role Track",
                roles,
                index=default_idx,
                key="sel_matcher_role"
            )

            c_t, c_co = st.columns(2)
            with c_t:
                job_title = st.text_input("Job Title", value=target_role, placeholder="e.g. Structural Engineer / ML Engineer")
            with c_co:
                company_name = st.text_input("Company (Optional)", value="", placeholder="e.g. L&T, Google, Apollo Hospitals")

            default_jd = (
                f"We are hiring a qualified {target_role} to join our engineering team.\n\n"
                "Key Responsibilities & Qualifications:\n"
                "- Strong proficiency in core discipline fundamentals, standards, and practical tools.\n"
                "- Proven hands-on project execution and technical problem solving.\n"
                "- Solid analytical documentation and team collaboration skills.\n"
                "- Relevant degree (B.Tech / B.E. / MBBS / Master's) or verified industry experience."
            )

            jd_text = st.text_area(
                "Job Description (JD) *",
                value=default_jd,
                height=180,
                help="Paste the full job posting requirements and responsibilities",
                key="txt_matcher_jd"
            )

            # Prominent CTA Button
            if st.button("Check Resume Fit & ATS Score", type="primary", use_container_width=True, key="btn_run_fit_check"):
                if not jd_text.strip():
                    st.error("Please paste the job description text.")
                elif not resume_data.get("raw_text", "").strip():
                    st.error("Please upload or paste your resume text first.")
                else:
                    with st.spinner("Analyzing requirements, checking skills, and evaluating ATS fit..."):
                        match_result = match_resume_to_job(resume_data, jd_text, target_role)
                        save_job_analysis(
                            job_title=job_title,
                            company_name=company_name,
                            job_description=jd_text,
                            target_role=target_role,
                            match_score=match_result["composite_score"],
                            analysis_dict=match_result
                        )
                        st.session_state["latest_match_result"] = match_result
                        st.success(f"Analysis complete! ATS Job Fit: {match_result['composite_score']}%")
                        st.rerun()

    with col_results:
        # Display match results
        latest_analysis = get_latest_job_analysis()
        res = st.session_state.get("latest_match_result")
        if not res and latest_analysis:
            res = latest_analysis.get("analysis")

        if not res:
            render_empty_state(
                title="Ready to Check Your Fit",
                message="Click 'Check Resume Fit & ATS Score' on the left to evaluate your resume readiness, ATS match score, and identified competencies."
            )
            return

        score = res.get("composite_score", 0.0)
        verdict = res.get("application_verdict", {})
        verdict_status = verdict.get("status", "Good Potential")
        verdict_color = verdict.get("badge_color", "warning")
        verdict_summary = verdict.get("summary", "")
        action_advice = verdict.get("action_advice", "")

        # 1. Big "Is it OK to Apply?" Verdict Card
        with st.container(border=True):
            col_v1, col_v2 = st.columns([0.7, 0.3])
            with col_v1:
                st.caption("APPLICATION READINESS VERDICT")
                st.subheader(verdict_status)
            with col_v2:
                st.metric("JD ATS Score", f"{int(score)}%")

            st.write(verdict_summary)
            if verdict_color == "success":
                st.success(f"**Recommended Next Step:** {action_advice}")
            elif verdict_color == "warning":
                st.warning(f"**Recommended Next Step:** {action_advice}")
            else:
                st.error(f"**Recommended Next Step:** {action_advice}")

        # 2. Next Action Navigation Buttons
        c_act1, c_act2, c_act3 = st.columns(3)
        with c_act1:
            if st.button("Build / Tailor Resume", key="btn_verdict_builder", use_container_width=True):
                st.session_state["nav_selection"] = "Resume Builder"
                st.rerun()
        with c_act2:
            if st.button("AI Interview Coach", key="btn_verdict_coach", use_container_width=True):
                st.session_state["nav_selection"] = "AI Interview Coach (RAG)"
                st.rerun()
        with c_act3:
            if st.button("Ask AI Chatbot", key="btn_verdict_chat", use_container_width=True):
                st.session_state["nav_selection"] = "AI Career Chatbot"
                st.rerun()

        # 3. Skills Matched vs Missing Cards
        with st.container(border=True):
            st.subheader("Skills Alignment for this Job")
            st.caption("Comparing your demonstrated credentials against required and preferred skills.")

            matched_req = res.get("matched_required", [])
            missing_req = res.get("missing_required", [])

            st.markdown(f"**Required Skills You Have ({len(matched_req)})**")
            render_skill_badges(matched_req, category="matched")

            st.markdown(f"**Required Skills Missing or Not Evidenced ({len(missing_req)})**")
            if missing_req:
                render_skill_badges(missing_req, category="missing")
            else:
                st.success("All core required skills are present on your resume!")

            # Preferred Skills
            matched_pref = res.get("matched_preferred", [])
            missing_pref = res.get("missing_preferred", [])
            if matched_pref or missing_pref:
                st.markdown(f"**Preferred / Bonus Skills ({len(matched_pref)} Matched, {len(missing_pref)} Missing)**")
                render_skill_badges(matched_pref, category="matched")
                if missing_pref:
                    render_skill_badges(missing_pref, category="default")

        # 4. Tailored Bullet Guidance
        with st.container(border=True):
            st.subheader("Tailoring Tips to Boost Your ATS Score")
            suggestions = res.get("tailoring_suggestions", [])
            for sug in suggestions:
                st.markdown(f"- ✅ {sug}")
