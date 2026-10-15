"""
Career Copilot AI - Clean Native UI Components
Provides styled presentation components built exclusively with native Streamlit elements
(containers with borders, metrics, columns, clean markdown pills, and captions)
to ensure 100% reliable rendering with zero raw HTML or SVG code leakage.
"""

import streamlit as st
from typing import List, Dict, Any, Optional

# Clean Unicode / Text symbols for icons that never leak raw SVG code
ICONS = {
    "dashboard": "📊",
    "resume": "📄",
    "match": "🎯",
    "builder": "✏️",
    "roles": "🧭",
    "gaps": "🔍",
    "projects": "📁",
    "roadmap": "🗺️",
    "jobs": "💼",
    "tracker": "📌",
    "settings": "⚙️",
    "check": "✅",
    "alert": "⚠️",
    "external": "🔗"
}


def render_page_header(title: str, subtitle: str, breadcrumb: Optional[str] = None, badge_text: Optional[str] = None):
    """Render a clean SaaS top page header using native Streamlit layout."""
    if breadcrumb:
        st.caption(f"🧭 {breadcrumb}")

    col_title, col_badge = st.columns([0.78, 0.22])
    with col_title:
        st.markdown(f"## {title}")
        st.write(subtitle)
    with col_badge:
        if badge_text:
            st.info(f"**{badge_text}**")

    st.divider()


def render_metric_card(label: str, value: str, subtext: str, badge_type: str = "sky"):
    """Render a clean SaaS KPI metric card using native Streamlit metric."""
    with st.container(border=True):
        st.metric(label=label, value=value)
        st.caption(subtext)


def render_empty_state(title: str, message: str, action_label: Optional[str] = None) -> bool:
    """Render an honest, informative empty state using native Streamlit containers."""
    with st.container(border=True):
        st.subheader(f"📋 {title}")
        st.write(message)
        if action_label:
            return st.button(action_label, key=f"btn_empty_{title.lower().replace(' ', '_')}", type="primary")
    return False


def render_skill_badges(skills: List[str], category: str = "default"):
    """Render a clean cluster of skill pills using native markdown badges."""
    if not skills:
        st.caption("None specified")
        return

    prefix_map = {
        "matched": "✅",
        "missing": "⚠️",
        "improved": "💡",
        "default": "🔹"
    }
    symbol = prefix_map.get(category, "🔹")
    formatted = "  ".join([f"`{symbol} {s}`" for s in skills])
    st.markdown(formatted)


def render_journey_steps(current_step: int = 1):
    """Render the 6-step interactive career roadmap guide using native Streamlit cards."""
    steps = [
        {"num": 1, "title": "Upload your resume", "desc": "Extract skills, experience, and get structural ATS feedback."},
        {"num": 2, "title": "Add a target job description", "desc": "Match requirements transparently and calculate coverage."},
        {"num": 3, "title": "Review your skill gaps", "desc": "Identify demonstrated vs missing skills with actionable learning paths."},
        {"num": 4, "title": "Choose a target role", "desc": "Explore core responsibilities, toolsets, and interview topics."},
        {"num": 5, "title": "Build your learning roadmap", "desc": "Track structured milestones, practical exercises, and interview prep."},
        {"num": 6, "title": "Discover projects & relevant jobs", "desc": "Build portfolio proof-of-work and apply to verified listings on Naukri & LinkedIn."}
    ]

    st.subheader("Your Career Journey")
    cols = st.columns(2)
    for i, step in enumerate(steps):
        col_idx = i % 2
        with cols[col_idx]:
            is_active = (step["num"] == current_step)
            with st.container(border=True):
                status_label = f"📍 Step {step['num']} (Current Stage)" if is_active else f"Step {step['num']}"
                st.caption(status_label)
                st.markdown(f"**{step['title']}**")
                st.write(step['desc'])


def render_sidebar_profile(profile: Dict[str, Any]):
    """Render the compact user profile at the bottom of the sidebar using native controls."""
    st.sidebar.divider()
    with st.sidebar.container():
        st.markdown(f"👤 **{profile.get('full_name', 'Professional User')}**")
        st.caption(f"🎯 Target: {profile.get('target_role', 'Engineering Professional')}")
        st.caption(f"⚡ Dedication: {profile.get('weekly_study_hours', 12)} hrs/week")
