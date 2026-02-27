import httpx
from github import get_user_events

GITHUB_API = "https://api.github.com"


async def user_status(username:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API}/users/{username}")
        print(f"user_status_client :{client}")
        print(f"user_status_response :{response}")
    
    if response.status_code == 404:
       return None
    
    return response.json()


async def user_events(username:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API}/users/{username}/events")
        print(f"user_event_client :{client}")
        print(f"user_event_response :{response}")

    return response.json()


async def user_repos(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API}/users/{username}/repos")
        print(f"user_repos_client :{client}")
        print(f"user_repos_response :{response}")
    
    return response.json()


def format_events(events: list):
    formatted_res = []
    
    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        
    # Output Format: 
    # - Pushed 3 commits to kamranahmedse/developer-roadmap
    # - Opened a new issue in kamranahmedse/developer-roadmap
    # - Starred kamranahmedse/developer-roadmap
    # - ...
        if event_type == "PushEvent":
            commit_count = len(event["payload"]["commits"])
            formatted_res.append(
                f"Pushed {commit_count} commits to {repo_name}"
            )
            


