from os import environ, path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

def get_calendar_events():
    credentials = None
    # Load credentials from a file or environment variable
    if 'GOOGLE_APPLICATION_CREDENTIALS' in environ: 
        google_credentials_path = environ['GOOGLE_APPLICATION_CREDENTIALS']
        # Ensure the environment variable points to a valid credentials file
        if google_credentials_path:
            credentials = Credentials.from_authorized_user_file(google_credentials_path)
        else: environ['GOOGLE_APPLICATION_CREDENTIALS'] = input("Please provide the path to your Google credentials file: ")
        # If the environment variable is not set, you can prompt for it or use a default path
        credentials = Credentials.from_authorized_user_file(environ['GOOGLE_APPLICATION_CREDENTIALS'])
    else:
        # Fallback to a specific file path
        if 'credentials.json' in path.exists(): credentials = Credentials.from_authorized_user_file('credentials.json')
    # Initialize the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)
    try:
        # Call the Calendar API to get the list of events
        events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        return events_result.get('items', [])
    
    except HttpError as error: print(f'An error occurred: {error}')

    def send_nudge():
        events = get_calendar_events()
        for event in events:
            nudge_message = f"Reminder: {event['summary']} is scheduled for {event['start'].get('dateTime', event['start'].get('date'))}."
            client.chat_postMessage(channel="general", text=nudge_message)
