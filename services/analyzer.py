"""
Code Analyzer - Main analysis logic
Coordinates LLM calls and response processing
"""

from typing import Dict, Any
from .llm import LLMClient

class CodeAnalyzer:
    """Main code analysis coordinator"""
    
    def __init__(self):
        """Initialize the analyzer"""
        try:
            self.llm_client = LLMClient()
        except ValueError as e:
            # Handle missing API key gracefully
            self.llm_client = None
            self.error_message = str(e)
    
    def analyze_code(self, code: str, language: str) -> Dict[str, Any]:
        """
        Analyze code and return structured explanation
        
        Args:
            code: The code to analyze
            language: Programming language
            
        Returns:
            Structured analysis dictionary
        """
        if not self.llm_client:
            # Return mock data if no API key
            return self._get_mock_analysis(code, language)
        
        # Validate inputs
        if not code.strip():
            raise ValueError("Code cannot be empty")
        
        supported_languages = ["python", "javascript", "java", "cpp", "c"]
        if language.lower() not in supported_languages:
            raise ValueError(f"Language '{language}' not supported. Supported: {supported_languages}")
        
        # Get AI analysis
        try:
            analysis = self.llm_client.analyze_code(code, language)
            return analysis
        except Exception as e:
            raise ValueError(f"Analysis failed: {str(e)}")
    
    def _get_mock_analysis(self, code: str, language: str) -> Dict[str, Any]:
        """
        Return mock analysis when API key is not available
        Useful for testing UI without OpenAI API
        """
        lines = code.strip().split('\n')
        
        return {
            "line_explanations": [
                {
                    "line_number": i + 1,
                    "code": line.strip(),
                    "what_it_does": f"This line performs a {language} operation",
                    "why_it_exists": "It contributes to the overall program logic",
                    "what_breaks": "The program would not function correctly without this line"
                }
                for i, line in enumerate(lines[:5])  # Limit to first 5 lines for demo
            ],
            "concepts": ["variables", "functions", "control_flow"],
            "misconceptions": [
                f"Students often misunderstand how {language} handles this type of operation",
                "The execution order might be confusing for beginners"
            ],
            "quiz": [
                {
                    "question": f"What would happen if you removed the first line of this {language} code?",
                    "answer": "The program would likely fail or behave unexpectedly",
                    "concept": "program_structure"
                },
                {
                    "question": "Why is proper indentation important in this code?",
                    "answer": "It defines the code structure and execution flow",
                    "concept": "syntax"
                }
            ]
        }