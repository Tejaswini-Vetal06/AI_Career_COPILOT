"""
Career Copilot AI - Skills Gap Analysis Page Module
Segments competencies into:
1. Skills Already Demonstrated
2. Skills Requiring Improvement
3. Skills Not Yet Demonstrated
Provides learning resources, exercises, and project applications with nuanced evaluations
rendered entirely using native Streamlit containers and clean standard markdown.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_empty_state
)
from modules.storage.database import get_active_resume, get_latest_job_analysis, get_user_profile


def render_skills_gap():
    """Render Skills Gap Analysis page with 100% native UI elements."""
    render_page_header(
        title="Skills Gap Analysis",
        subtitle="Prioritized diagnostic of demonstrated competencies, improvement areas, and targeted practice exercises.",
        breadcrumb="Career Copilot AI / Skills Gap Analysis",
        badge_text="Skill Intelligence"
    )

    latest_job = get_latest_job_analysis()
    active_resume = get_active_resume()
    profile = get_user_profile()

    if not latest_job:
        render_empty_state(
            title="No Job Match Analysis Found",
            message="Run a Job Description Match first to evaluate your demonstrated skills against real employer requirements.",
            action_label="Go to Job Description Matcher"
        )
        if st.session_state.get("btn_empty_no_job_match_analysis_found"):
            st.session_state["nav_selection"] = "Job Description Matcher"
            st.rerun()
        return

    analysis = latest_job.get("analysis", {})
    demonstrated = analysis.get("demonstrated_skills", [])
    to_improve = analysis.get("to_improve_skills", [])
    not_demonstrated = analysis.get("not_demonstrated_skills", [])
    prioritized_gaps = analysis.get("prioritized_gaps", [])

    # Overview Banner with Nuanced Evaluation Principle
    st.info(
        "**Nuanced Assessment Principle:** Career Copilot AI does not deem you unqualified simply because a specific keyword is absent. "
        "Transferable problem-solving ability, engineering fundamentals, and demonstrable projects are prioritized over exact keyword matching."
    )

    # 3 Summary Buckets
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.metric("Demonstrated Skills", len(demonstrated))
            st.caption("✅ Evidenced with practical bullets in your resume.")

    with col2:
        with st.container(border=True):
            st.metric("Requires Improvement", len(to_improve))
            st.caption("💡 Mentioned, but needs quantitative impact evidence.")

    with col3:
        with st.container(border=True):
            st.metric("Not Yet Demonstrated", len(not_demonstrated))
            st.caption("⚠️ Absent from resume text; candidate for targeted learning.")

    st.divider()

    # Prioritized Detailed Skill Gap Action Cards
    st.subheader("Actionable Learning & Practice Roadmap")

    if prioritized_gaps:
        for item in prioritized_gaps:
            status_text = item.get("status", "Skill Gap")
            is_priority_high = "High" in item.get("priority", "")

            with st.container(border=True):
                c_title, c_badge = st.columns([0.75, 0.25])
                with c_title:
                    st.markdown(f"### {item['skill']}")
                    priority_label = f"🔴 **{item.get('priority', 'Medium')}**" if is_priority_high else f"🟡 **{item.get('priority', 'Medium')}**"
                    st.caption(f"Priority: {priority_label}  |  Status: `{status_text}`")
                with c_badge:
                    if status_text == "Needs Improvement":
                        st.warning(f"**{status_text}**")
                    else:
                        st.error(f"**{status_text}**")

                st.markdown(f"**Why it matters:** {item.get('why_matters', 'Required capability for this role.')}")

                col_res, col_ex, col_proj = st.columns(3)
                with col_res:
                    st.markdown("**Suggested Resource:**")
                    res_name = item.get("resource", "Official Documentation")
                    res_url = item.get("resource_url", "#")
                    st.markdown(f"🔗 [{res_name}]({res_url})")

                with col_ex:
                    st.markdown("**Practice Exercise:**")
                    st.write(item.get("exercise", "Build a focused practical prototype."))

                with col_proj:
                    st.markdown("**Applied Project:**")
                    st.write(item.get("project", "Incorporate into active portfolio."))
    else:
        st.success("No critical skill gaps identified between your resume and the target position! Your demonstrated skills align strongly with this job.")
