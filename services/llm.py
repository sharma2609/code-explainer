"""
LLM Client for code analysis
Handles OpenAI API calls and response parsing
"""

import json
import os
from typing import Dict, Any, Optional
import openai
from openai import OpenAI

class LLMClient:
    """Client for interacting with OpenAI API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the LLM client"""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = "gpt-4"
    
    def analyze_code(self, code: str, language: str) -> Dict[str, Any]:
        """
        Analyze code and return structured explanation
        
        Args:
            code: The code to analyze
            language: Programming language
            
        Returns:
            Structured analysis as dictionary
        """
        try:
            prompt = self._get_analysis_prompt(code, language)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            if not content:
                raise ValueError("Empty response from LLM")
            
            # Parse JSON response
            analysis = json.loads(content)
            
            # Validate required fields
            required_fields = ["line_explanations", "concepts", "misconceptions", "quiz"]
            for field in required_fields:
                if field not in analysis:
                    raise ValueError(f"Missing required field: {field}")
            
            return analysis
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response from LLM: {e}")
        except openai.APIError as e:
            raise ValueError(f"OpenAI API error: {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error during code analysis: {e}")
    
    def _get_system_prompt(self) -> str:
        """Get the system prompt for educational code analysis"""
        return """You are a programming tutor for undergraduate students. Your goal is to explain code clearly, identify learning gaps, and avoid giving shortcuts or answers directly.

RULES:
- Use simple, clear language
- Focus on WHY each line exists, not just WHAT it does
- Identify common misconceptions students have
- Generate educational questions that test understanding
- Never solve assignments directly
- Maintain an encouraging, educational tone

Your explanations should help students understand the logic and flow, not just copy code."""
    
    def _get_analysis_prompt(self, code: str, language: str) -> str:
        """Generate the main prompt for code analysis"""
        return f"""Analyze the following {language} code line by line. For each line provide:

1. **What it does** (simple explanation)
2. **Why it exists** (purpose in the overall logic)
3. **What breaks if removed** (consequence)

Then provide:
- **Programming concepts used** (list key concepts)
- **Common misconceptions** (what students typically misunderstand)
- **3 concept-check questions** (test understanding, not memorization)

Code to analyze:
```{language}
{code}
```

Format your response as JSON with this structure:
{{
    "line_explanations": [
        {{
            "line_number": 1,
            "code": "actual line of code",
            "what_it_does": "simple explanation",
            "why_it_exists": "purpose explanation",
            "what_breaks": "consequence if removed"
        }}
    ],
    "concepts": ["concept1", "concept2"],
    "misconceptions": [
        "Students often misunderstand..."
    ],
    "quiz": [
        {{
            "question": "Why does this code use a loop instead of direct access?",
            "answer": "Because...",
            "concept": "iteration"
        }}
    ]
}}"""