# Discord Bot for Email Notifications

This project is a Python-based Discord bot that listens to messages in a specific channel on Discord and sends the content of each message as an email notification. This bot can be particularly useful for monitoring channels that log events, updates, or other critical messages that need to be forwarded via email.

## Features

- Connects to a Discord channel and listens for new messages.
- Sends each message in the specified channel as an email to a designated recipient.
- Configurable settings for Discord token, email credentials, channel ID, and more.

## Prerequisites

- Python 3.6+
- `discord.py` library for Discord API interactions.
- `smtplib` for handling email transmission.
- A Gmail account for sending emails (or other SMTP service with slight modifications).

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/discord-email-bot.git
cd discord-email-bot
```
### 2. Install Dependencies
Set up a virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate  # on Linux/macOS
.venv\Scripts\activate     # on Windows

pip install discord.py
```
### 3. Configure Environment Variables
Create a config.txt file in the root directory of the project. This file should contain the necessary configuration variables:

```plain
python3 -m venv .venv
source .venv/bin/activate  # on Linux/macOS
.venv\Scripts\activate     # on Windows

pip install discord.py
```
### 4. Running the Bot
Once configured, start the bot with:

```bash
python main.py
```

You should see an output indicating that the bot has successfully connected to Discord. It will listen for messages in the specified channel and send email notifications accordingly.

### Important Note
Ensure your Gmail account has an app-specific password if using two-factor authentication. Alternatively, use an email service that supports SMTP.

## File Structure

main.py: Main script that initializes the Discord bot, listens for messages, and sends email notifications.
config.txt: Configuration file containing Discord token, Gmail credentials, channel ID, and other necessary settings.

### Security Recommendations

Avoid hardcoding sensitive information directly into the code.
Use .gitignore to prevent config.txt from being uploaded to version control.

### License

This project is licensed under the MIT License. See the LICENSE file for more information.