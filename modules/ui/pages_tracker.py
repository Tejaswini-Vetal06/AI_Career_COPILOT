"""
Career Copilot AI - Application Tracker Page Module
Manages job application lifecycle with statuses:
- Interested, To Apply, Applied, Interview, Offer, Rejected
Persisted in SQLite database with dates, salary, notes, and follow-up reminders.
"""

import streamlit as st
from datetime import date
from modules.ui.components import (
    render_page_header, render_metric_card, render_empty_state, ICONS
)
from modules.storage.database import (
    get_all_applications, add_application, update_application,
    delete_application, get_application_counts
)

STATUS_OPTIONS = ["Interested", "To Apply", "Applied", "Interview", "Offer", "Rejected"]


def render_application_tracker():
    """Render the Application Tracker page."""
    render_page_header(
        title="Application Tracker",
        subtitle="Organize your active job applications, interview stages, follow-up deadlines, and offers.",
        breadcrumb="Career Copilot AI / Application Tracker",
        badge_text="Pipeline Management"
    )

    counts = get_application_counts()

    # KPI Metrics Header
    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        render_metric_card("Total Pipeline", str(counts["Total"]), "Active Leads", "sky")
    with k2:
        render_metric_card("To Apply", str(counts["To Apply"]), "Preparing", "navy")
    with k3:
        render_metric_card("Applied", str(counts["Applied"]), "Submitted", "sky")
    with k4:
        render_metric_card("Interviews", str(counts["Interview"]), "In Progress", "warning")
    with k5:
        render_metric_card("Offers", str(counts["Offer"]), "Decisions", "success")

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)

    tab_pipeline, tab_add = st.tabs(["Active Applications", "Add New Application"])

    with tab_add:
        render_add_application_form()

    with tab_pipeline:
        render_applications_list()


def render_add_application_form():
    """Form to manually record a new application."""
    st.markdown("""
    <div class="copilot-card">
        <h3 style="font-size: 1.05rem; color: #123B63; margin: 0 0 0.75rem 0;">Record Application Lead</h3>
    """, unsafe_allow_html=True)

    with st.form("form_add_app", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            company = st.text_input("Company Name *", placeholder="e.g. Google, Anthropic")
            role = st.text_input("Role Title *", placeholder="e.g. Machine Learning Engineer")
            location = st.text_input("Location", value="Remote", placeholder="e.g. Remote, San Francisco, CA")
        with c2:
            status = st.selectbox("Current Status", STATUS_OPTIONS, index=0)
            salary = st.text_input("Compensation / Salary Range", placeholder="e.g. $140k - $180k")
            job_url = st.text_input("Job Posting URL", placeholder="https://company.com/careers/job-123")

        c3, c4 = st.columns(2)
        with c3:
            applied_date = st.date_input("Applied Date", value=None)
        with c4:
            follow_up_date = st.date_input("Follow-up Reminder Date", value=None)

        notes = st.text_area("Interview Notes & Key Contacts", placeholder="Notes about interview rounds, referral contacts, or take-home tests...")

        submitted = st.form_submit_button("Save Application to Tracker", type="primary")
        if submitted:
            if not company.strip() or not role.strip():
                st.error("Company Name and Role Title are required.")
            else:
                add_application(
                    company=company.strip(),
                    role=role.strip(),
                    location=location.strip(),
                    status=status,
                    applied_date=str(applied_date) if applied_date else None,
                    follow_up_date=str(follow_up_date) if follow_up_date else None,
                    salary_range=salary.strip(),
                    job_url=job_url.strip(),
                    notes=notes.strip()
                )
                st.success(f"Added {role} at {company} to tracker!")
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def render_applications_list():
    """List and manage all tracked applications."""
    filter_col, _ = st.columns([2, 4])
    with filter_col:
        status_filter = st.selectbox("Filter Status", ["All"] + STATUS_OPTIONS, index=0)

    apps = get_all_applications(status_filter=status_filter)

    if not apps:
        render_empty_state(
            title="No Applications Found",
            message="You haven't added any job applications under this status yet. Click 'Add New Application' or add one directly from the Job Opportunities page."
        )
        return

    for app in apps:
        app_id = app["id"]
        status = app["status"]
        badge_type = (
            "success" if status == "Offer" else
            "warning" if status == "Interview" else
            "sky" if status in ["Applied", "To Apply"] else
            "error" if status == "Rejected" else "navy"
        )

        with st.expander(f"{app['role']} @ {app['company']} — [{status}]", expanded=False):
            st.markdown(f"""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; font-size: 0.85rem; margin-bottom: 0.75rem;">
                <div><span style="color: #64748B;">Company:</span> <b>{app['company']}</b></div>
                <div><span style="color: #64748B;">Role:</span> <b>{app['role']}</b></div>
                <div><span style="color: #64748B;">Location:</span> {app['location']}</div>
                <div><span style="color: #64748B;">Salary:</span> {app['salary_range'] or 'Not specified'}</div>
                <div><span style="color: #64748B;">Applied Date:</span> {app['applied_date'] or 'N/A'}</div>
                <div><span style="color: #64748B;">Follow-up Date:</span> {app['follow_up_date'] or 'N/A'}</div>
            </div>
            """, unsafe_allow_html=True)

            if app.get("job_url"):
                st.markdown(f"<div style='font-size: 0.82rem; margin-bottom: 0.5rem;'><a href='{app['job_url']}' target='_blank' style='color: #0284C7; text-decoration: none;'>View Original Job Posting {ICONS['external']}</a></div>", unsafe_allow_html=True)

            if app.get("notes"):
                st.markdown(f"<div style='background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 0.6rem; font-size: 0.82rem; color: #475569; margin-bottom: 0.75rem;'><b>Notes:</b> {app['notes']}</div>", unsafe_allow_html=True)

            # Quick update form
            c_status, c_del = st.columns([3, 1])
            with c_status:
                new_status = st.selectbox(
                    "Update Status",
                    STATUS_OPTIONS,
                    index=STATUS_OPTIONS.index(status),
                    key=f"status_select_{app_id}"
                )
                if new_status != status:
                    update_application(
                        app_id=app_id,
                        company=app["company"],
                        role=app["role"],
                        location=app["location"],
                        status=new_status,
                        applied_date=app["applied_date"],
                        follow_up_date=app["follow_up_date"],
                        salary_range=app["salary_range"],
                        job_url=app["job_url"],
                        notes=app["notes"]
                    )
                    st.success(f"Status updated to '{new_status}'")
                    st.rerun()

            with c_del:
                st.markdown("<div style='margin-top: 1.7rem;'></div>", unsafe_allow_html=True)
                if st.button("Delete", key=f"btn_del_app_{app_id}"):
                    delete_application(app_id)
                    st.success("Application deleted.")
                    st.rerun()

