from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import products_routes

allowed_origins = [
    
]

app = FastAPI()

# app.add_middleware(CORSMiddleware(
#     allowed_origins
# ))

app.include_router(products_routes.router)

@app.get("/", tags=["homepage"], summary="the homepage", status_code=200)
def root():
    return { "description" : " Welcome to the Multikart Backend Api" }
