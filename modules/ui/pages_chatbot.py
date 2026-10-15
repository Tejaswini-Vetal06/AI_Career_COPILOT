"""
Career Copilot AI - AI Career Chatbot UI Page
Multi-turn conversational assistant helping users with:
- Resume analysis & bullet point feedback
- Personalized study roadmaps & priority concepts
- Interview preparation (STAR method, mock questions)
- Multi-platform job search tactics (Naukri, LinkedIn, Indeed)
"""

import streamlit as st
from modules.ui.components import render_page_header, ICONS
from modules.storage.database import get_active_resume, get_latest_job_analysis, get_user_profile
from modules.agent.career_chatbot import get_chatbot_response


def render_career_chatbot():
    """Render the AI Career Chatbot page."""
    render_page_header(
        title="AI Career Chatbot",
        subtitle="Your 24/7 intelligent coach for resume queries, study roadmaps, technical interview prep, and job search tactics.",
        breadcrumb="Career Copilot AI / AI Career Chatbot",
        badge_text="Copilot Assistant"
    )

    profile = get_user_profile()
    active_resume = get_active_resume()
    latest_job = get_latest_job_analysis()
    target_role = profile.get("target_role", "Machine Learning Engineer")

    # Context Awareness Banner
    resume_status = f"Active Resume: <b>{active_resume.get('file_name')}</b> ({active_resume.get('readiness_score')}% readiness)" if active_resume else "No resume uploaded yet"
    target_status = f"Target Role: <b>{target_role}</b>"

    st.markdown(f"""
    <div style="background: #F0F9FF; border: 1px solid #BAE6FD; border-radius: 8px; padding: 0.75rem 1rem; margin-bottom: 1.25rem; font-size: 0.82rem; color: #0369A1; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
        <div>🤖 <b>Chatbot Context:</b> {target_status} &nbsp;|&nbsp; {resume_status}</div>
        <span class="copilot-badge badge-sky">Ready to Assist</span>
    </div>
    """, unsafe_allow_html=True)

    # Initialize chat history in session state
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "content": (
                    f"Hello! I am your **Career Copilot AI Assistant**. "
                    f"I can help you review your resume, break down complex interview questions, plan your {target_role} study roadmap, "
                    f"or optimize your job search on LinkedIn and Naukri. What would you like help with today?"
                )
            }
        ]

    # Quick Suggestion Chips
    st.markdown("<div style='font-size: 0.82rem; font-weight: 700; color: #123B63; margin-bottom: 0.4rem;'>Quick Question Starters:</div>", unsafe_allow_html=True)
    chip_cols = st.columns(4)

    chips = [
        "How do I answer 'Tell me about yourself'?",
        "Explain the STAR method with an example",
        "How to get recruiter attention on LinkedIn and Naukri?",
        "How can I improve my resume's ATS score?"
    ]

    selected_chip = None
    for idx, chip_text in enumerate(chips):
        with chip_cols[idx]:
            if st.button(chip_text, key=f"chip_btn_{idx}", use_container_width=True):
                selected_chip = chip_text

    # Render previous conversation history
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input handler (from chat input or quick chip)
    prompt = st.chat_input("Ask any question about your resume, roadmap, interview, or job search...")
    query_to_send = selected_chip or prompt

    if query_to_send:
        # Append and display user message
        st.session_state["chat_messages"].append({"role": "user", "content": query_to_send})
        with st.chat_message("user"):
            st.markdown(query_to_send)

        # Generate bot response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing your profile and generating recommendations..."):
                response = get_chatbot_response(
                    user_query=query_to_send,
                    chat_history=st.session_state["chat_messages"],
                    active_resume=active_resume,
                    latest_job=latest_job,
                    target_role=target_role,
                    gemini_api_key=st.session_state.get("gemini_api_key")
                )
                st.markdown(response)

        st.session_state["chat_messages"].append({"role": "assistant", "content": response})

