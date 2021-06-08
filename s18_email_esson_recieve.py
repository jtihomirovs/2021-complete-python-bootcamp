import email
import getpass
import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

emailVar = getpass.getpass('Email: ')
passwordVar = getpass.getpass('Password: ')

M.login(emailVar, passwordVar)
print(M.list())
print(M.select('inbox'))

# Define search criteria and do search
typ, data = M.search(None, 'SUBJECT "NEW TEST PYTHON"')

# Get email ID which is found by criteria above
email_id = data[0]

# Fetch result
result, email_data = M.fetch(email_id, '(RFC822)')

# Print result
print('Result data: ', result)
print('Email data: ', email_data)

# Get raw email data
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

# Parse and print: b'Hello this is a test\r\n'
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
