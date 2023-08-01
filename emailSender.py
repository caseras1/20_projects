# Steps for making this code

# Go over to our gmail account and setup 2 factur authentication
# Generate app password
# create a function to send the mail

from email.message import EmailMessage
from emailSender import password
import ssl
import smtplib

email_sender = 'erascas7@gmail.com'
email_password = password

email_receiver = 'dabodi7714@mliok.com'

subject = "Going on a trip"
body = """
We want to go on a vacation to Bali
"""
# Variables for email message 
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())




