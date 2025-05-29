from os import getenv, environ
from slack_sdk.web import WebClient
from slack_sdk.rtm_v2 import RTMClient

SLACK_BOT_TOKEN = getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = getenv("SLACK_APP_TOKEN")

if not SLACK_BOT_TOKEN: environ["SLACK_BOT_TOKEN"] = input("Type in your slack bot token: ")
if not SLACK_APP_TOKEN: environ["SLACK_APP_TOKEN"] = input("Type in your slack app token: ")

while True:
    try: 
        client = WebClient(token=SLACK_BOT_TOKEN)
        break
    except KeyBoardInterrupt:
        print("Exiting...")
        exit(0)
    except Exception as e:
        print(f"Error creating WebClient: {e}")
        SLACK_BOT_TOKEN = input("Please re-enter your Slack bot token: ")
        environ["SLACK_BOT_TOKEN"] = SLACK_BOT_TOKEN
        continue

def processMessage(data):
    if 'text' in data:
        user_message = data['text']
        response = generate_ai_response(user_message)
        if response:
            try: client.chat_postMessage(channel=data['channel'], text=response)
            except Exception as e: print(f"Error sending message: {e}")

while True:
    try:
        rtm_client = RTMClient(token=SLACK_APP_TOKEN)
        rtm_client.on("message")(processMessage)
        rtm_client.start()
        break
    except Exception as e:
        print(f"Error starting RTM client: {e}")
        SLACK_APP_TOKEN = input("Please re-enter your Slack app token: ")
        environ["SLACK_APP_TOKEN"] = SLACK_APP_TOKEN
        continue
