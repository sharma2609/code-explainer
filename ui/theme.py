"""
NothingOS-inspired theme for Streamlit
Simple, working approach with clean monochrome design
"""

import streamlit as st

def apply_theme():
    """Apply the NothingOS monochrome theme to Streamlit"""
    
    st.markdown("""
    <style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Global styling */
    .stApp {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container - keep it visible */
    .main .block-container {
        background-color: #000000 !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Custom header */
    .custom-header {
        text-align: center;
        padding: 1.5rem 0 2rem 0;
        border-bottom: 1px solid #1E1E1E;
        margin-bottom: 2rem;
    }
    
    .custom-header h1 {
        color: #FFFFFF !important;
        font-size: 1.5rem !important;
        font-weight: 500 !important;
        margin: 0 0 0.5rem 0 !important;
    }
    
    .custom-header p {
        color: #7A7A7A !important;
        font-size: 0.875rem !important;
        margin: 0 !important;
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        background-color: #0B0B0B !important;
        color: #FFFFFF !important;
        border: 1px solid #1E1E1E !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #FFFFFF !important;
        box-shadow: 0 0 0 1px #FFFFFF !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: #7A7A7A !important;
    }
    
    /* Select Box */
    .stSelectbox > div > div > select {
        background-color: #0B0B0B !important;
        color: #FFFFFF !important;
        border: 1px solid #1E1E1E !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stSelectbox > div > div > select:focus {
        border-color: #FFFFFF !important;
        box-shadow: 0 0 0 1px #FFFFFF !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: transparent !important;
        color: #FFFFFF !important;
        border: 1px solid #1E1E1E !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        transition: border-color 0.2s ease !important;
    }
    
    .stButton > button:hover {
        border-color: #FFFFFF !important;
        background-color: #0B0B0B !important;
    }
    
    .stButton > button[kind="primary"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #FFFFFF !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        background-color: #E0E0E0 !important;
        border-color: #E0E0E0 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        border-bottom: 1px solid #1E1E1E !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: #7A7A7A !important;
        border: none !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
    }
    
    .stTabs [aria-selected="true"] {
        color: #FFFFFF !important;
        border-bottom: 2px solid #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #0B0B0B !important;
        color: #FFFFFF !important;
        border: 1px solid #1E1E1E !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.875rem !important;
    }
    
    .streamlit-expanderContent {
        background-color: #000000 !important;
        border: 1px solid #1E1E1E !important;
        border-top: none !important;
        color: #B3B3B3 !important;
    }
    
    /* Messages */
    .stSuccess {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        border-left: 3px solid #FFFFFF !important;
        color: #FFFFFF !important;
    }
    
    .stWarning {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        border-left: 3px solid #7A7A7A !important;
        color: #B3B3B3 !important;
    }
    
    .stError {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        border-left: 3px solid #FFFFFF !important;
        color: #FFFFFF !important;
    }
    
    .stInfo {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        border-left: 3px solid #7A7A7A !important;
        color: #7A7A7A !important;
    }
    
    /* Markdown */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    .stMarkdown p {
        color: #B3B3B3 !important;
    }
    
    .stMarkdown strong {
        color: #FFFFFF !important;
    }
    
    .stMarkdown code {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        font-family: 'JetBrains Mono', monospace !important;
        padding: 0.125rem 0.25rem !important;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
    }
    
    /* Custom components */
    .code-stats {
        background-color: #1E1E1E !important;
        color: #7A7A7A !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.75rem !important;
        padding: 0.5rem 0.75rem !important;
        margin-top: 0.5rem !important;
        border: 1px solid #1E1E1E !important;
    }
    
    .placeholder-empty {
        text-align: center !important;
        padding: 3rem 2rem !important;
        color: #7A7A7A !important;
    }
    
    .placeholder-empty h3 {
        color: #B3B3B3 !important;
        font-size: 1.125rem !important;
        font-weight: 500 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .placeholder-empty p {
        color: #7A7A7A !important;
        font-size: 0.875rem !important;
    }
    
    .concept-item {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        color: #B3B3B3 !important;
        font-size: 0.875rem !important;
        padding: 0.75rem 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .misconception-item {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        border-left: 3px solid #7A7A7A !important;
        color: #B3B3B3 !important;
        font-size: 0.875rem !important;
        line-height: 1.5 !important;
        padding: 1rem !important;
        margin-bottom: 0.75rem !important;
    }
    
    .quiz-question {
        background-color: #0B0B0B !important;
        border: 1px solid #1E1E1E !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    }
    
    .quiz-question-text {
        color: #FFFFFF !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        line-height: 1.5 !important;
        margin-bottom: 0.75rem !important;
    }
    
    .quiz-answer {
        background-color: #1E1E1E !important;
        color: #B3B3B3 !important;
        font-size: 0.875rem !important;
        line-height: 1.5 !important;
        padding: 0.75rem 1rem !important;
        margin-top: 0.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)