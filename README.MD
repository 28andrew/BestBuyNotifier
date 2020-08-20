# BestBuy Price Notifier

Python3 script to check the price of a BestBuy product and sends an email if it has a sale.

# Usage
1. Install dependencies (`pip install -r requirements.txt`)
2. Obtain an API key at [BestBuy Developer](https://developer.bestbuy.com/).
3. Edit script with API key, product details, and SMTP details.
4. Test SMTP email send by manually setting the `message` variable to a non-empty string and running the script. After verifying that SMTP email send works, make sure `message` variable is initialized to an empty string as in the original script.
5. Periodically run the script. Example of crontab entry to run every 20 minutes and log to a file:
```
*/20 * * * * /usr/bin/python3 /home/user/bestbuy/main.py >> /home/user/bestbuy/cron.log 2>&1
```

# Known Issues

- If run periodically, multiple emails will be sent for a sale as the script does not remember if it has sent an email already for a sale.