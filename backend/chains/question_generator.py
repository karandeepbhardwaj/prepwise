from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from backend.config import settings
from backend.models.guide import InterviewQuestion
from backend.prompts.behavioral_questions import BEHAVIORAL_QUESTIONS_PROMPT
from backend.prompts.technical_questions import TECHNICAL_QUESTIONS_PROMPT

async def generate_questions(title: str, requirements: list[str], experience_areas: list[str], seniority: str) -> list[InterviewQuestion]:
    llm = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key, temperature=0.5)
    parser = JsonOutputParser()

    behavioral_chain = ChatPromptTemplate.from_template(BEHAVIORAL_QUESTIONS_PROMPT) | llm | parser
    technical_chain = ChatPromptTemplate.from_template(TECHNICAL_QUESTIONS_PROMPT) | llm | parser

    behavioral = await behavioral_chain.ainvoke({"title": title, "requirements": ", ".join(requirements), "seniority": seniority})
    technical = await technical_chain.ainvoke({"title": title, "requirements": ", ".join(requirements), "experience_areas": ", ".join(experience_areas)})

    return [InterviewQuestion(**q) for q in behavioral + technical]
