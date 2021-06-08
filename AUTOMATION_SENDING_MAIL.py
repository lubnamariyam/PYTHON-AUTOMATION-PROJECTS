import pandas as pd
import smtplib
import xlrd

my_email = "xyz@gmail.com"
my_password = "abcdefghi"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(my_email,my_password)

email_list = pd.read_excel(r'C:\Users\HP\Desktop\emaildata2.xls')

names = email_list['Name']
emails = email_list['Email']
messages = email_list['Message']

# iterate through the records
for i in range(len(emails)):
    # for every record get the name and the email addresses
    name = names[i]
    email = emails[i]
    message = messages[i]


    # sending the email
    server.sendmail(my_email, email, message)

# close the smtp server
server.close()