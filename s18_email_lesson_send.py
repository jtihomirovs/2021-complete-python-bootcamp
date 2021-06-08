import getpass
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())

smtp_object.starttls()

email = getpass.getpass('Email please: ')
password = getpass.getpass('Password please: ')

smtp_object.login(email, password)

from_address = email
to_address = email
subject = input('Enter the subject line: ')
message = input('Enter the body message: ')

msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()
