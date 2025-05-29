from slackbot import start_slackbot
from calendar_nudges import send_nudge
from onboarding import onboarding_path
from dashboard import generate_dashboard
from ai_coach import generate_ai_response
from content_scheduler import schedule_messages

def main():
    print("Starting Slack Bot...")
    start_slackbot()
    schedule_messages()
    send_nudge()
    generate_dashboard()
    onboarding_path()
    generate_ai_response()
    print("Slack Bot is running...")
    
if __name__ == "__main__": main()
