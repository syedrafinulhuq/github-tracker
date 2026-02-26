from fastapi import FastAPI,HTTPException, status
import httpx

app = FastAPI()
GITHUB_API = "https://api.github.com"


@app.get("/")
def main():
    return {"message": "Github User Events Tracker"}







    
