from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.config import settings


model = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=settings.OPENAI_API_KEY
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Resume Analyzer.

Analyze the given resume and provide:

1. Resume score out of 100
2. Skills
3. Strengths
4. Weaknesses
5. Improvement suggestions
6. Career roadmap

Give clear and practical feedback based only on the resume.
"""
    ),
    (
        "human",
        """
Analyze this resume:

{resume}
"""
    )
])


def analyze_resume(resume: str):

    chat = prompt.invoke({
        "resume": resume
    })

    response = model.invoke(chat)

    return response.content