import discord
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

# Configurazione
config = configparser.ConfigParser()
config.read('config.txt')

TOKEN = config.get('DEFAULT', 'TOKEN')
GMAIL_USER = config.get('DEFAULT', 'GMAIL_USER')
GMAIL_PASSWORD = config.get('DEFAULT', 'GMAIL_PASSWORD')
EMAIL_DEST = config.get('DEFAULT', 'EMAIL_DEST')
CHANNEL_ID = int(config.get('DEFAULT', 'CHANNEL_ID'))
SUBJECT = config.get('DEFAULT', 'SUBJECT')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def send_email(subject, content):
    # Configurazione email
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = EMAIL_DEST
    msg['Subject'] = subject

    # Corpo dell'email
    msg.attach(MIMEText(content, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, EMAIL_DEST, msg.as_string())
        server.quit()
        print("Email inviata con successo")
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")


@client.event
async def on_ready():
    print(f'Connesso come {client.user}')


@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        content = message.content
        send_email(SUBJECT, content)


client.run(TOKEN)
