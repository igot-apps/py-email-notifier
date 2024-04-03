import imaplib
import email
import time
from bs4 import BeautifulSoup
from imapclient import IMAPClient
import pygame

# Define IMAP server settings for Hotmail
IMAP_SERVER = 'imap-mail.outlook.com'
IMAP_PORT = 993

# Define email account credentials
EMAIL_ADDRESS = 'username@hotmail.com'
EMAIL_PASSWORD = 'your_hotmail_password'

# Default time interval for checking emails (in seconds)
CHECK_INTERVAL = 60

# Initialize pygame
pygame.mixer.init()

# Load the song
pygame.mixer.music.load("./song.mp3")

# Function to process emails
def process_emails(keywords):
    try:
        # Connect to the IMAP server with an increased timeout value
        with IMAPClient(IMAP_SERVER, port=IMAP_PORT, use_uid=True) as mail:
            mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Select the mailbox (inbox by default)
            mail.select_folder('INBOX')

            # Check for new messages
            unseen_msgs = mail.search('UNSEEN')

            for msg_id in unseen_msgs:
                # Fetch the email data for each message number
                raw_email = mail.fetch([msg_id], ['RFC822'])[msg_id][b'RFC822']
                msg = email.message_from_bytes(raw_email)

                # Get the subject and sender of the email
                subject = msg['Subject']
                sender = msg['From']

                # Extract the message body
                body = extract_email_body(msg)

                print('New Email:')
                print('Subject:', subject)
                print('From:', sender)
                print('Content:', body)

                # Check if any of the keywords are present in the email subject or body
                found_keywords = [keyword for keyword in keywords if keyword.lower() in subject.lower() or keyword.lower() in body.lower()]
                if found_keywords:
                    print(f"Email found with the specified keywords: {', '.join(found_keywords)}")
                    # Play the song
                    pygame.mixer.music.play()
                    # Wait for the song to finish playing
                    while pygame.mixer.music.get_busy():
                        continue
                else:
                    print("Email not found with the specified keywords.")
    except (imaplib.IMAP4.error, ConnectionError) as e:
        print("An error occurred while connecting to the mail server:", e)
    except Exception as e:
        print("An error occurred while processing emails:", e)

# Function to extract email body
def extract_email_body(msg):
    body = ""
    try:
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body = part.get_payload(decode=True).decode()
                elif content_type == 'text/html':
                    html_body = part.get_payload(decode=True).decode()
                    soup = BeautifulSoup(html_body, 'html.parser')
                    body = soup.get_text()
                else:
                    body = None
        else:
            body = msg.get_payload(decode=True).decode()
    except Exception as e:
        print("An error occurred while extracting email body:", e)
    return body

# Function to start monitoring emails
def start_monitoring_emails(keywords):
    print("Starting email monitoring...")
    while True:
        process_emails(keywords)
        time.sleep(CHECK_INTERVAL)

# Function to update time interval for checking emails
def update_check_interval():
    global CHECK_INTERVAL
    try:
        interval = int(input("Enter new time interval in seconds: "))
        if interval > 0:
            CHECK_INTERVAL = interval
            print("Check interval updated successfully.")
        else:
            print("Invalid interval. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Function to update keywords to monitor
def update_keywords(keywords):
    global CHECK_INTERVAL
    new_keywords = input("Enter new comma-separated list of keywords to monitor: ")
    keywords.clear()
    keywords.extend([keyword.strip() for keyword in new_keywords.split(",")])
    print("Keywords updated successfully.")

# Numbered Menu
def display_menu():
    print("\nNumbered Menu:")
    print("1. Start monitoring emails")
    print("2. Set time interval for checking emails")
    print("3. Update keywords to monitor")
    print("4. Exit")

keywords = []

while True:
    display_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        start_monitoring_emails(keywords)
    elif choice == '2':
        update_check_interval()
    elif choice == '3':
        update_keywords(keywords)
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")