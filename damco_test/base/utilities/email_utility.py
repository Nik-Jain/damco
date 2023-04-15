import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from . import CONSTANT

def create_email(body, subject, sender, receiver, filepath=None):
    
        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))
        if filepath:
            
            # Open the file in python as a binary
            attachment= open(filepath, 'rb')  # r for read and b for binary

            # Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filepath)
            msg.attach(attachment_package)
        
        # Cast as string
        text = msg.as_string()
        return text
    

# Define the email function (dont call it email!)
def send_emails(smtp_server, smtp_port, sender, receiver, msg):
        password = os.environ.get('EMAIL_PASSWORD')
        # Connect with the server
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(sender, password)
        print("Successfully connected to server")
        
        # Send emails to "person" as list is iterated
        TIE_server.sendmail(sender, receiver, msg)
        print(f"Email sent to: {receiver}")
        
        # Close the port
        TIE_server.quit()

def send_failure_email(success_count, failure_count, filepath, server, port, sender, receiver):
    body = ''.join([CONSTANT.FAIL_EMAIL_BODY_1, str(failure_count), CONSTANT.FAIL_EMAIL_BODY_2])
    subject = CONSTANT.FAILURE_EMAIL_SUBJECT
    receiver = ','.join(receiver)
    msg = create_email(body, subject, sender, receiver, filepath)
    send_emails(server, port, sender, receiver, msg)

def send_success_email(success_count, server, port, sender, receiver):
    body = CONSTANT.SUCCESS_EMAIL_BODY + str(success_count)
    subject = CONSTANT.SUCCESS_EMAIL_SUBJECT
    receiver = ','.join(receiver)
    msg = create_email(body, subject, sender, receiver)
    send_emails(server, port, sender, receiver, msg)
