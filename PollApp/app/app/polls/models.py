from sqlalchemy import Column, String, Integer,DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from  database import Base

class Question(Base):
    __tablename__="questions"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    question_text = Column(String,nullable=False, index=True )
    published_date = Column(DateTime, default=datetime.now())
    
    choices = relationship('Choice', backref="question")
    
class Choice(Base):
    __tablename__='choices'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    choice_text =  Column(String,nullable=False, index=True )
    votes = Column(Integer, nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id') )
    