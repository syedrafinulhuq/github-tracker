from fastapi import APIRouter, HTTPException
from services.github_services import format_events,user_events, user_status,user_repos
import httpx

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/user-status/{username}")
async def get_user_status(username:str):
    user = await user_status(username)

    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    else:
        return {
            "username": username,
            "status": "active",
            "profile_url": user.get("html_url")
        }
    


@router.get("/user-events/{username}")
async def get_user_events(username:str):
    events = await user_events(username)

    if events is None:
        raise HTTPException(status_code=404, detail="There's No Event")
    
    formatted = format_events(events)

    return formatted



@router.get("/user-repos/{username}")
async def get_user_repos(username: str):
    repos = await user_repos(username)

    if repos is None:
         raise HTTPException(status_code =404, detail ="There's No Repos")
    return repos
