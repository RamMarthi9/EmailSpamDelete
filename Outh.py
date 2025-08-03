import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CREDENTIALS_PATH = 'C:/Users/ramma/Documents/Ram/Preparation/AI Agents/EmailSpamCleaner-ESC-Credentials-Tokens/credential.json'
TOKEN_PATH = 'C:/Users/ramma/Documents/Ram/Preparation/AI Agents/EmailSpamCleaner-ESC-Credentials-Tokens/token.json'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify'] # Or gmail.readonly if you just want to identify

def get_gmail_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

if __name__ == '__main__':
    service = get_gmail_service()
    print("Successfully authenticated with Gmail API!")
    # You can add a simple test here, e.g., print your profile
    profile = service.users().getProfile(userId='me').execute()
    print(f"Authenticated as: {profile['emailAddress']}")