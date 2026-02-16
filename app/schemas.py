from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str


class HealthResponse(BaseModel):
    status: str

class VersionResponse(BaseModel):
    model_version: str

class HomeResponse(BaseModel):
    message: str