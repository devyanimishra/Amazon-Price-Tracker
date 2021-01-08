import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Juarez-JRZ23UK-NA-Hawaiian-Fingerboard/dp/B06Y1KSYCR/ref=sr_1_5?dchild=1&keywords=ukulele&qid=1608545307&sr=8-5"

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66' }

def check_price():
    page = requests.get (URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title= soup.find(id="productTitle")
    title=title.get_text().strip()
    price= soup.find(id="priceblock_ourprice")
    price=price.get_text()

    converted_price=price[2:7]
    final_price = float(converted_price.replace(',',''))

    if(final_price < 2000):
        send_mail()
        
        
    
    print('TITLE: ' + title)
    #print('CONV PRICE ' +converted_price)
    #print('WITHOUT COMMA ' +final_price)
    print('OG PRICE ' +price)
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('your email ID',' your password ')
    
    subject = 'Price has been lowered !!'
    body = 'Check this product link again !! https://www.amazon.in/Juarez-JRZ23UK-NA-Hawaiian-Fingerboard/dp/B06Y1KSYCR/ref=sr_1_5?dchild=1&keywords=ukulele&qid=1608545307&sr=8-5 '
    msg = f"Subject: {subject} \n\n {body}"
    
    server.sendmail( 
    'your email ID',
    'your email ID',
    msg)
    
    print("EMAIL HAS BEEN SENT ")
    server.quit()
    
    
    
check_price()
    
