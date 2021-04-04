from email.mime.text import MIMEText
import smtplib

def send_mail(email, height):
    from_email = "test@testmail.com"
    from_password = 'NA'
    to_email = email

    subject = "Height data"
    message = f"Hey there, Your height is <strong> {height} </strong>"

    msg = MIMEText(message, 'html')
    msg["subject"] = subject
    msg["to"] = to_email
    msg["from"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
