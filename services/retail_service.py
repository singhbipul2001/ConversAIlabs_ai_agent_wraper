import requests

def create_retell_agent(request):
    url = "https://api.retellai.com/agents"  # This is the endpoint to create agent
    headers = {
        "Authorization": "Bearer YOUR_RETELL_API_KEY",  # Replace with your real API key
        "Content-Type": "application/json"
    }
    payload = {
        "title": request.name,        # Retell uses 'title' instead of 'name'
        "language": request.language
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
