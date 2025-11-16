from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from backend.config import settings
from backend.models.guide import InterviewQuestion, AnswerFramework
from backend.prompts.answer_frameworks import ANSWER_FRAMEWORKS_PROMPT

async def generate_answer_frameworks(title: str, questions: list[InterviewQuestion]) -> list[AnswerFramework]:
    llm = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key, temperature=0.5)
    prompt = ChatPromptTemplate.from_template(ANSWER_FRAMEWORKS_PROMPT)
    parser = JsonOutputParser()
    chain = prompt | llm | parser
    questions_text = "\n".join(f"- {q.question}" for q in questions)
    result = await chain.ainvoke({"title": title, "questions": questions_text})
    return [AnswerFramework(**f) for f in result]
