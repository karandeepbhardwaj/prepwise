from backend.chains.job_analyzer import analyze_job
from backend.chains.question_generator import generate_questions
from backend.chains.answer_coach import generate_answer_frameworks
from backend.chains.technical_prep import generate_study_guide
from backend.models.guide import PrepGuide

async def assemble_guide(title: str, content: str, company: str = "") -> PrepGuide:
    analysis = await analyze_job(title, content)

    questions = await generate_questions(
        title=title, requirements=analysis.get("key_requirements", []),
        experience_areas=analysis.get("experience_areas", []),
        seniority=analysis.get("seniority_level", "mid"),
    )

    behavioral_qs = [q for q in questions if q.category == "behavioral"]
    frameworks = await generate_answer_frameworks(title, behavioral_qs)

    topics = await generate_study_guide(
        title=title, requirements=analysis.get("key_requirements", []),
        experience_areas=analysis.get("experience_areas", []),
    )

    return PrepGuide(
        position_title=title, company=company,
        key_requirements=analysis.get("key_requirements", []),
        questions=questions, answer_frameworks=frameworks, technical_topics=topics,
        questions_to_ask=[
            f"What does a typical day look like for a {title} on this team?",
            "What are the biggest challenges the team is currently facing?",
            "How do you measure success in this role during the first 90 days?",
            "What opportunities for growth and learning does the team provide?",
            "Can you describe the team's development workflow and culture?",
        ],
        preparation_tips=[
            "Research the company's recent news, products, and engineering blog",
            "Prepare 2-3 concrete examples for each key requirement",
            "Practice explaining technical concepts clearly",
            "Review fundamentals of your core technical skills",
            "Prepare thoughtful questions showing genuine interest",
            "Test your setup if the interview is virtual",
        ],
    )
