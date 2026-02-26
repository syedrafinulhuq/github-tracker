import httpx

GITHUB_API = "https://api.github.com"


async def user_status(username:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API}/users/{username}")
        print(f"user_status_client :{client}")
        print(f"user_status_response :{response}")
    
    if response.status_code == 404:
       return None
    
    return response


async def user_events(username:str):
    async with httpx.AsyncClient as client:
        response = await client.get(f"{GITHUB_API}/users/{username}/events")
        print(f"user_event_client :{client}")
        print(f"user_event_response :{response}")

    return response
