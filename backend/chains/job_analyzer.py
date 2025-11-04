from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from backend.config import settings
from backend.prompts.job_analysis import JOB_ANALYSIS_PROMPT

async def analyze_job(title: str, content: str) -> dict:
    llm = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key, temperature=0.3)
    prompt = ChatPromptTemplate.from_template(JOB_ANALYSIS_PROMPT)
    parser = JsonOutputParser()
    chain = prompt | llm | parser
    return await chain.ainvoke({"title": title, "content": content})
