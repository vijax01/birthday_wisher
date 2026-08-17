import os, pandas, datetime as dt, smtplib, random
os.system('cls')


now = dt.datetime.now()


MY_EMAIL = os.environ['MY_EMAIL']
PASSWORD = os.environ['PASSWORD']


persons = []
with open('data.csv') as file:
    data = pandas.read_csv(file)
    for (index, row) in data.iterrows():
        if row.month == now.month and row.day == now.day:
            persons.append([row['name'], row['email']])

for name,email in persons:
    l_no = random.randint(1,3)
    letter = ''
    with open(f'templates/t{l_no}.txt') as file:
        letter = file.read()
        letter = letter.replace('[name]', name.capitalize())
        letter = 'Subject:Happy Birthday\n\n' + letter
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=letter
        )

print('Birthday Wish sent successfully')
        
