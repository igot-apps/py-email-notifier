# Email Notification System Readme
	Test and working with hotmail

This repository contains a Python script that monitors an email inbox for specific keywords and plays a song notification when an email containing those keywords is received. It uses the IMAP protocol to connect to the email server and fetches emails using the `imapclient` library. The script is intended to run on a local machine.

## Setup Instructions

### 1. Prerequisites

- Python 3.x installed on your system.
- Ensure the necessary Python libraries are installed. You can install them using pip:

pip install imapclient bs4 pygame

csharp
Copy code

### 2. Clone the Repository

Clone this repository to your local machine using Git:

git clone https://github.com/your_username/email-notification-system.git

markdown
Copy code

### 3. Configuration

Before running the script, you need to update the configuration variables in the script:

- `IMAP_SERVER`: The IMAP server address.
- `IMAP_PORT`: The port number for IMAP (usually 993 for secure connections).
- `EMAIL_ADDRESS`: Your email address.
- `EMAIL_PASSWORD`: Your email account password.
- `CHECK_INTERVAL`: Time interval (in seconds) for checking emails.

### 4. Run the Script

Navigate to the directory where the script is located and run it using Python:

python email_notification.py

sql
Copy code

## Usage

Once the script is running, you can interact with it through the numbered menu displayed in the terminal. Here are the available options:

1. **Start monitoring emails**: Begin monitoring the inbox for emails containing specified keywords.
2. **Set time interval for checking emails**: Change the time interval for checking emails.
3. **Update keywords to monitor**: Update the list of keywords to monitor for email notifications.
4. **Exit**: Terminate the script and exit the program.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE)