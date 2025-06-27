import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


URL = "https://www.amazon.com/HP-Touchscreen-i7-1165G7-Backlit-Accessories/dp/B0C9FN56XX/ref=sr_1_2_sspa?keywords=hp%2Blaptops&qid=1696454112&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
max_price = 670
my_email = "jidog.100@gmail.com"
password = "yqjyxqifhsrkiyne"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}


with requests.get(url=URL, headers=header) as response:
    contents = response.text

soup = BeautifulSoup(markup=contents, features="lxml")
current_whole_price_tag = soup.find(name="span", class_="a-price-whole")
current_decimal_price_tag = soup.find(name="span", class_="a-price-fraction")
current_price = float(f"{current_whole_price_tag.get_text()}{current_decimal_price_tag.get_text()}")


if current_price < max_price:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:It's time to buy\n\nHP Laptop goes for ${current_price}\n{URL}")
