# Code Understanding Assistant

A clean, educational AI-powered tool that explains code line-by-line, identifies programming concepts, and generates learning quizzes. Built with Streamlit and designed with a NothingOS-inspired monochrome aesthetic.

## Features

- **Line-by-Line Explanations**: Understand what each line does, why it exists, and what breaks if removed
- **Concept Identification**: Learn the programming concepts used in your code
- **Misconception Detection**: Avoid common pitfalls and misunderstandings that students face
- **Educational Quizzes**: Test your understanding with AI-generated questions
- **Clean Interface**: Distraction-free, monochrome design focused on learning
- **Multiple Languages**: Support for Python, JavaScript, Java, C++, and C

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for AI-powered analysis)

### Installation

1. **Clone or download the project**

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**

   Create a `.env` file in the project root:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application:**

   ```bash
   streamlit run app.py
   ```

5. **Open in your browser:**
   ```
   http://localhost:8501
   ```

## How to Use

1. **Select your programming language** from the dropdown
2. **Paste or type your code** in the editor
3. **Click "Analyze Code"** to get AI-powered insights
4. **Explore the results** through different tabs:
   - **Explanations**: Line-by-line breakdown
   - **Concepts**: Programming concepts used
   - **Misconceptions**: Common student pitfalls
   - **Quiz**: Test your understanding

## Project Structure

```
├── app.py              # Main Streamlit application
├── services/           # Core business logic
│   ├── llm.py         # OpenAI API integration
│   └── analyzer.py    # Code analysis coordinator
├── ui/                # UI components and styling
│   └── theme.py       # NothingOS-inspired theme
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (create this)
└── README.md         # This file
```

## Supported Languages

- **Python** - Full support with syntax highlighting
- **JavaScript** - ES6+ features supported
- **Java** - Object-oriented programming concepts
- **C++** - Modern C++ standards
- **C** - Procedural programming fundamentals

## Design Philosophy

This tool follows a **NothingOS-inspired design philosophy**:

- **Monochrome aesthetic** - Pure black, white, and gray color scheme
- **Minimal interface** - No distractions, focus on content
- **Clean typography** - Inter for UI, JetBrains Mono for code
- **Educational focus** - Designed for learning, not just explanation

## Technical Stack

- **Frontend**: Streamlit with custom CSS
- **Backend**: Python with OpenAI API integration
- **AI**: GPT-4 for code analysis and explanation
- **Styling**: Custom CSS for NothingOS aesthetic

## Notes

- The app works with mock data when no OpenAI API key is provided
- Analysis quality depends on code complexity and language
- Designed for educational purposes and learning enhancement
