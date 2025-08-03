from Outh import get_gmail_service

def delete_spam():
    service = get_gmail_service()
    # List messages in the SPAM label
    results = service.users().messages().list(userId='me', labelIds=['SPAM']).execute()
    messages = results.get('messages', [])
    print(f"Found {len(messages)} spam messages.")
    for msg in messages:
        msg_id = msg['id']
        # Delete the message
        service.users().messages().trash(userId='me', id=msg_id).execute()
        print(f"Deleted spam message with ID: {msg_id}")

if __name__ == '__main__':
    delete_spam()

def empty_bin():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['TRASH']).execute()
    messages = results.get('messages', [])
    print(f"Found {len(messages)} messages in bin.")
    for msg in messages:
        msg_id = msg['id']
        service.users().messages().trash(userId='me', id=msg_id).execute()
        print(f"Deleted spam message with ID: {msg_id}")

if __name__ == '__main__':
    delete_spam()
