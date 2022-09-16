from pydantic import BaseModel
from datetime import  datetime

class BaseQuestion(BaseModel):
    id: int
    question_text: str
    published_date: datetime
    
    class Config:
        orm_mode = True
        
class BaseChoice(BaseModel):
    choice_text: str
    votes: int
    
    class Config:
        orm_mode = True

class ReadQuestion(BaseQuestion):
    id: int
        
class ReadQuestionChoices(ReadQuestion):
    id: int
    question_text: str
    pub_date: datetime
    choices: list[BaseChoice]

    class Config:
        orm_mode = True
    