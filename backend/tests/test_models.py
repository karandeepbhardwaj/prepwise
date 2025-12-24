from backend.models.guide import PrepGuide, InterviewQuestion, AnswerFramework, TechnicalTopic

def test_prep_guide_creation():
    guide = PrepGuide(
        position_title="Software Engineer", company="Acme", key_requirements=["Python"],
        questions=[InterviewQuestion(question="Tell me about yourself", category="behavioral", difficulty="easy", what_they_assess="Communication")],
        answer_frameworks=[AnswerFramework(question="Tell me about yourself", situation="At my previous company", task="I needed to introduce myself", action="I prepared a brief summary", result="The interviewer was impressed")],
        technical_topics=[TechnicalTopic(topic="Python", relevance="Core language", key_points=["Data structures", "OOP"])],
        questions_to_ask=["What's the team like?"], preparation_tips=["Research the company"],
    )
    assert guide.position_title == "Software Engineer"
    assert len(guide.questions) == 1
