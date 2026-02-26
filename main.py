from fastapi import FastAPI
from routers.github import router as github_router

app = FastAPI()

app.include_router(github_router)