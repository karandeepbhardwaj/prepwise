from pydantic import BaseModel

class InterviewQuestion(BaseModel):
    question: str
    category: str
    difficulty: str
    what_they_assess: str

class AnswerFramework(BaseModel):
    question: str
    situation: str
    task: str
    action: str
    result: str

class TechnicalTopic(BaseModel):
    topic: str
    relevance: str
    key_points: list[str]

class PrepGuide(BaseModel):
    position_title: str
    company: str
    key_requirements: list[str]
    questions: list[InterviewQuestion]
    answer_frameworks: list[AnswerFramework]
    technical_topics: list[TechnicalTopic]
    questions_to_ask: list[str]
    preparation_tips: list[str]
