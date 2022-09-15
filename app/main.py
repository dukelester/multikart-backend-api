from fastapi import FastAPI
from routes import products_routes
from models import products_models
from database.database import engine

allowed_origins = [
    
]

products_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.add_middleware(CORSMiddleware(
#     allowed_origins
# ))


app.include_router(products_routes.router)

@app.get("/", tags=["homepage"], summary="the homepage", status_code=200)
def root():
    return { "description" : " Welcome to the Multikart Backend Api" }

