import os
import re
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
load_dotenv()

my_mail = os.environ["MY_MAIL"]
password = os.environ["PASSWORD"]

#================= Instructions ==============
# Just paste the product link from amazon by clicking share and then copy.
# Enter just the price of product not any price symbols.
BUY_PRICE = 80
PRODUCT_LIVE_URL = "https://amzn.in/d/0eRcvciR"

live_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://google.com",
    "DNT": "1",
}

response = requests.get(url=PRODUCT_LIVE_URL, headers=live_header)
soup = BeautifulSoup(response.text, "html.parser")

# ================= ROBUST LIVE WEBSITE SCRAP =================
title_element = soup.find(name="span", id="productTitle")
product_name = title_element.getText().strip() if title_element else "Unknown Amazon Product"

price_text = None
price_element = soup.find("span", class_="a-offscreen")
if price_element and price_element.getText().strip():
    price_text = price_element.getText().strip()

if not price_text:
    price_whole = soup.find("span", class_="a-price-whole")
    if price_whole and price_whole.getText().strip():
        price_text = price_whole.getText().strip()

if not price_text:
    price_block = soup.find("span", id="priceblock_ourprice") or soup.find("span", id="priceblock_dealprice")
    if price_block and price_block.getText().strip():
        price_text = price_block.getText().strip()

if price_text:
    cleaned_price_string = re.sub(r"[^\d.]", "", price_text)
    try:
        final_price = float(cleaned_price_string)

        #=========== Mail Alert if a DEAL is Found==========
        if final_price <= BUY_PRICE:
            with smtplib.SMTP(os.environ["SMTP"]) as connection:
                connection.starttls()
                connection.login(user=my_mail, password=password)
                message = f"The Price of the {product_name} you wanted is available at ₹{final_price}. Go to {PRODUCT_LIVE_URL} to purchase it.\n\nAmazon Bot at your Service"
                connection.sendmail(
                    from_addr=my_mail,
                    to_addrs=os.environ["TO_EMAIL"],
                    msg=f"Subject:Amazon Price Drop Alert! 🤖\n\n{message}".encode("utf-8")
                )
    except ValueError:
        print(f"❌ Error: Found price text '{price_text}' but regex couldn't convert it to a number.")
else:
    print(
        "❌ Error: All fallback elements returned empty text. Amazon might be serving a CAPTCHA page or testing a completely new layout.")