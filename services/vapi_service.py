import requests

def create_vapi_agent(request):
    url = "https://api.vapi.ai/assistants"  # This is the endpoint to create agent
    headers = {
        "Authorization": "Bearer YOUR_VAPI_API_KEY",  # Replace with your real API key
        "Content-Type": "application/json"
    }
    payload = {
        "name": request.name,
        "language": request.language
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
