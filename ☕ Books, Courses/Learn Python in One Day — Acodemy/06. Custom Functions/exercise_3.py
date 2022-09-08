name = ['John', 'Mark', 'George']
surname = ['Smith', 'Pond', 'London']

new_email = []


def email_generator(email='@gmail', extension='.com'):
    global name, surname
    for name, surname in zip(name, surname):
        a = f'{name}{surname}@gmail.com'
        new_email.append(a)


email_generator()
print(new_email)

'''
List Comprehesion
'''
name_ = ['John', 'Mark', 'George']
surname_ = ['Smith', 'Pond', 'London']


def email(name, surname, email='gmail', extension='.com'):
    return f'{name}{surname}{email}{extension}'


y = [email(name, surname, '@yahoo') for name, surname in zip(name_, surname_)]
print(y)
