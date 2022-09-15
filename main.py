from fastapi import FastAPI
from app.routes import products_routes, rating_routes
from app.models import products_models
from app.database.database import engine

allowed_origins = [
    
]

products_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.add_middleware(CORSMiddleware(
#     allowed_origins
# ))


app.include_router(products_routes.router)
app.include_router(rating_routes.router)

@app.get("/", tags=["homepage"], summary="the homepage", status_code=200)
def root():
    return { "description" : " Welcome to the Multikart Backend Api" }

