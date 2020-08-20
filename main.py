import json
import urllib.request
import smtplib
import ssl
from email.message import EmailMessage

# API Settings
apiURL = "https://api.bestbuy.com"
bestbuyAPIKey = "CHANGE TO YOUR API KEY"

# Product Settings
productName = "Example Laptop"
productSKU = "6409400"
productRegularPrice = 1599.99

# Email Settings
host = "SMTP HOST"
port = 465
sslSecure = True
user = "SMTP USER"
password = "SMTP PASSWORD"
fromEmail = "price-notifier@yourdomain.com"
toEmail = "yourpersonalemail@yourdomain.com"

with urllib.request.urlopen(f"{apiURL}/v1/products/{productSKU}.json?show=sku,name,onlineAvailability"
                            ",freeShipping,salePrice,regularPrice,onSale,priceUpdateDate,dollarSavings"
                            f"&apiKey={bestbuyAPIKey}") as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4, sort_keys=True))
    savings = data["dollarSavings"]
    onSale = data["onSale"]
    regularPrice = data["regularPrice"]
    salePrice = data["salePrice"]
    freeShipping = data["freeShipping"]

    message = ""
    if savings > 0.0:
        message = f"Savings is {savings}"
    elif onSale:
        message = "Now on sale"
    elif regularPrice < productRegularPrice:
        message = f"Regular price is lower at {regularPrice}"
    elif salePrice < productRegularPrice or salePrice < regularPrice:
        message = f"Sale price is lower at {salePrice}"
    elif not freeShipping:
        message = "No more free shipping"

    if message:
        emailText = f"BestBuy {productName} Notifier"
        emailText += "\n---------------------------------------------------------------------------------------------"
        emailText += f"\nMessage: {message}"
        emailText += f"\nJSON: {data}"
        emailText += "\n---------------------------------------------------------------------------------------------"

        msg = EmailMessage()
        msg['Subject'] = f"{productName} Notification"
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg.preamble = message
        msg.set_content(emailText)

        # Send email
        context = ssl.create_default_context() if sslSecure else ssl._create_unverified_context()
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(user, password)
            server.send_message(msg)
            print(f"Email sent with message: {message}")
    else:
        print("Nothing special")
