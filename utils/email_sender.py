import os.path
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


def send_email(recipients: list[str], mail_subject: str, mail_body: str, attachment: str = None) -> None:

    TOKEN_API = config.TOKEN_API
    USER = config.USER
    SMTP_SERVER = config.SMTP_SERVER

    msg = MIMEMultipart("alternative")
    msg["Subject"] = mail_subject
    msg["From"] = f"{USER} sent this email"
    msg["To"] = ", ".join(recipients)
    msg["Reply-To"] = USER
    msg["Return-Path"] = USER
    msg["X-Mailer"] = "decorator"

    if attachment:
        is_file_exists = os.path.exists(attachment)
        if not is_file_exists:
            print(f"File {attachment} does`n exist")
        else:
            basename = os.path.basename(attachment)
            file_size = os.path.getsize(attachment)
            file = MIMEBase("application", f"octet-stream: name={basename}")
            file.set_payload(open(attachment, "rb").read())
            file.add_header("Content-Description", attachment)
            file.add_header("Content-Description", f"attachment; filename={attachment}: size={file_size}")
            encoders.encode_base64(file)
            msg.attach(file)

    test_to_send = MIMEText(mail_body, "html")
    msg.attach(test_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN_API)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()
