import os
import ssl
import smtplib
import logging
import re
from dotenv import load_dotenv
from email.message import EmailMessage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_credentials():
    """
    Load email sender credentials from environment variables.
    Returns:
        (str, str): Tuple containing sender email and password.
    """
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("PASSWORD_SENDER")
    if not sender_email or not sender_password:
        raise ValueError("Sender email or password not found in environment variables.")
    return sender_email, sender_password


def validate_email(email):
    """
    Validate email address format.
    Args:
        email (str): Email address to validate.
    Returns:
        bool: True if email address is valid, False otherwise.
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True


def send_email(receiver_email, subject, body, is_html=False):
    """
    Send an email.
    Args:
        receiver_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body content of the email.
    """
    if not validate_email(receiver_email):
        logger.error("Invalid recipient email address.")
        return

    sender_email, sender_password = load_credentials()

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    if is_html:
        message.set_content(body, subtype="html")
    else:
        message.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(message)
            logger.info("Email sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")


if __name__ == "__main__":
    load_dotenv()
    receiver_email = os.getenv("RECEIVER_EMAIL")
    if not receiver_email:
        logger.error("Recipient email address not found in environment variables.")
    else:
        subject = "This is a test subject."
        # Read HTML content from file
        with open("payload.html", "r") as file:
            body = file.read()
        send_email(receiver_email, subject, body, is_html=True)
