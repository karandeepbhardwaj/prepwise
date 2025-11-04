JOB_ANALYSIS_PROMPT = """Analyze the following job description and extract key information.

Job Title: {title}
Job Description:
{content}

Extract the following in JSON format:
1. key_requirements: List of 5-8 most important skills and qualifications
2. experience_areas: List of domains the candidate should have experience in
3. seniority_level: The seniority level (junior, mid, senior, lead, principal)

Respond only with valid JSON."""
