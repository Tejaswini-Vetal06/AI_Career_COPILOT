"""
Career Copilot AI - Multi-Platform Job Opportunities Page Module
Aggregates verified live hiring listings from:
- LinkedIn Jobs
- Naukri.com
- Indeed
- Google Careers
- Direct Corporate Portals across Civil, Mechanical, Electrical, ECE, Medical, and Tech.
Rendered entirely with native Streamlit containers and components.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_skill_badges, render_empty_state
)
from modules.jobs.job_service import (
    fetch_live_remote_jobs, filter_jobs, generate_platform_search_urls
)
from modules.storage.database import add_application, get_user_profile
from modules.data.roles_data import get_role_titles


def render_job_opportunities():
    """Render the Job Opportunities and Multi-Platform Search Board."""
    render_page_header(
        title="Job Opportunities & Hiring Board",
        subtitle="Explore current hiring listings across LinkedIn, Naukri, Indeed, and Google Jobs for all engineering and healthcare fields.",
        breadcrumb="Career Copilot AI / Job Opportunities",
        badge_text="Multi-Portal Feed"
    )

    profile = get_user_profile()
    default_role = profile.get("target_role", "Civil Structural Engineer")

    # Dynamic 1-Click Search Generator Header
    with st.container(border=True):
        st.subheader("1-Click Live Search across Top Hiring Portals")
        st.caption("Generate direct pre-filled queries for live hiring on major recruitment platforms.")

        col_q, col_loc = st.columns([1.5, 1])
        with col_q:
            search_query = st.text_input("Target Role or Tool Keyword:", value=default_role, key="txt_jobs_search_query")
        with col_loc:
            search_location = st.text_input("Location (Optional):", value="India", placeholder="e.g. Bengaluru, Mumbai, Remote", key="txt_jobs_location")

        search_urls = generate_platform_search_urls(search_query, search_location)

        col_p1, col_p2, col_p3, col_p4 = st.columns(4)
        with col_p1:
            st.markdown(f"💼 **[Search on LinkedIn]({search_urls['linkedin']})**")
        with col_p2:
            st.markdown(f"🟢 **[Search on Naukri.com]({search_urls['naukri']})**")
        with col_p3:
            st.markdown(f"🔵 **[Search on Indeed]({search_urls['indeed']})**")
        with col_p4:
            st.markdown(f"🌐 **[Search on Google Jobs]({search_urls['google']})**")

    st.divider()

    # Fetch verified listings
    all_jobs = fetch_live_remote_jobs()

    # Filter Bar
    with st.container(border=True):
        st.subheader("Filter Verified Openings")
        f1, f2, f3, f4, f5 = st.columns([1.5, 1, 1, 1, 1.5])
        with f1:
            roles_opts = ["All"] + get_role_titles()
            selected_role = st.selectbox("Role Track", roles_opts, index=0)
        with f2:
            selected_platform = st.selectbox("Platform Source", ["All", "LinkedIn", "Naukri", "Indeed", "Google"], index=0)
        with f3:
            selected_workplace = st.selectbox("Workplace Type", ["All", "Hybrid", "Remote", "On-site"], index=0)
        with f4:
            selected_exp = st.selectbox("Experience Level", ["All", "Entry Level", "Mid Level", "Senior Level"], index=0)
        with f5:
            keyword = st.text_input("Keyword or Tool", placeholder="e.g. AutoCAD, SolidWorks, Python, ETAP")

    # Filter
    filtered_jobs = filter_jobs(
        jobs=all_jobs,
        role_filter=selected_role,
        platform_filter=selected_platform,
        workplace_filter=selected_workplace,
        experience_filter=selected_exp,
        keyword_search=keyword
    )

    st.caption(f"Showing **{len(filtered_jobs)}** verified openings across hiring portals")

    if not filtered_jobs:
        render_empty_state(
            title="No Matching Openings Found",
            message="Try widening your platform or role filters to view more current openings."
        )
        return

    # Render Cards
    for job in filtered_jobs:
        job_id = job.get("id", "")
        title = job.get("title", "")
        company = job.get("company", "")
        location = job.get("location", "")
        workplace = job.get("workplace_type", "Remote")
        platform = job.get("platform", "Platform")
        salary = job.get("salary_range", "Competitive")
        date_str = job.get("posted_date", "Recent")
        source = job.get("source", "Verified Feed")
        url = job.get("url", "#")
        desc = job.get("description", "")
        skills = job.get("skills_required", [])

        with st.container(border=True):
            col_j1, col_j2 = st.columns([0.72, 0.28])
            with col_j1:
                st.caption(f"{platform} • {workplace}")
                st.markdown(f"### {title}")
                st.write(f"**{company}** — {location}")
            with col_j2:
                st.markdown(f"**{salary}**")
                st.caption(f"Source: {source} ({date_str})")

            st.write(desc)

            st.markdown("**Key Skills Required:**")
            render_skill_badges(skills, category="matched")

            col_b1, col_b2 = st.columns([0.65, 0.35])
            with col_b1:
                st.markdown(f"👉 **[Apply directly on {platform}]({url})**")
            with col_b2:
                if st.button("Add to Application Tracker", key=f"btn_track_{job_id}"):
                    add_application(
                        company=company,
                        role=title,
                        location=location,
                        status="Interested",
                        salary_range=salary,
                        job_url=url,
                        notes=f"Found via {platform}. Key skills: {', '.join(skills[:4])}"
                    )
                    st.success(f"Added '{title} at {company}' to your Application Tracker!")
