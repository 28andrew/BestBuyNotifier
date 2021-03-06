# BestBuy Price Notifier

Python3 script to check the price of a BestBuy product and send an email if it has a sale.

# Usage
1. Install dependencies (`pip install -r requirements.txt`)
2. Obtain an API key at [BestBuy Developer](https://developer.bestbuy.com/). *Note: BestBuy Developer will not grant API keys to users with email addresses from free services like Gmail or Yahoo. You will have to use an email address on a custom domain, such as one from work or school.*
3. Edit script with API key, product details, and SMTP details.
4. Test SMTP email send by manually setting the `message` variable to a non-empty string (e.g "Test email message") and running the script. After verifying that SMTP email send works, undo changes to the `message` variable.
5. Periodically run the script. Example of crontab entry to run every 20 minutes and log to a file:
```bash
*/20 * * * * /usr/bin/python3 /home/user/bestbuy/main.py >> /home/user/bestbuy/cron.log 2>&1
```

# Sample Email

![image](https://user-images.githubusercontent.com/9660418/90815944-17a66d00-e2f1-11ea-9e44-cc5006ecb1c1.png)

# Known Issues

- If ran periodically, multiple emails will be sent for a sale as the script does not remember if it has sent an email already for a sale.
