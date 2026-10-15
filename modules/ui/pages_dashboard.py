"""
Career Copilot AI - Dashboard Page Module
Renders welcoming hero, overview KPI cards, 6-step career journey, and recent activity feed.
All UI elements are native Streamlit components for maximum reliability and clean styling.
"""

import streamlit as st
from modules.ui.components import (
    render_metric_card, render_journey_steps
)
from modules.storage.database import (
    get_user_profile, get_active_resume, get_latest_job_analysis,
    get_recent_activities, get_completed_tasks_count, get_application_counts
)
from modules.data.roadmap_data import get_total_roadmap_tasks


def render_dashboard():
    """Render the main executive overview dashboard."""
    profile = get_user_profile()
    active_resume = get_active_resume()
    latest_job = get_latest_job_analysis()
    recent_acts = get_recent_activities(limit=5)
    app_counts = get_application_counts()

    target_role = profile.get("target_role", "Engineering Professional")
    completed_tasks = get_completed_tasks_count(target_role)
    total_tasks = get_total_roadmap_tasks(target_role)
    roadmap_pct = int((completed_tasks / max(total_tasks, 1)) * 100)

    # Hero Section using Native Streamlit Container
    with st.container(border=True):
        st.caption("🧭 MULTI-DISCIPLINARY CAREER COPILOT")
        st.title("Build your next career move with confidence.")
        st.write(
            "Analyze your skills, match employer job descriptions, discover the right engineering or medical career paths, "
            "and turn your career goals into an actionable, verified plan."
        )

        cta_col1, cta_col2, cta_col_spacer = st.columns([1.5, 1.5, 3])
        with cta_col1:
            if st.button("Analyze My Resume", key="hero_btn_resume", type="primary", use_container_width=True):
                st.session_state["nav_selection"] = "Resume Analyzer"
                st.rerun()
        with cta_col2:
            if st.button("Explore Career Roles", key="hero_btn_careers", use_container_width=True):
                st.session_state["nav_selection"] = "Career Role Explorer"
                st.rerun()

    st.divider()

    # 4 Overview Cards (Readiness, Job Match, Skills to Improve, Learning Progress)
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        if active_resume:
            readiness = active_resume.get("readiness_score", 0)
            status_text = "Good ATS Baseline" if readiness >= 70 else "Needs Optimization"
            badge_color = "success" if readiness >= 70 else "warning"
            render_metric_card("Resume Readiness", f"{readiness}%", status_text, badge_color)
        else:
            render_metric_card("Resume Readiness", "No Resume", "Upload resume to score", "navy")

    with m2:
        if latest_job:
            match_score = int(latest_job.get("match_score", 0))
            render_metric_card("Job Match Overview", f"{match_score}%", f"Matched vs {latest_job.get('job_title', 'Job')[:14]}", "sky")
        else:
            render_metric_card("Job Match Overview", "--", "Add job description to test", "navy")

    with m3:
        if latest_job and "analysis" in latest_job:
            missing_count = len(latest_job["analysis"].get("missing_required", []))
            badge = "warning" if missing_count > 0 else "success"
            render_metric_card("Skills to Improve", str(missing_count), f"{missing_count} priority gaps identified", badge)
        elif active_resume:
            render_metric_card("Skills to Improve", "0 Gaps", "Match with JD to evaluate", "sky")
        else:
            render_metric_card("Skills to Improve", "--", "Pending analysis", "navy")

    with m4:
        sub = f"{completed_tasks} of {total_tasks} milestones completed"
        render_metric_card("Learning Progress", f"{roadmap_pct}%", sub, "sky" if roadmap_pct > 0 else "navy")

    st.divider()

    # Two column layout: 6-step Journey on Left, Recent Activity & Target Role on Right
    left_col, right_col = st.columns([1.6, 1])

    with left_col:
        # Determine current journey step
        step_idx = 1
        if active_resume and not latest_job:
            step_idx = 2
        elif latest_job and roadmap_pct == 0:
            step_idx = 3
        elif roadmap_pct > 0 and app_counts["Total"] == 0:
            step_idx = 5
        elif app_counts["Total"] > 0:
            step_idx = 6

        render_journey_steps(current_step=step_idx)

    with right_col:
        st.subheader("Target Role & Profile")
        with st.container(border=True):
            col_p1, col_p2 = st.columns([0.7, 0.3])
            with col_p1:
                st.markdown(f"### {profile.get('target_role', 'Engineering Professional')}")
            with col_p2:
                st.info(f"**{profile.get('experience_level', 'Entry Level')}**")

            st.write(profile.get('summary', 'Focused on building strong verified technical and domain competencies.'))
            st.caption(f"⚡ Weekly Commitment: **{profile.get('weekly_study_hours', 12)} hours**  |  Active 4-Week Track")

        st.subheader("Recent Activity")
        if recent_acts:
            for act in recent_acts:
                with st.container(border=True):
                    c_act_t, c_act_d = st.columns([0.75, 0.25])
                    with c_act_t:
                        st.markdown(f"**{act.get('title', '')}**")
                        st.caption(act.get('description', ''))
                    with c_act_d:
                        st.caption(f"`{act.get('action_type', 'Action')}`")
                        st.caption(str(act.get('timestamp', ''))[:16])
        else:
            with st.container(border=True):
                st.caption("No recent activities recorded yet. Start by uploading a resume or checking a job description!")
