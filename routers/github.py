from fastapi import APIRouter, HTTPException
from services.github_services import user_events, user_status
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
    
    return events