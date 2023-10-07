from email.message import EmailMessage
import smtplib
import ssl

email_send = 'Enter-Your-Email'
email_pass = 'Enter-Your-Password'
email_rec = input('Enter your the gmail account of the reciever:')

subject = 'Enter Subject'
body = '''
Enter Body
'''

em = EmailMessage()
em['From'] = email_send
em['To'] = email_rec
em['Subject'] = subject  # Changed 'subject' to 'Subject'
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_send, email_pass)
    smtp.sendmail(email_send, email_rec, em.as_string())
