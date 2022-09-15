from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Welcome to the Polls App" }