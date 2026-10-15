"""
Career Copilot AI - Career Role Explorer Page Module
Explores industry roles across all engineering branches and healthcare/medical fields.
Provides deep-dives into core responsibilities, essential skills, learning progression,
portfolio standards, interview themes, and side-by-side role comparisons.
Rendered entirely with native Streamlit components.
"""

import streamlit as st
import urllib.parse
from modules.ui.components import (
    render_page_header, render_skill_badges
)
from modules.data.roles_data import (
    ROLES_DATA, get_all_roles, get_role_titles, get_role_branches, get_roles_by_branch
)


def render_career_roles():
    """Render the Career Role Explorer page."""
    render_page_header(
        title="Career Role Explorer",
        subtitle="Explore high-demand career tracks across Civil, Mechanical, Electrical, Electronics, CS/AI, and Healthcare.",
        breadcrumb="Career Copilot AI / Career Role Explorer",
        badge_text="Multi-Discipline Catalog"
    )

    tab_explore, tab_compare = st.tabs(["Explore Roles", "Side-by-Side Comparison Tool"])

    with tab_explore:
        render_explore_tab()

    with tab_compare:
        render_comparison_tab()


def render_explore_tab():
    """Render single role deep-dive view with branch filtering."""
    branches = get_role_branches()
    col_branch, col_role = st.columns([1, 1.5])

    with col_branch:
        selected_branch = st.selectbox("Filter by Field / Discipline", branches, index=0, key="sel_roles_branch")

    roles_in_branch = get_roles_by_branch(selected_branch)
    with col_role:
        selected_role_title = st.selectbox(
            "Select Role to Inspect",
            roles_in_branch,
            index=0 if roles_in_branch else 0,
            key="role_selector"
        )

    if not selected_role_title or selected_role_title not in ROLES_DATA:
        st.info("No roles found for selected discipline.")
        return

    role = ROLES_DATA[selected_role_title]

    # Role Overview Card
    with st.container(border=True):
        col_t1, col_t2 = st.columns([0.75, 0.25])
        with col_t1:
            st.caption(f"FIELD: {role.get('branch', 'Engineering & Technology').upper()}")
            st.title(role['title'])
        with col_t2:
            st.success("**High Demand**")

        st.write(role['overview'])
        st.info(f"**Education Expectations:** {role['education_expectations']}")

    c1, c2 = st.columns(2)

    with c1:
        # Essential vs Optional Skills Card
        with st.container(border=True):
            st.subheader("Technical Competencies")

            st.markdown("**Essential Core Skills:**")
            render_skill_badges(role["essential_skills"], category="matched")

            st.markdown("**Optional / Advanced Specializations:**")
            render_skill_badges(role["optional_skills"], category="default")

        # Portfolio Project Standards
        with st.container(border=True):
            st.subheader("Strong Portfolio Projects")
            st.caption("Proof-of-work projects that demonstrate practical competency to hiring managers.")

            for proj in role.get("portfolio_projects", []):
                with st.container(border=True):
                    st.markdown(f"**{proj['title']}**")
                    st.write(proj['desc'])
                    tech_str = ", ".join(proj.get("tech", []))
                    st.caption(f"🔧 Tools / Standards: {tech_str}")

    with c2:
        # Beginner to Advanced Learning Roadmap
        with st.container(border=True):
            st.subheader("Learning Progression (Beginner to Advanced)")

            for item in role.get("learning_topics", []):
                lvl = item["level"]
                icon = "🟢" if lvl == "Beginner" else ("🔵" if lvl == "Intermediate" else "🟣")
                st.markdown(f"- {icon} **{lvl}:** {item['topic']}")

        # Interview Preparation Topics & Curated Job Search Links
        with st.container(border=True):
            st.subheader("Interview Topics & Job Search")
            st.markdown("**Key Interview Themes:**")

            for topic in role.get("interview_topics", []):
                st.markdown(f"- 🎯 {topic}")

            st.divider()

            # Job portal query URLs
            q = urllib.parse.quote_plus(role.get("job_query", role["title"]))
            linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={q}"
            naukri_url = f"https://www.naukri.com/{q}-jobs"
            indeed_url = f"https://www.indeed.com/jobs?q={q}"
            google_url = f"https://www.google.com/search?ibp=htl;jobs&q={q}+jobs"

            st.markdown("**Search Current Openings:**")
            col_l1, col_l2 = st.columns(2)
            with col_l1:
                st.markdown(f"👉 [Search on LinkedIn]({linkedin_url})")
                st.markdown(f"👉 [Search on Naukri]({naukri_url})")
            with col_l2:
                st.markdown(f"👉 [Search on Indeed]({indeed_url})")
                st.markdown(f"👉 [Search on Google Jobs]({google_url})")


def render_comparison_tab():
    """Render side-by-side multi-role comparison matrix."""
    st.subheader("Side-by-Side Role Comparison")
    st.caption("Select 2 or 3 roles across any engineering branch or healthcare field to compare focus areas, essential skills, and portfolio expectations.")

    role_titles = get_role_titles()
    default_selection = ["Civil Structural Engineer", "Mechanical Design & CAD/FEA Engineer", "Machine Learning Engineer"]
    valid_defaults = [r for r in default_selection if r in role_titles]

    selected_roles = st.multiselect(
        "Choose roles to compare (2-3 recommended)",
        role_titles,
        default=valid_defaults if valid_defaults else role_titles[:2]
    )

    if not selected_roles:
        st.info("Select at least one role to view details.")
        return

    cols = st.columns(len(selected_roles))

    for idx, r_title in enumerate(selected_roles):
        r_data = ROLES_DATA.get(r_title, {})
        with cols[idx]:
            with st.container(border=True):
                st.caption(f"FIELD: {r_data.get('branch', 'Engineering').upper()}")
                st.markdown(f"### {r_title}")
                st.write(r_data.get("short_desc", ""))

                st.markdown("**Essential Skills:**")
                render_skill_badges(r_data.get("essential_skills", [])[:6], category="matched")

                st.markdown("**Portfolio Standard:**")
                if r_data.get("portfolio_projects"):
                    st.write(r_data["portfolio_projects"][0].get("title", ""))
                    st.caption(r_data["portfolio_projects"][0].get("desc", ""))

                st.markdown("**Typical Degree:**")
                st.caption(r_data.get("education_expectations", "")[:120] + "...")
