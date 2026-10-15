"""
Career Copilot AI - Project Recommendations Page Module
Tailors concrete, proof-of-work portfolio project blueprints to the user's
target role and skill gaps with milestones, testing standards, and deliverables.
Rendered entirely using native Streamlit containers and components.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_skill_badges
)
from modules.storage.database import get_user_profile
from modules.data.projects_data import get_projects_for_role
from modules.data.roles_data import get_role_titles, get_role_branches, get_roles_by_branch


def render_project_recommendations():
    """Render Project Recommendations page with native Streamlit cards."""
    render_page_header(
        title="Project Recommendations",
        subtitle="Production-grade engineering and clinical project blueprints tailored to your target discipline.",
        breadcrumb="Career Copilot AI / Project Recommendations",
        badge_text="Portfolio Blueprints"
    )

    profile = get_user_profile()
    branches = get_role_branches()
    col_b, col_r = st.columns([1, 1.5])

    with col_b:
        selected_branch = st.selectbox("Discipline / Field", branches, index=0, key="proj_branch_select")

    branch_roles = get_roles_by_branch(selected_branch)
    default_role = profile.get("target_role", "Civil Structural Engineer")
    default_idx = branch_roles.index(default_role) if default_role in branch_roles else 0

    with col_r:
        selected_role = st.selectbox(
            "Target Role Track",
            branch_roles,
            index=default_idx,
            key="proj_role_select"
        )

    projects = get_projects_for_role(selected_role)

    st.info(
        "**Portfolio Proof-of-Work Standards:** Hiring managers and engineering teams look for verifiable evidence—such as "
        "structural calculation sheets, validated CAD models, containerized microservices, or clinical audit reports—rather than "
        "generic tutorial exercises. Each blueprint below fulfills industry hiring benchmarks."
    )

    for p in projects:
        with st.container(border=True):
            st.caption(f"{p.get('role', selected_role).upper()} BENCHMARK")
            st.subheader(p['title'])

            st.markdown(f"**Objective:** {p['objective']}")
            st.info(f"**Why it matches this role:** {p['why_matches']}")

            st.markdown("**Competencies Demonstrated:**")
            render_skill_badges(p.get("skills_demonstrated", []), category="matched")

            col_m, col_t = st.columns([1.2, 1])

            with col_m:
                st.markdown("**Implementation Milestones:**")
                for m in p.get("milestones", []):
                    st.markdown(f"- {m}")

            with col_t:
                st.markdown("**Testing & Quality Verification:**")
                for t in p.get("testing_requirements", []):
                    st.markdown(f"- ✅ {t}")

                st.markdown("**Key Deliverables:**")
                for g in p.get("github_deliverables", []):
                    st.markdown(f"- 📁 {g}")
