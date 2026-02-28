import httpx

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
        event_type = event.get("type")
        repo_name = event.get("repo",{}).get("name","unidentified repo")
        payload = event.get("payload",{})
        
    # Output Format: 
    # - Pushed 3 commits to kamranahmedse/developer-roadmap
    # - Opened a new issue in kamranahmedse/developer-roadmap
    # - Starred kamranahmedse/developer-roadmap
    # - ...
        if event_type == "PushEvent":
            commits = payload.get("commits",[])
            commit_count = len(commits)
            formatted_res.append(
                f"Pushed {commit_count} commits to {repo_name}"
            )
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            formatted_res.append(
                f"Opened a new issue in {action}"
            )

        elif event_type == "WatchEvent":
            starred = event["repo"]["name"]
            formatted_res.append(
                f"Starred {starred}"
            )

    return formatted_res
