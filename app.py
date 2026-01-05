"""
Code Understanding Assistant - Streamlit Version
Clean, educational, NothingOS-inspired design
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our modules
from services.analyzer import CodeAnalyzer
from ui.theme import apply_theme

# Page config
st.set_page_config(
    page_title="Code Understanding Assistant",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply NothingOS theme
apply_theme()

def main():
    # Custom header
    st.markdown("""
    <div class="custom-header">
        <h1>Code Understanding Assistant</h1>
        <p>Understand your code, don't just copy it</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'analysis' not in st.session_state:
        st.session_state.analysis = None
    if 'quiz_revealed' not in st.session_state:
        st.session_state.quiz_revealed = {}
    
    # Main layout - simple two columns
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("### Code Input")
        
        # Language selector
        language = st.selectbox(
            "Programming Language",
            ["python", "javascript", "java", "cpp", "c"],
            index=0
        )
        
        # Code input
        code = st.text_area(
            "Enter your code",
            height=350,
            placeholder="# Paste your code here to understand it\n# Try this example:\n\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nresult = fibonacci(5)\nprint(f'Result: {result}')"
        )
        
        # Analyze button
        if st.button("🔍 Analyze Code", type="primary", use_container_width=True):
            if code.strip():
                with st.spinner("🧠 Analyzing your code..."):
                    try:
                        analyzer = CodeAnalyzer()
                        analysis = analyzer.analyze_code(code, language)
                        st.session_state.analysis = analysis
                        st.session_state.quiz_revealed = {}
                        st.success("✅ Analysis complete!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Analysis failed: {str(e)}")
            else:
                st.warning("⚠️ Please enter some code to analyze")
        
        # Code stats
        if code.strip():
            lines = len([line for line in code.split('\n') if line.strip()])
            chars = len(code)
            st.markdown(f"""
            <div class="code-stats">
                📊 {lines} lines • {chars} characters • {language.upper()}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Analysis Results")
        
        if st.session_state.analysis:
            # Tabs for different analysis views
            tab1, tab2, tab3, tab4 = st.tabs([
                "📝 Explanations", 
                "🧠 Concepts", 
                "⚠️ Misconceptions", 
                "❓ Quiz"
            ])
            
            with tab1:
                show_explanations(st.session_state.analysis)
            
            with tab2:
                show_concepts(st.session_state.analysis)
            
            with tab3:
                show_misconceptions(st.session_state.analysis)
            
            with tab4:
                show_quiz(st.session_state.analysis)
        else:
            # Empty state
            st.markdown("""
            <div class="placeholder-empty">
                <h3>Ready to analyze your code</h3>
                <p>Paste code in the editor and click "Analyze Code"</p>
            </div>
            """, unsafe_allow_html=True)

def show_explanations(analysis):
    """Display line-by-line explanations"""
    explanations = analysis.get('line_explanations', [])
    if not explanations:
        st.info("No explanations available")
        return
    
    for i, explanation in enumerate(explanations):
        line_code = explanation['code'].strip()
        if len(line_code) > 50:
            line_code = line_code[:47] + "..."
        
        with st.expander(f"**Line {explanation['line_number']}** • `{line_code}`", expanded=i < 2):
            # Show full code if truncated
            if len(explanation['code'].strip()) > 50:
                st.code(explanation['code'], language='python')
            
            st.markdown(f"**🔍 What it does:** {explanation['what_it_does']}")
            st.markdown(f"**🎯 Why it exists:** {explanation['why_it_exists']}")
            st.markdown(f"**💥 What breaks:** {explanation['what_breaks']}")

def show_concepts(analysis):
    """Display programming concepts"""
    concepts = analysis.get('concepts', [])
    if not concepts:
        st.info("No concepts identified")
        return
    
    st.markdown("Key concepts used in your code:")
    
    for concept in concepts:
        concept_name = concept.replace('_', ' ').title()
        st.markdown(f"""
        <div class="concept-item">
            🔹 {concept_name}
        </div>
        """, unsafe_allow_html=True)

def show_misconceptions(analysis):
    """Display common misconceptions"""
    misconceptions = analysis.get('misconceptions', [])
    if not misconceptions:
        st.info("No misconceptions identified")
        return
    
    st.markdown("Areas where students often get confused:")
    
    for misconception in misconceptions:
        st.markdown(f"""
        <div class="misconception-item">
            {misconception}
        </div>
        """, unsafe_allow_html=True)

def show_quiz(analysis):
    """Display quiz questions"""
    questions = analysis.get('quiz', [])
    if not questions:
        st.info("No quiz questions available")
        return
    
    st.markdown("Test your understanding:")
    
    for i, question in enumerate(questions):
        st.markdown(f"""
        <div class="quiz-question">
            <div class="quiz-question-text">
                **Q{i + 1}:** {question['question']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Answer reveal button
        if st.button(f"💡 Reveal Answer", key=f"reveal_{i}", use_container_width=True):
            st.session_state.quiz_revealed[i] = True
        
        # Show answer if revealed
        if st.session_state.quiz_revealed.get(i, False):
            st.markdown(f"""
            <div class="quiz-answer">
                <strong>Answer:</strong> {question['answer']}
            </div>
            """, unsafe_allow_html=True)
            
            if 'concept' in question:
                st.markdown(f"**Related Concept:** {question['concept'].replace('_', ' ').title()}")

if __name__ == "__main__":
    main()