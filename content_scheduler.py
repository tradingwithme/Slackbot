from time import sleep
from airtable import Airtable
from os import environ, getenv
from dotenv import load_dotenv
from schedule import every, run_pending

AIRTABLE_API_KEY = getenv("AIRTABLE_API_KEY")
if not AIRTABLE_API_KEY:
    load_dotenv()
    AIRTABLE_API_KEY = environ.get("AIRTABLE_API_KEY")
if not AIRTABLE_API_KEY: env["AIRTABLE_API_KEY"] = input("Enter your Airtable API Key: ")
AIRTABLE_BASE_ID = getenv("AIRTABLE_BASE_ID")
if not AIRTABLE_BASE_ID:
    load_dotenv()
    AIRTABLE_BASE_ID = environ.get("AIRTABLE_BASE_ID")
if not AIRTABLE_BASE_ID: env["AIRTABLE_BASE_ID"] = input("Enter your Airtable Base ID: ")

def fetch_weekly_content():
    at = Airtable(AIRTABLE_BASE_ID, "CoachingContent", api_key=AIRTABLE_API_KEY)
    return at.get_all()

def send_weekly_message():
    content = fetch_weekly_content()
    message = content[0]['fields'].get('Message', 'No message found')
    client.chat_postMessage(channel="general", text=message)

every().monday.at("09:00").do(send_weekly_message)

while True:
    run_pending()
    sleep(60)  # Sleep to prevent busy-waiting
