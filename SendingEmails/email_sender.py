import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jane Doe'
email['to'] = 'narcy611@yahoo.com'
email['subject'] = 'You got mail'

email.set_content(html.substitute({'name': 'TinTin'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery1@gmail,com', 'helloztm')
    smtp.send_message(email)
    print("Email sent")
