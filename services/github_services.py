import httpx

GITHUB_API = "https://api.github.com"


async def user_status(username:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API}/users/{username}")
        print(f"client: {client}")
        print(f"user response: {response}")
    
    if response.status_code == 404:
       return None
    
    return response.json()


async def user_events()
