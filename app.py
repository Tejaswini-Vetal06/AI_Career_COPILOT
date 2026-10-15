"""
Career Copilot AI - Main Application Entrypoint
A modern, responsive, engineering-focused career copilot for job seekers and engineering students.
"""

import streamlit as st

# Configure page layout and visual metadata
st.set_page_config(
    page_title="Career Copilot AI — Engineering Career Navigator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

from modules.ui.styles import get_theme_css
from modules.ui.components import render_sidebar_profile, ICONS
from modules.storage.database import get_user_profile, init_db

# Import page modules
from modules.ui.pages_dashboard import render_dashboard
from modules.ui.pages_analyzer import render_resume_analyzer
from modules.ui.pages_matcher import render_job_matcher
from modules.ui.pages_interview import render_interview_coach
from modules.ui.pages_chatbot import render_career_chatbot
from modules.ui.pages_builder import render_resume_builder
from modules.ui.pages_roles import render_career_roles
from modules.ui.pages_gaps import render_skills_gap
from modules.ui.pages_projects import render_project_recommendations
from modules.ui.pages_roadmap import render_learning_roadmap
from modules.ui.pages_jobs import render_job_opportunities
from modules.ui.pages_tracker import render_application_tracker
from modules.ui.pages_settings import render_settings

# Initialize database schemas
init_db()

# Inject Global Visual Identity CSS
st.markdown(get_theme_css(), unsafe_allow_html=True)

# Navigation Menu Definition
NAV_OPTIONS = [
    "Dashboard",
    "Resume Analyzer",
    "Job Description Matcher",
    "AI Interview Coach (RAG)",
    "AI Career Chatbot",
    "Resume Builder",
    "Career Role Explorer",
    "Skills Gap Analysis",
    "Project Recommendations",
    "Learning Roadmap",
    "Job Opportunities",
    "Application Tracker",
    "Settings"
]

# Initialize Session State
if "nav_selection" not in st.session_state:
    st.session_state["nav_selection"] = "Dashboard"

# Synchronize navigation if externally updated
current_nav = st.session_state["nav_selection"]
if current_nav not in NAV_OPTIONS:
    current_nav = "Dashboard"

# ----------------- SIDEBAR ----------------- #
with st.sidebar:
    # App Logo & Branding
    st.markdown("""
    <div style="padding: 0.5rem 0 1.25rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 38px; height: 38px; background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #FFFFFF; font-weight: 800; font-size: 1.15rem; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                CC
            </div>
            <div>
                <div style="font-weight: 800; font-size: 1.05rem; color: #FFFFFF; letter-spacing: -0.01em;">Career Copilot AI</div>
                <div style="font-size: 0.72rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600;">AI Career Platform</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation Selection
    selected = st.radio(
        label="Navigation Menu",
        options=NAV_OPTIONS,
        index=NAV_OPTIONS.index(current_nav),
        label_visibility="collapsed",
        key="main_sidebar_nav"
    )

    if selected != st.session_state["nav_selection"]:
        st.session_state["nav_selection"] = selected
        st.rerun()

    # User Profile at Bottom of Sidebar
    profile = get_user_profile()
    render_sidebar_profile(profile)


# ----------------- MAIN CONTENT ROUTER ----------------- #
page = st.session_state["nav_selection"]

if page == "Dashboard":
    render_dashboard()
elif page == "Resume Analyzer":
    render_resume_analyzer()
elif page == "Job Description Matcher":
    render_job_matcher()
elif page == "AI Interview Coach (RAG)":
    render_interview_coach()
elif page == "AI Career Chatbot":
    render_career_chatbot()
elif page == "Resume Builder":
    render_resume_builder()
elif page == "Career Role Explorer":
    render_career_roles()
elif page == "Skills Gap Analysis":
    render_skills_gap()
elif page == "Project Recommendations":
    render_project_recommendations()
elif page == "Learning Roadmap":
    render_learning_roadmap()
elif page == "Job Opportunities":
    render_job_opportunities()
elif page == "Application Tracker":
    render_application_tracker()
elif page == "Settings":
    render_settings()

