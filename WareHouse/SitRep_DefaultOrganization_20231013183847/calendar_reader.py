'''
This file contains functions to read events from Microsoft Calendar.
'''
import os
from dotenv import load_dotenv
from msal import ConfidentialClientApplication
import requests

# Load environment variables from the .env file
load_dotenv()

def get_calendar_access_token():
    # Retrieve your Microsoft Calendar client ID and client secret from the environment variables
    client_id = os.environ.get("MICROSOFT_CALENDAR_CLIENT_ID")
    client_secret = os.environ.get("MICROSOFT_CALENDAR_CLIENT_SECRET")
    authority = os.environ.get("MICROSOFT_CALENDAR_AUTHORITY")

    if not (client_id and client_secret and authority):
        print("Please set the MICROSOFT_CALENDAR_CLIENT_ID, MICROSOFT_CALENDAR_CLIENT_SECRET, and MICROSOFT_CALENDAR_AUTHORITY environment variables in your .env file.")
        return None

    app = ConfidentialClientApplication(client_id, client_secret, authority)
    result = None
    try:
        result = app.acquire_token_for_client(scopes=["https://outlook.office365.com/.default"])
    except Exception as e:
        print(f"Error while acquiring token: {e}")
    
    return result

def read_events():
    access_token = get_calendar_access_token()

    if access_token and "access_token" in access_token:
        token = access_token["access_token"]
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # Define the Microsoft Calendar API endpoint
        url = "https://outlook.office365.com/api/v2.0/me/events"

        # Make a GET request to retrieve calendar events
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            events = response.json().get('value', [])
            return [event.get('subject', '') for event in events]
        else:
            print(f"Failed to retrieve events. Status code: {response.status_code}")
            return []

    print("Failed to obtain an access token.")
    return []

if __name__ == "__main__":
    events = read_events()

    if events:
        print("Events:")
        for event in events:
            print(event)
    else:
        print("Failed to retrieve events.")
