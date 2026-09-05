from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model = "small-mistral-latest"

)

prompt = ChatPromptTemplate([
    ("system", 
    
    """Summarizes the Resume
    - Road Map Explantion
    - """),

    ("human",
    """
    {resume}
    """
    )
])

def resume_analyzer(resume):
    message = prompt.invoke({
        "reusme": resume
    })

    result = model.invoke(message)

    return result.content




