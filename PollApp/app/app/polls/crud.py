from sqlalchemy import select
from sqlalchemy.orm import Session


from polls import models

def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()
    
def get_all_questions(db: Session):
    return db.query(models.Question).all()