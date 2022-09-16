from fastapi import APIRouter, HTTPException,Depends
from . import schemas, crud
from app.database import SessionLocal



# Database session as a dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
router = APIRouter(
    prefix="/polls",
    tags=["polls"]
)

async def index(db=Depends(get_db)):
    return crud.list_questions(db)


@router.get("/{id}/", response_model=schemas.ReadQuestionChoices)
async def question_detail(id: int, db=Depends(get_db)):
    try:
        return crud.get_question(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Token does not exist",) from e