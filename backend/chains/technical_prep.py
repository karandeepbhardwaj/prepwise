from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from backend.config import settings
from backend.models.guide import TechnicalTopic
from backend.prompts.study_guide import STUDY_GUIDE_PROMPT

async def generate_study_guide(title: str, requirements: list[str], experience_areas: list[str]) -> list[TechnicalTopic]:
    llm = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key, temperature=0.3)
    prompt = ChatPromptTemplate.from_template(STUDY_GUIDE_PROMPT)
    parser = JsonOutputParser()
    chain = prompt | llm | parser
    result = await chain.ainvoke({"title": title, "requirements": ", ".join(requirements), "experience_areas": ", ".join(experience_areas)})
    return [TechnicalTopic(**t) for t in result]
