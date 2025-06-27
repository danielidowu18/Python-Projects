import random
import pandas
import datetime as dt
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day

my_email = "jidog.100@gmail.com"
password = "yqjyxqifhsrkiyne"

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthday_data = pandas.read_csv("./AutomatedEmails/AutomatedBirthdayWisher/birthdays.csv")
data_dict = birthday_data.to_dict(orient="records")
for record in data_dict:
    if record["month"] == today_month and record["day"] == today_day:
        rand_letter = random.choice(letter_list)
        with open(f"./AutomatedEmails/AutomatedBirthdayWisher/letter_templates/{rand_letter}") as letter:
            mail = letter.read()
            named_mail = mail.replace("[NAME]", record["name"])
        
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=record["email"], msg=f"Subject:Happy Birthday\n\n{named_mail}")
            



