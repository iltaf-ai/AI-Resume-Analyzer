from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import settings


model = ChatMistralAI(
    model="mistral-medium-latest"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an AI Resume Analyzer.

        Analyze the given resume and provide:
        1. Resume score
        2. Skills
        3. Strengths
        4. Weaknesses
        5. Improvement suggestions
        6. Career roadmap
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