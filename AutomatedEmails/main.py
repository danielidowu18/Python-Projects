import datetime as dt
import random
import smtplib

now = dt.datetime.now()
current_day = now.weekday()

my_email = "jidog.100@gmail.com"
password = "yqjyxqifhsrkiyne"

with open(file="./AutomatedBirthdayWisher/quotes.txt", encoding="utf8") as quotes:
    quotes_data = quotes.readlines()
current_quote = random.choice(quotes_data).encode(encoding="utf8")



if current_day == 6:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(msg=f"Subject:Quote of the Day\n\n{current_quote}", from_addr=my_email, to_addrs="archg1998@gmail.com")
        
