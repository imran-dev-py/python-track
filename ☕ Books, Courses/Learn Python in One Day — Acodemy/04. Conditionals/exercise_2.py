email_address = input('Enter your email address: ')

gmail = 'gmail'
yahoo = 'yahoo'
hotmail = 'hotmail'

if (gmail in email_address):
    print('This is a gmail user')
elif (yahoo in email_address):
    print('This is a yahoo user')
elif (hotmail in email_address):
    print('This is a hotmail user')
else:
    print('This is another user')
