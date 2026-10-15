"""
Career Copilot AI - Personalized Learning Roadmap Page Module
Interactive weekly planner with persistent completion tracking in SQLite.
Computes real progress percentage from completed milestones across all engineering and healthcare disciplines.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_metric_card
)
from modules.storage.database import (
    get_user_profile, get_roadmap_progress, set_roadmap_task_status
)
from modules.data.roadmap_data import get_roadmap_for_role, get_total_roadmap_tasks
from modules.data.roles_data import get_role_titles, get_role_branches, get_roles_by_branch


def render_learning_roadmap():
    """Render the Learning Roadmap page with native Streamlit controls."""
    render_page_header(
        title="Personalized Learning Roadmap",
        subtitle="Actionable, milestone-driven weekly curriculum with persistent progress tracking across all career tracks.",
        breadcrumb="Career Copilot AI / Learning Roadmap",
        badge_text="Real Progress Tracker"
    )

    profile = get_user_profile()
    branches = get_role_branches()

    # Planner Controls Row
    c_b, c_r, c_exp, c_hrs = st.columns([1, 1.2, 1, 1])
    with c_b:
        selected_branch = st.selectbox("Discipline / Field", branches, index=0, key="roadmap_branch_select")

    branch_roles = get_roles_by_branch(selected_branch)
    default_role = profile.get("target_role", "Civil Structural Engineer")
    default_idx = branch_roles.index(default_role) if default_role in branch_roles else 0

    with c_r:
        target_role = st.selectbox(
            "Curriculum Track",
            branch_roles,
            index=default_idx,
            key="roadmap_role_select"
        )
    with c_exp:
        experience_lvl = st.selectbox(
            "Experience Tier",
            ["Beginner / Student", "Intermediate (1-3 yrs)", "Advanced / Transitioning"],
            index=0,
            key="roadmap_exp_select"
        )
    with c_hrs:
        study_hours = st.selectbox(
            "Weekly Commitment",
            ["6-8 hrs/week", "10-12 hrs/week", "15-20 hrs/week"],
            index=1,
            key="roadmap_hours_select"
        )

    # Fetch curriculum & persistent progress from SQLite
    curriculum = get_roadmap_for_role(target_role)
    progress_map = get_roadmap_progress(target_role)
    completed_count = sum(1 for status in progress_map.values() if status)
    total_tasks = sum(len(w.get("tasks", [])) for w in curriculum)
    progress_pct = int((completed_count / max(total_tasks, 1)) * 100)

    # Progress KPI Row
    k1, k2, k3 = st.columns(3)
    with k1:
        render_metric_card("Track Progress", f"{progress_pct}%", f"{completed_count}/{total_tasks} Milestones Done", "sky" if progress_pct > 0 else "navy")
    with k2:
        render_metric_card("Duration", f"{len(curriculum)} Weeks", study_hours, "sky")
    with k3:
        render_metric_card("Target Role", target_role[:18], experience_lvl[:16], "success")

    st.progress(progress_pct / 100.0)

    st.divider()

    # Render Weekly Milestones
    for week_data in curriculum:
        week_num = week_data["week"]
        week_title = week_data["title"]
        week_hours = week_data.get("hours", "10-12 hrs")
        week_focus = week_data.get("focus", "")

        week_tasks = week_data.get("tasks", [])
        week_done = sum(1 for t in week_tasks if progress_map.get(t["id"], False))
        week_pct = int((week_done / max(len(week_tasks), 1)) * 100)

        with st.expander(f"Week {week_num}: {week_title} ({week_done}/{len(week_tasks)} Done — {week_pct}%)", expanded=(week_num == 1 or week_pct < 100)):
            with st.container(border=True):
                col_f1, col_f2 = st.columns([0.8, 0.2])
                with col_f1:
                    st.markdown(f"**Core Focus:** {week_focus}")
                with col_f2:
                    st.caption(f"⏱️ {week_hours}")

            st.markdown("**Actionable Tasks & Practice Exercises:**")

            for task in week_tasks:
                t_id = task["id"]
                current_val = progress_map.get(t_id, False)

                is_checked = st.checkbox(
                    task["desc"],
                    value=current_val,
                    key=f"chk_task_{target_role}_{t_id}"
                )

                if is_checked != current_val:
                    set_roadmap_task_status(
                        role_id=target_role,
                        week_id=week_num,
                        task_id=t_id,
                        is_completed=is_checked
                    )
                    st.rerun()
