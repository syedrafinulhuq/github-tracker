from fastapi import FastAPI,HTTPException, status
import httpx
import main.py

@app.get("/user-status/{username}")
async def user_status(username:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API}/users/{username}")
        print(f"client: {client}")
        print(f"user response: {response}")
    
    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found"
        )
    return{
        "username": {username},
        "status": "active",
        "profile_url": response.json().get("html_url")
    }
