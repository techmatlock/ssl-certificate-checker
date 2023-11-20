import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def send_email():
    smtp_server = 'smtp.example.com'

    # Email parameters
    from_email = 'no-reply@example.comn'
    to_email = 'receiving-email@example.com'
    subject = "Certificate expiration warning"
    body = "List of expiring certificates can be found in attachment"

    # Setup MIME
    msg = MIMEMultipart(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    msg.attach(MIMEText(body, 'plain'))

    # Attaching the CSV file
    filename = "output.csv"
    attachment = open("output.csv", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")

    msg.attach(part)

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()  # Upgrade to secure connection if using TLS
        server.sendmail(from_email, to_email, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()