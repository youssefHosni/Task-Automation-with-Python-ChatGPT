import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_emails, subject, message):
    # Set up the SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = subject

    # Attach the message as plain text
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)
        print('Email sent successfully')

    except smtplib.SMTPException as e:
        print(f'Error: Unable to send email. {str(e)}')

    finally:
        # Disconnect from the SMTP server
        server.quit()

# Provide the email details
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_emails = ['recipient1@example.com', 'recipient2@example.com']
subject = 'Automated Email'
message = 'This is an automated email sent using Python.'

# Send the email
send_email(sender_email, sender_password, recipient_emails, subject, message)