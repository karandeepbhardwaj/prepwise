ANSWER_FRAMEWORKS_PROMPT = """Create STAR method answer frameworks for these behavioral questions.

Position: {title}
Questions: {questions}

For each question, create a framework:
- question: The original question
- situation: A realistic professional situation (1-2 sentences)
- task: What needed to be accomplished (1 sentence)
- action: Specific steps to take (2-3 sentences)
- result: Measurable outcome (1-2 sentences)

Respond as a JSON array."""
