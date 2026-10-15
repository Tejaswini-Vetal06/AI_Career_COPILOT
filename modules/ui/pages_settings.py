"""
Career Copilot AI - Settings & User Profile Page Module
Provides user profile configuration, optional Gemini AI API key setup,
data export in JSON, and database reset tools.
"""

import streamlit as st
import json
import os
from modules.ui.components import render_page_header
from modules.storage.database import (
    get_user_profile, update_user_profile, reset_all_data,
    get_all_applications, get_active_resume
)
from modules.data.roles_data import get_role_titles


def render_settings():
    """Render the Settings & Configuration page."""
    render_page_header(
        title="Settings & Profile",
        subtitle="Manage your career target goals, optional AI intelligence keys, and persistent local data storage.",
        breadcrumb="Career Copilot AI / Settings",
        badge_text="System Configuration"
    )

    profile = get_user_profile()
    roles = get_role_titles()

    tab_profile, tab_ai, tab_data = st.tabs(["User Profile", "AI Model Provider", "Data Management"])

    with tab_profile:
        render_profile_tab(profile, roles)

    with tab_ai:
        render_ai_provider_tab()

    with tab_data:
        render_data_tab(profile)


def render_profile_tab(profile, roles):
    """User profile edit form."""
    st.markdown("""
    <div class="copilot-card">
        <h3 style="font-size: 1.05rem; color: #123B63; margin: 0 0 0.75rem 0;">Professional Profile</h3>
    """, unsafe_allow_html=True)

    with st.form("form_profile_settings"):
        c1, c2 = st.columns(2)
        with c1:
            full_name = st.text_input("Full Name", value=profile.get("full_name", "Alex Mercer"))
            email = st.text_input("Email Address", value=profile.get("email", "alex.mercer@example.com"))
            headline = st.text_input("Professional Headline", value=profile.get("headline", "Aspiring Machine Learning Engineer"))
        with c2:
            target_role = st.selectbox(
                "Primary Target Role",
                roles,
                index=roles.index(profile.get("target_role", "Machine Learning Engineer")) if profile.get("target_role") in roles else 1
            )
            exp_opts = ["Entry Level (0-2 yrs)", "Mid Level (2-5 yrs)", "Senior Level (5+ yrs)", "Student / Recent Graduate"]
            current_exp = profile.get("experience_level", "Entry Level (0-2 yrs)")
            experience_level = st.selectbox("Experience Tier", exp_opts, index=exp_opts.index(current_exp) if current_exp in exp_opts else 0)
            weekly_study_hours = st.slider("Weekly Study Hours", min_value=2, max_value=40, value=profile.get("weekly_study_hours", 12))

        summary = st.text_area("Career Objective / Bio", value=profile.get("summary", ""), height=90)

        saved = st.form_submit_button("Save Profile Settings", type="primary")
        if saved:
            update_user_profile(
                full_name=full_name,
                email=email,
                headline=headline,
                target_role=target_role,
                experience_level=experience_level,
                weekly_study_hours=weekly_study_hours,
                summary=summary
            )
            st.success("Profile updated successfully!")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def render_ai_provider_tab():
    """Optional Google Gemini API Key configuration."""
    st.markdown("""
    <div class="copilot-card">
        <h3 style="font-size: 1.05rem; color: #123B63; margin: 0 0 0.5rem 0;">AI Inference Architecture</h3>
        <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 1rem; line-height: 1.45;">
            Career Copilot AI operates with a <b>100% self-contained local Python baseline</b> (TF-IDF, Scikit-Learn, regex NLP, and heuristics).
            Optionally configure a Google Gemini API key to unlock advanced generative insights and deep natural language feedback.
        </p>
    </div>
    """, unsafe_allow_html=True)

    current_key = os.environ.get("GEMINI_API_KEY", "")
    masked_key = (current_key[:6] + "..." + current_key[-4:]) if len(current_key) > 10 else ""

    col_key, col_status = st.columns([2, 1])
    with col_key:
        api_key_input = st.text_input(
            "Google Gemini API Key (Optional)",
            type="password",
            placeholder="Enter AI Studio API Key (or set GEMINI_API_KEY in environment)",
            help="Get an API key from https://aistudio.google.com/"
        )

        if st.button("Save API Key to Session", key="btn_save_key"):
            if api_key_input.strip():
                st.session_state["gemini_api_key"] = api_key_input.strip()
                st.success("API key stored securely in active session memory.")
            else:
                st.warning("Please enter a valid key.")

    with col_status:
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1rem; font-size: 0.82rem;">
            <b>Active Inference Engine:</b><br>
            <span style="color: #16A34A; font-weight: 700;">Local Scikit-Learn Engine</span><br><br>
            <b>Gemini API Status:</b><br>
            <span style="color: {'#16A34A' if (current_key or st.session_state.get('gemini_api_key')) else '#64748B'};">
                {'Connected' if (current_key or st.session_state.get('gemini_api_key')) else 'Not Configured (Using Local)'}
            </span>
        </div>
        """, unsafe_allow_html=True)


def render_data_tab(profile):
    """Local SQLite Data Management & Export."""
    st.markdown("""
    <div class="copilot-card">
        <h3 style="font-size: 1.05rem; color: #123B63; margin: 0 0 0.5rem 0;">Local Data Storage & Privacy</h3>
        <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 1rem;">
            All your resumes, matches, roadmap completions, and application records are stored locally in an embedded SQLite database (<code>data/career_copilot.db</code>).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Export User Data
    active_resume = get_active_resume()
    apps = get_all_applications()
    export_payload = {
        "profile": profile,
        "active_resume_summary": {
            "file_name": active_resume.get("file_name") if active_resume else None,
            "readiness_score": active_resume.get("readiness_score") if active_resume else None
        },
        "applications_count": len(apps),
        "applications": apps
    }
    export_json = json.dumps(export_payload, indent=2)

    c_export, c_reset = st.columns(2)
    with c_export:
        st.download_button(
            label="Export All My Data (JSON)",
            data=export_json,
            file_name="career_copilot_data_export.json",
            mime="application/json",
            use_container_width=True
        )

    with c_reset:
        if st.button("Reset All Saved Data to Default", type="secondary", use_container_width=True, key="btn_reset_all"):
            reset_all_data()
            st.success("All data tables reset to fresh installation state.")
            st.rerun()

