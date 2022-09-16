from fastapi import FastAPI
from polls import endpoints
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(endpoints.router)

@app.get("/")
def root():
    return { "message": "Welcome to the Polls App" }