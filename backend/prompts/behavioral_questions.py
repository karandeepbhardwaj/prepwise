BEHAVIORAL_QUESTIONS_PROMPT = """Based on this job analysis, generate likely behavioral interview questions.

Position: {title}
Key Requirements: {requirements}
Seniority Level: {seniority}

Generate 8 behavioral interview questions. For each:
- question: The interview question
- category: "behavioral"
- difficulty: "easy", "medium", or "hard"
- what_they_assess: What the interviewer is evaluating

Respond as a JSON array."""
