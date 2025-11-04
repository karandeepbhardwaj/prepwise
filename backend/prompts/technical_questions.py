TECHNICAL_QUESTIONS_PROMPT = """Generate technical interview questions for this role.

Position: {title}
Key Requirements: {requirements}
Experience Areas: {experience_areas}

Generate 7 technical questions. For each:
- question: The interview question
- category: "technical"
- difficulty: "easy", "medium", or "hard"
- what_they_assess: The skill being evaluated

Respond as a JSON array."""
