"""
Career Copilot AI - RAG Interview Coach Page Module
Provides interactive mock interview practice grounded in the user's
specific resume and target job description using Retrieval-Augmented Generation.
"""

import streamlit as st
from modules.ui.components import (
    render_page_header, render_metric_card, render_empty_state, ICONS
)
from modules.storage.database import (
    get_active_resume, get_latest_job_analysis, get_user_profile
)
from modules.rag.interview_coach import RAGInterviewCoach


def render_interview_coach():
    """Render the AI Interview Coach (RAG) page."""
    render_page_header(
        title="AI Interview Coach (RAG)",
        subtitle="Practice tailored interview questions generated via RAG from your actual resume and target job requirements.",
        breadcrumb="Career Copilot AI / Interview Coach",
        badge_text="RAG Intelligence"
    )

    active_resume = get_active_resume()
    latest_job = get_latest_job_analysis()
    profile = get_user_profile()

    if not active_resume or not latest_job:
        render_empty_state(
            title="Interview Coach Requires Context",
            message="To generate deeply personalized interview questions, please ensure both a resume is uploaded and a job description is matched.",
            action_label="Go to Resume Analyzer"
        )
        if st.session_state.get("btn_empty_interview_coach_requires_context"):
            st.session_state["nav_selection"] = "Resume Analyzer"
            st.rerun()
        return

    target_role = profile.get("target_role", "Machine Learning Engineer")
    resume_text = active_resume.get("raw_text", "")
    jd_text = latest_job.get("job_description", "")
    matched_analysis = latest_job.get("analysis", {})

    # RAG Engine Instance
    coach = RAGInterviewCoach(
        resume_text=resume_text,
        jd_text=jd_text,
        target_role=target_role,
        resume_data=active_resume.get("extracted_data", {}),
        matched_analysis=matched_analysis
    )

    # Context Header Card
    st.markdown(f"""
    <div class="copilot-card" style="border-left: 4px solid #38BDF8; margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
            <div>
                <span class="copilot-badge badge-sky" style="font-size: 0.7rem;">Active RAG Grounding</span>
                <div style="font-size: 1.1rem; font-weight: 700; color: #123B63; margin-top: 0.25rem;">
                    Targeting: {latest_job.get('job_title', target_role)} @ {latest_job.get('company_name', 'Hiring Company') or 'Tech Industry'}
                </div>
                <div style="font-size: 0.8rem; color: #64748B;">
                    Grounded on: <b>{active_resume.get('file_name')}</b> | Chunks Indexed: <b>{len(coach.chunks)}</b>
                </div>
            </div>
            <div>
                <span class="copilot-badge badge-navy">STAR Methodology</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Initialize questions in session state
    if "interview_questions" not in st.session_state:
        st.session_state["interview_questions"] = coach.generate_interview_questions()

    questions = st.session_state["interview_questions"]

    # Re-generate button
    col_btn, _ = st.columns([1.5, 4])
    with col_btn:
        if st.button("Regenerate Questions", key="btn_regen_q"):
            st.session_state["interview_questions"] = coach.generate_interview_questions()
            st.session_state.pop("latest_evaluation", None)
            st.rerun()

    # Question Selection Radio/Selector
    q_titles = [f"Q{i+1}: [{q['type']}] {q['question'][:75]}..." for i, q in enumerate(questions)]
    selected_idx = st.selectbox("Select Question to Practice", range(len(questions)), format_func=lambda i: q_titles[i])

    active_q = questions[selected_idx]

    # Two column arena: Question on Left, Evaluation & Model Answer on Right
    c_q, c_eval = st.columns([1.2, 1.1])

    with c_q:
        st.markdown(f"""
        <div class="copilot-card">
            <span class="copilot-badge badge-sky" style="margin-bottom: 0.5rem;">{active_q['type']}</span>
            <h3 style="font-size: 1.15rem; font-weight: 700; color: #123B63; line-height: 1.45; margin: 0.2rem 0 0.75rem 0;">
                {active_q['question']}
            </h3>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 0.65rem; font-size: 0.8rem; color: #475569; margin-bottom: 0.75rem;">
                <b>RAG Retrieved Context:</b><br>
                <i>"{active_q.get('context_retrieved', '')[:180]}..."</i>
            </div>

            <div style="font-size: 0.82rem; color: #0284C7; margin-bottom: 1rem;">
                <b>Interviewer Focus:</b> {active_q['evaluation_focus']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        user_answer = st.text_area(
            "Your Answer (Type your response below):",
            height=200,
            placeholder="Structure your answer using Situation, Task, Action, and quantifiable Result (STAR)...",
            key=f"user_ans_{active_q['id']}"
        )

        if st.button("Submit Answer for AI Evaluation", type="primary", key=f"btn_eval_{active_q['id']}"):
            if not user_answer.strip():
                st.error("Please enter an answer to evaluate.")
            else:
                with st.spinner("Analyzing STAR structure, engineering rigor, and metric clarity..."):
                    eval_result = coach.evaluate_candidate_answer(active_q, user_answer)
                    st.session_state["latest_evaluation"] = eval_result
                    st.rerun()

    with c_eval:
        eval_data = st.session_state.get("latest_evaluation")
        if not eval_data:
            st.markdown("""
            <div class="empty-state-box" style="padding: 2.5rem 1rem;">
                <div style="width: 44px; height: 44px; background: #E0F2FE; color: #0284C7; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 0.5rem;">
                    🎯
                </div>
                <h4>Awaiting Your Answer</h4>
                <p>Type your interview response on the left and click 'Submit Answer for AI Evaluation' to receive STAR diagnostics and ideal model answers.</p>
            </div>
            """, unsafe_allow_html=True)
            return

        score = eval_data.get("score", 0)
        verdict = eval_data.get("verdict", "Good")
        score_badge = "success" if score >= 75 else ("warning" if score >= 55 else "error")

        # Score & Feedback Card
        st.markdown(f"""
        <div class="copilot-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                <div>
                    <span style="font-size: 0.8rem; font-weight: 700; color: #64748B; text-transform: uppercase;">Interview Readiness</span>
                    <h2 style="font-size: 2.2rem; font-weight: 800; color: #123B63; margin: 0.15rem 0;">{score}/100</h2>
                </div>
                <span class="copilot-badge badge-{score_badge}">{verdict}</span>
            </div>

            <div style="font-size: 0.82rem; font-weight: 700; color: #123B63; margin-bottom: 0.35rem;">STAR Framework Breakdown:</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 0.65rem; font-size: 0.78rem; margin-bottom: 0.85rem;">
                <div><b>Situation:</b> {eval_data['star_feedback'].get('situation')}</div>
                <div><b>Task:</b> {eval_data['star_feedback'].get('task')}</div>
                <div><b>Action:</b> {eval_data['star_feedback'].get('action')}</div>
                <div><b>Result:</b> {eval_data['star_feedback'].get('result')}</div>
            </div>
        """, unsafe_allow_html=True)

        # Strengths
        if eval_data.get("strengths"):
            st.markdown("<div style='font-size: 0.82rem; font-weight: 700; color: #16A34A; margin-bottom: 0.25rem;'>Strengths Identified:</div>", unsafe_allow_html=True)
            for s in eval_data["strengths"]:
                st.markdown(f"<div style='font-size: 0.8rem; color: #172B4D; margin-bottom: 0.25rem; display: flex; gap: 0.4rem;'>{ICONS['check']} <span>{s}</span></div>", unsafe_allow_html=True)

        # Improvements
        if eval_data.get("improvements"):
            st.markdown("<div style='font-size: 0.82rem; font-weight: 700; color: #D97706; margin-top: 0.6rem; margin-bottom: 0.25rem;'>What to Refine:</div>", unsafe_allow_html=True)
            for imp in eval_data["improvements"]:
                st.markdown(f"<div style='font-size: 0.8rem; color: #172B4D; margin-bottom: 0.25rem; display: flex; gap: 0.4rem;'>{ICONS['alert']} <span>{imp}</span></div>", unsafe_allow_html=True)

        # Model Answer / Guide
        with st.expander("Senior Engineer Model Answer & Strategy", expanded=True):
            st.markdown(f"""
            <div style="font-size: 0.83rem; color: #334155; line-height: 1.5; background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 6px; padding: 0.75rem;">
                <b>Recommended Framing:</b><br>
                {eval_data.get('model_answer', '')}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
