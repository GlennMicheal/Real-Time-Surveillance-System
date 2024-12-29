import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send alert email to security
def send_alert_email(subject, body, to_email):
    from_email = "your-email@gmail.com"
    password = "your-email-password"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Real-time threat detection integration with email alerts
if confidence > 0.5:  # Threshold for detecting suspicious activity
    subject = "Suspicious Activity Detected"
    body = "A suspicious activity was detected by the surveillance system. Immediate attention required!"
    send_alert_email(subject, body, "security-team@example.com")
