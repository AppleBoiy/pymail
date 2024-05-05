# Email Sender Script

This Python script sends an email using Gmail SMTP. It loads sender credentials and recipient email address from environment variables, and the email content from a file. The script supports sending both plain text and HTML emails.

## Prerequisites

- Python 3.x installed on your system
- Gmail account for sending emails
- Enable "Less secure app access" or set up an "App password" for Gmail (if using 2-step verification)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/AppleBoiy/pymail.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the project directory and add the following variables:

    ```
    EMAIL_SENDER=your_email@gmail.com
    PASSWORD_SENDER=your_gmail_password_or_app_password
    RECEIVER_EMAIL=recipient_email@example.com
    ```

    Replace `your_email@gmail.com` with your Gmail email address, `your_gmail_password_or_app_password` with your Gmail password or app password, and `recipient_email@example.com` with the recipient's email address.

## Usage

Run the script `main.py` to send the email:

```bash
python main.py
```

## Customization

- Modify the `payload.html` file to customize the email content.
- Adjust the logging configuration in the script as needed.
- Extend the script with additional features like attachments or multiple recipients.

## License

[MIT License](LICENSE)