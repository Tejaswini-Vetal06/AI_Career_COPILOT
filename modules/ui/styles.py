"""
Career Copilot AI - Design System and Theme Styles
Defines the visual identity, CSS variables, and layout aesthetics based on:
- Primary navy: #123B63
- Deep navy: #0B1F3A
- Sky blue: #38BDF8
- Pale sky blue: #E0F2FE
- White: #FFFFFF
- Page background: #F7FAFC
- Card background: #FFFFFF
- Primary text: #172B4D
- Secondary text: #64748B
- Borders: #E2E8F0
- Success: #16A34A | Warning: #D97706 | Error: #DC2626
"""

def get_theme_css() -> str:
    """Return injectible global CSS styling for the entire application."""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --primary-navy: #123B63;
        --deep-navy: #0B1F3A;
        --sky-blue: #38BDF8;
        --sky-pale: #E0F2FE;
        --white: #FFFFFF;
        --page-bg: #F7FAFC;
        --card-bg: #FFFFFF;
        --text-primary: #172B4D;
        --text-secondary: #64748B;
        --border-color: #E2E8F0;
        --success: #16A34A;
        --warning: #D97706;
        --error: #DC2626;
        --radius-sm: 6px;
        --radius-md: 10px;
        --radius-lg: 14px;
        --shadow-sm: 0 1px 2px 0 rgba(11, 31, 58, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(11, 31, 58, 0.08), 0 2px 4px -2px rgba(11, 31, 58, 0.04);
        --shadow-lg: 0 10px 15px -3px rgba(11, 31, 58, 0.07), 0 4px 6px -4px rgba(11, 31, 58, 0.03);
    }

    /* Overall Layout & Background */
    .stApp {
        background-color: var(--page-bg) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        color: var(--text-primary) !important;
    }

    /* Reduce default top padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
        max-width: 1400px !important;
    }

    /* Hide standard Streamlit header clutter */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    #MainMenu, footer {
        visibility: hidden !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: #0B1F3A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        width: 290px !important;
    }
    section[data-testid="stSidebar"] div.block-container {
        padding-top: 1.5rem !important;
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
    }
    section[data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }

    /* Sidebar Radio / Navigation styling */
    section[data-testid="stSidebar"] .stRadio label {
        font-size: 0.92rem !important;
        font-weight: 500 !important;
        color: #94A3B8 !important;
        padding: 0.5rem 0.75rem !important;
        border-radius: var(--radius-sm) !important;
        transition: all 0.15s ease !important;
        cursor: pointer !important;
        margin-bottom: 2px !important;
        display: flex !important;
        align-items: center !important;
    }
    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(56, 189, 248, 0.1) !important;
        color: #38BDF8 !important;
    }
    section[data-testid="stSidebar"] .stRadio [aria-checked="true"] label {
        background: rgba(56, 189, 248, 0.15) !important;
        color: #FFFFFF !important;
        border-left: 3px solid #38BDF8 !important;
        font-weight: 600 !important;
    }
    /* Hide the radio button circle itself for clean nav-bar look */
    section[data-testid="stSidebar"] .stRadio input[type="radio"] {
        display: none !important;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: var(--primary-navy) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    p, span, label, div {
        color: var(--text-primary);
        font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }

    /* SaaS Cards */
    .copilot-card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: 1.5rem;
        box-shadow: var(--shadow-sm);
        margin-bottom: 1.25rem;
        transition: box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .copilot-card:hover {
        border-color: #CBD5E1;
        box-shadow: var(--shadow-md);
    }

    .copilot-card-hero {
        background: linear-gradient(135deg, #0B1F3A 0%, #123B63 60%, #1E4F7C 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: var(--radius-lg);
        padding: 2.25rem;
        color: #FFFFFF !important;
        box-shadow: var(--shadow-md);
        margin-bottom: 1.75rem;
        position: relative;
        overflow: hidden;
    }
    .copilot-card-hero h1, .copilot-card-hero p {
        color: #FFFFFF !important;
    }

    /* Badges & Pills */
    .copilot-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        text-transform: uppercase;
    }
    .badge-sky {
        background-color: var(--sky-pale);
        color: #0369A1;
        border: 1px solid #BAE6FD;
    }
    .badge-navy {
        background-color: #E2E8F0;
        color: var(--primary-navy);
        border: 1px solid #CBD5E1;
    }
    .badge-success {
        background-color: #DCFCE7;
        color: var(--success);
        border: 1px solid #86EFAC;
    }
    .badge-warning {
        background-color: #FEF3C7;
        color: var(--warning);
        border: 1px solid #FDE68A;
    }
    .badge-error {
        background-color: #FEE2E2;
        color: var(--error);
        border: 1px solid #FCA5A5;
    }

    /* Metric Stat Widget */
    .metric-container {
        background-color: #FFFFFF;
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: 1.25rem 1.5rem;
        box-shadow: var(--shadow-sm);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
    }
    .metric-label {
        font-size: 0.82rem;
        font-weight: 600;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.35rem;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 800;
        color: var(--primary-navy);
        line-height: 1.15;
    }
    .metric-footer {
        font-size: 0.8rem;
        color: var(--text-secondary);
        margin-top: 0.45rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    /* Button Styling */
    div.stButton > button {
        background-color: var(--primary-navy) !important;
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        border-radius: var(--radius-sm) !important;
        border: 1px solid transparent !important;
        padding: 0.55rem 1.2rem !important;
        box-shadow: var(--shadow-sm) !important;
        transition: all 0.18s ease-in-out !important;
    }
    div.stButton > button:hover {
        background-color: var(--deep-navy) !important;
        border-color: var(--sky-blue) !important;
        color: #FFFFFF !important;
        box-shadow: var(--shadow-md) !important;
        transform: translateY(-1px);
    }
    div.stButton > button:active {
        transform: translateY(0);
    }

    /* Secondary / Outline button styling */
    div.stButton > button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: var(--primary-navy) !important;
        border: 1px solid var(--border-color) !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        background-color: var(--sky-pale) !important;
        border-color: var(--sky-blue) !important;
        color: var(--deep-navy) !important;
    }

    /* Form Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {
        border-color: var(--border-color) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        background-color: #FFFFFF !important;
        box-shadow: var(--shadow-sm) !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--sky-blue) !important;
        box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.25) !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1.5rem !important;
        border-bottom: 2px solid var(--border-color) !important;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 600 !important;
        color: var(--text-secondary) !important;
        padding: 0.75rem 0.25rem !important;
        background-color: transparent !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--primary-navy) !important;
        border-bottom: 3px solid var(--sky-blue) !important;
    }

    /* Empty State Container */
    .empty-state-box {
        text-align: center;
        padding: 3rem 1.5rem;
        background: #FFFFFF;
        border: 2px dashed #CBD5E1;
        border-radius: var(--radius-md);
        margin: 1rem 0;
    }
    .empty-state-box h4 {
        color: var(--primary-navy) !important;
        margin-top: 0.75rem;
        margin-bottom: 0.35rem;
    }
    .empty-state-box p {
        color: var(--text-secondary) !important;
        font-size: 0.9rem;
        max-width: 460px;
        margin: 0 auto 1.25rem auto;
    }

    /* A4 Resume Preview Paper */
    .resume-a4-preview {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border-radius: 4px;
        padding: 2.5rem 3rem;
        font-family: 'Inter', sans-serif;
        color: #172B4D;
        line-height: 1.5;
        min-height: 800px;
        position: relative;
    }
    .resume-header {
        border-bottom: 2px solid var(--primary-navy);
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
    }
    .resume-section-title {
        font-size: 0.95rem;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--primary-navy);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 0.3rem;
        margin-top: 1.2rem;
        margin-bottom: 0.6rem;
        letter-spacing: 0.05em;
    }

    /* Journey Roadmap Step Card */
    .journey-step {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 1rem;
        border: 1px solid var(--border-color);
        border-radius: var(--radius-sm);
        background: #FFFFFF;
        margin-bottom: 0.75rem;
        transition: all 0.15s ease;
    }
    .journey-step:hover {
        border-color: var(--sky-blue);
        transform: translateX(3px);
    }
    .journey-num {
        background: var(--sky-pale);
        color: #0369A1;
        font-weight: 700;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        font-size: 0.85rem;
    }

    /* Bullet Tip Card */
    .bullet-tip-card {
        border-left: 3px solid var(--warning);
        background: #FFFBEB;
        padding: 0.85rem 1rem;
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        margin-bottom: 0.75rem;
        font-size: 0.88rem;
    }
    .bullet-tip-card.success {
        border-left-color: var(--success);
        background: #F0FDF4;
    }

    /* Skill Tag */
    .skill-tag {
        display: inline-block;
        background: #F1F5F9;
        color: var(--text-primary);
        border: 1px solid #E2E8F0;
        border-radius: 6px;
        padding: 0.25rem 0.6rem;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.2rem 0.2rem;
    }
    .skill-tag.matched {
        background: #DCFCE7;
        color: #166534;
        border-color: #BBF7D0;
    }
    .skill-tag.missing {
        background: #FEE2E2;
        color: #991B1B;
        border-color: #FECACA;
    }
    .skill-tag.improved {
        background: #FEF3C7;
        color: #92400E;
        border-color: #FDE68A;
    }
    </style>
    """

